import os
import sys
import shutil

ROOT_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

RES_DIR = os.path.join(ROOT_DIR, "android", "app", "src", "main", "res")
MANIFEST_PATH = os.path.join(ROOT_DIR, "android", "app", "src", "main", "AndroidManifest.xml")
WRAPPER_PROPS = os.path.join(ROOT_DIR, "android", "gradle", "wrapper", "gradle-wrapper.properties")
JAVA_DIR = os.path.join(ROOT_DIR, "android", "app", "src", "main", "java")
STYLES_PATH = os.path.join(RES_DIR, "values", "styles.xml")

ICON_MAP = {
    "mipmap-mdpi": os.path.join(REPO_DIR, "icon-72.png"),
    "mipmap-hdpi": os.path.join(REPO_DIR, "icon-72.png"),
    "mipmap-xhdpi": os.path.join(REPO_DIR, "icon-96.png"),
    "mipmap-xxhdpi": os.path.join(REPO_DIR, "icon-144.png"),
    "mipmap-xxxhdpi": os.path.join(REPO_DIR, "icon-192.png"),
}

for folder, icon_src in ICON_MAP.items():
    target_dir = os.path.join(RES_DIR, folder)
    if os.path.exists(target_dir) and os.path.exists(icon_src):
        for name in ["ic_launcher.png", "ic_launcher_round.png", "ic_launcher_foreground.png"]:
            shutil.copy2(icon_src, os.path.join(target_dir, name))

if os.path.exists(MANIFEST_PATH):
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest_text = f.read()

    permissions = [
        '<uses-permission android:name="android.permission.INTERNET" />',
        '<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />',
        '<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />',
        '<uses-permission android:name="android.permission.CAMERA" />',
        '<uses-feature android:name="android.hardware.camera" android:required="false" />',
        '<uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />'
    ]

    for perm in permissions:
        if perm not in manifest_text:
            manifest_text = manifest_text.replace("</manifest>", f"    {perm}\n</manifest>")

    if 'android:usesCleartextTraffic="true"' not in manifest_text:
        manifest_text = manifest_text.replace("<application", '<application android:usesCleartextTraffic="true"')

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        f.write(manifest_text)

if os.path.exists(STYLES_PATH):
    with open(STYLES_PATH, "r", encoding="utf-8") as f:
        styles_text = f.read()

    items_to_add = (
        '        <item name="android:windowFullscreen">true</item>\n'
        '        <item name="android:windowContentOverlay">@null</item>\n'
        '        <item name="android:windowLayoutInDisplayCutoutMode">shortEdges</item>\n'
    )

    if '<style name="AppTheme.NoActionBar"' in styles_text:
        if 'android:windowFullscreen' not in styles_text:
            styles_text = styles_text.replace(
                '<style name="AppTheme.NoActionBar" parent="Theme.AppCompat.DayNight.NoActionBar">',
                f'<style name="AppTheme.NoActionBar" parent="Theme.AppCompat.DayNight.NoActionBar">\n{items_to_add}'
            )

    with open(STYLES_PATH, "w", encoding="utf-8") as f:
        f.write(styles_text)

if os.path.exists(JAVA_DIR):
    for root, _, files in os.walk(JAVA_DIR):
        if "MainActivity.java" in files:
            main_activity_path = os.path.join(root, "MainActivity.java")
            with open(main_activity_path, "r", encoding="utf-8") as f:
                content = f.read()

            pkg_line = ""
            for line in content.splitlines():
                if line.strip().startswith("package "):
                    pkg_line = line.strip()
                    break

            java_code = f"""{pkg_line}

import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {{
    @Override
    protected void onCreate(Bundle savedInstanceState) {{
        super.onCreate(savedInstanceState);
        hideSystemUI();
    }}

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {{
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {{
            hideSystemUI();
        }}
    }}

    private void hideSystemUI() {{
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {{
            WindowInsetsController controller = getWindow().getInsetsController();
            if (controller != null) {{
                controller.hide(WindowInsets.Type.statusBars() | WindowInsets.Type.navigationBars());
                controller.setSystemBarsBehavior(WindowInsetsController.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE);
            }}
        }} else {{
            View decorView = getWindow().getDecorView();
            decorView.setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_FULLSCREEN
            );
        }}
    }}
}}
"""
            with open(main_activity_path, "w", encoding="utf-8") as f:
                f.write(java_code)

if os.path.exists(WRAPPER_PROPS):
    with open(WRAPPER_PROPS, "r", encoding="utf-8") as f:
        props = f.read()
    props = props.replace("-all.zip", "-bin.zip")
    with open(WRAPPER_PROPS, "w", encoding="utf-8") as f:
        f.write(props)
