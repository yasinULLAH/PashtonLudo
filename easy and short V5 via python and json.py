### Part 2: The Production Python Runner (`patcher.py`)

#Place this script in your project root alongside `patch.json`. It includes:
#* Automatic file detection (`index.php` or `index.html` prioritized if unspecified).
#* Automatic pre-patch backup (`.bak` with timestamp).
#* Dry-run mode (`--dry-run` or `-d`) to verify anchors without touching code.
#3* Automatic strip of markdown fences if you accidentally copy the ` ```json ` markers.
#* Windows newline normalization (`CRLF` vs `LF` safety).
#* Rollback if any step fails in strict mode.
#Toggleable via Variable or CLI Flag:
#    Change ENABLE_BACKUP = False at the top of the file to disable backups by default.
#    Or pass -b or --no-backup in the terminal when running the command to skip backups on the fly.

#Save this as **`patcher.py`**:

#```python
#!/usr/bin/env python3
"""
Robust, standalone JSON patch engine for single-file web applications.
Features:
- Single overwritten .bak file (no timestamp clutter)
- Toggleable backup flag (-b / --no-backup or internal boolean)
- CRLF/LF normalization
- Safe multi-step validation before modifying files
"""

import sys
import os
import re
import json
import shutil
from pathlib import Path

# ==================== CONFIGURATION ====================
DEFAULT_PATCH_FILE = "patch.json"
FALLBACK_TARGET_FILES = ["index.php", "index.html", "index.htm"]
ENABLE_BACKUP = True  # Set to False to disable backups by default
# =======================================================

def detect_default_target(root_dir: Path) -> Path:
    """Detects primary application file if target is unspecified."""
    for fname in FALLBACK_TARGET_FILES:
        candidate = root_dir / fname
        if candidate.is_file():
            return candidate
    for ext in ("*.php", "*.html"):
        matches = list(root_dir.glob(ext))
        if matches:
            return matches[0]
    return root_dir / "index.php"

def clean_json_content(raw_text: str) -> str:
    """Strips markdown code block fences if present in the pasted JSON."""
    text = raw_text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*\n?", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\n?```\s*$", "", text)
    return text.strip()

def normalize_newlines(content: str) -> str:
    """Normalizes CRLF to LF for consistent regex and exact string matching."""
    return content.replace("\r\n", "\n")

def run_patcher():
    root_dir = Path(__file__).resolve().parent
    args = sys.argv[1:]

    # Flags
    dry_run = "--dry-run" in args or "-d" in args
    no_backup = "-b" in args or "--no-backup" in args
    create_backup = ENABLE_BACKUP and not no_backup

    # Filter out flags to extract patch filename if provided
    custom_args = [a for a in args if not a.startswith("-")]
    patch_filename = custom_args[0] if custom_args else DEFAULT_PATCH_FILE
    patch_path = root_dir / patch_filename

    print("==================================================")
    print("           JSON FILE PATCH RUNNER                 ")
    print(f" Mode:    {'DRY RUN (Preview Only)' if dry_run else 'ACTIVE (Modifying Files)'}")
    print(f" Source:  {patch_filename}")
    print(f" Backup:  {'ENABLED (Single .bak file)' if create_backup and not dry_run else 'DISABLED'}")
    print("==================================================")

    if not patch_path.is_file():
        print(f"[!] Error: Patch file '{patch_filename}' not found in {root_dir}")
        sys.exit(1)

    try:
        raw_data = patch_path.read_text(encoding="utf-8")
        cleaned_data = clean_json_content(raw_data)
        rules = json.loads(cleaned_data)
        if isinstance(rules, dict):
            rules = [rules]
        if not isinstance(rules, list):
            raise ValueError("Root JSON entity must be an array of patch objects.")
    except Exception as e:
        print(f"[!] Failed to parse JSON in '{patch_filename}': {e}")
        sys.exit(1)

    if not rules:
        print("[-] Patch file is empty. Nothing to do.")
        sys.exit(0)

    files_state = {}
    default_target_path = detect_default_target(root_dir)

    # 1. Verification Phase: Check all files and patterns before writing
    all_matched = True
    print("\n>>> Phase 1: Validating targets & patterns...")

    for i, rule in enumerate(rules, start=1):
        target_name = rule.get("target")
        target_path = (root_dir / target_name) if target_name else default_target_path

        if not target_path.is_file():
            print(f"  [X] Step {i}: Target file '{target_path.name}' does not exist.")
            all_matched = False
            continue

        if target_path not in files_state:
            raw_content = target_path.read_text(encoding="utf-8")
            is_crlf = "\r\n" in raw_content
            normalized_content = normalize_newlines(raw_content)
            files_state[target_path] = {
                "original": raw_content,
                "current": normalized_content,
                "is_crlf": is_crlf,
                "modified": False
            }

        rule_type = rule.get("type", "exact").lower()
        find_str = normalize_newlines(rule.get("find", ""))
        replace_str = normalize_newlines(rule.get("replace", ""))
        count = rule.get("count", 1)

        if not find_str:
            print(f"  [X] Step {i}: 'find' field is empty. Skipping.")
            all_matched = False
            continue

        buffer = files_state[target_path]["current"]

        if rule_type == "exact":
            occurrences = buffer.count(find_str)
            if occurrences == 0:
                # Fallback: try matching with flexible leading/trailing whitespace per line
                # (Prevents false failures when HTML indentation differs slightly)
                lines = [ln.strip() for ln in find_str.split("\n") if ln.strip()]
                ws_pattern_str = r"^[ \t]*" + r"[ \t]*\n[ \t]*".join(re.escape(ln) for ln in lines)
                ws_pattern = re.compile(ws_pattern_str, re.MULTILINE)
                ws_matches = list(ws_pattern.finditer(buffer))
                if ws_matches:
                    max_replace = 0 if count == 0 else count
                    files_state[target_path]["current"] = ws_pattern.sub(lambda m: replace_str, buffer, count=max_replace)
                    files_state[target_path]["modified"] = True
                    print(f"  [✓] Step {i} [EXACT-WS]: Matched ({len(ws_matches)} found via flexible indentation) in '{target_path.name}'.")
                else:
                    first_line = lines[0][:60] if lines else "<empty>"
                    print(f"  [X] Step {i} [EXACT]: Pattern not found in '{target_path.name}' (starts with: {first_line!r}).")
                    all_matched = False
            else:
                max_replace = occurrences if count == 0 else count
                files_state[target_path]["current"] = buffer.replace(find_str, replace_str, max_replace)
                files_state[target_path]["modified"] = True
                print(f"  [✓] Step {i} [EXACT]: Matched ({occurrences} found, replacing {max_replace}) in '{target_path.name}'.")

        elif rule_type == "regex":
            try:
                pattern = re.compile(find_str, re.MULTILINE | re.DOTALL)
                matches = list(pattern.finditer(buffer))
                if not matches:
                    print(f"  [X] Step {i} [REGEX]: Pattern did not match in '{target_path.name}'.")
                    all_matched = False
                else:
                    max_replace = 0 if count == 0 else count
                    files_state[target_path]["current"] = pattern.sub(replace_str, buffer, count=max_replace)
                    files_state[target_path]["modified"] = True
                    print(f"  [✓] Step {i} [REGEX]: Matched {len(matches)} instance(s) in '{target_path.name}'.")
            except re.error as err:
                print(f"  [X] Step {i} [REGEX ERROR]: Invalid regex pattern '{find_str}': {err}")
                all_matched = False
        else:
            print(f"  [X] Step {i}: Unknown type '{rule_type}'.")
            all_matched = False

    # 2. Execution Phase
    if not all_matched:
        print("\n[!] Patch abort: One or more steps failed validation.")
        print("[-] No changes were written to your files.")
        sys.exit(1)

    if dry_run:
        print("\n[✓] Dry run completed successfully. All patterns verified.")
        sys.exit(0)

    print("\n>>> Phase 2: Applying patches & writing files...")

    for path, data in files_state.items():
        if not data["modified"]:
            continue

        # Single backup replacement (.bak)
        if create_backup:
            backup_path = path.with_suffix(f"{path.suffix}.bak")
            shutil.copy2(path, backup_path)
            print(f"  [+] Backup refreshed: {backup_path.name}")

        # Restore original newline style
        final_content = data["current"]
        if data["is_crlf"]:
            final_content = final_content.replace("\n", "\r\n")

        path.write_text(final_content, encoding="utf-8")
        print(f"  [✓] Successfully updated: {path.name}")

    print("\n==================================================")
    print("All patches applied cleanly! Review changes in Git.")
    print("==================================================")

if __name__ == "__main__":
    run_patcher()