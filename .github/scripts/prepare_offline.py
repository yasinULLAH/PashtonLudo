import os
import shutil
import urllib.request
import re

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WWW_DIR = os.path.join(BASE_DIR, "www")
VENDOR_DIR = os.path.join(WWW_DIR, "vendor")
FONTAWESOME_DIR = os.path.join(VENDOR_DIR, "font-awesome")
FONTAWESOME_CSS_DIR = os.path.join(FONTAWESOME_DIR, "css")
FONTAWESOME_WEBFONTS_DIR = os.path.join(FONTAWESOME_DIR, "webfonts")

if os.path.exists(WWW_DIR):
    shutil.rmtree(WWW_DIR)

os.makedirs(VENDOR_DIR, exist_ok=True)
os.makedirs(FONTAWESOME_CSS_DIR, exist_ok=True)
os.makedirs(FONTAWESOME_WEBFONTS_DIR, exist_ok=True)

for item in os.listdir(BASE_DIR):
    item_path = os.path.join(BASE_DIR, item)
    if os.path.isfile(item_path):
        if item.endswith((".html", ".png", ".ico", ".json", ".txt", ".js")):
            shutil.copy2(item_path, os.path.join(WWW_DIR, item))

with open(os.path.join(WWW_DIR, "pwa-register.js"), "w", encoding="utf-8") as f:
    f.write('console.log("PWA service worker disabled for native APK build.");\n')

URL_MAPPING = {
    "https://cdn.tailwindcss.com/3.4.17": ("vendor/tailwindcss.js", os.path.join(VENDOR_DIR, "tailwindcss.js")),
    "https://cdn.tailwindcss.com": ("vendor/tailwindcss.js", os.path.join(VENDOR_DIR, "tailwindcss.js")),
    "https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js": ("vendor/qrcode.min.js", os.path.join(VENDOR_DIR, "qrcode.min.js")),
    "https://cdn.jsdelivr.net/npm/jsqr@1.4.0/dist/jsQR.js": ("vendor/jsQR.js", os.path.join(VENDOR_DIR, "jsQR.js")),
    "https://unpkg.com/peerjs@1.5.4/dist/peerjs.min.js": ("vendor/peerjs.min.js", os.path.join(VENDOR_DIR, "peerjs.min.js")),
    "https://unpkg.com/peerjs@1.5.2/dist/peerjs.min.js": ("vendor/peerjs.min.js", os.path.join(VENDOR_DIR, "peerjs.min.js")),
    "https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js": ("vendor/chart.umd.min.js", os.path.join(VENDOR_DIR, "chart.umd.min.js")),
    "https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js": ("vendor/xlsx.full.min.js", os.path.join(VENDOR_DIR, "xlsx.full.min.js")),
    "https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js": ("vendor/jspdf.umd.min.js", os.path.join(VENDOR_DIR, "jspdf.umd.min.js")),
    "https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js": ("vendor/jspdf.plugin.autotable.min.js", os.path.join(VENDOR_DIR, "jspdf.plugin.autotable.min.js")),
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css": ("vendor/font-awesome/css/all.min.css", os.path.join(FONTAWESOME_CSS_DIR, "all.min.css")),
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css": ("vendor/animate.min.css", os.path.join(VENDOR_DIR, "animate.min.css")),
    "https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css": ("vendor/sweetalert2.min.css", os.path.join(VENDOR_DIR, "sweetalert2.min.css")),
    "https://cdn.jsdelivr.net/npm/sweetalert2@11": ("vendor/sweetalert2.all.min.js", os.path.join(VENDOR_DIR, "sweetalert2.all.min.js")),
    "https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css": ("vendor/select2.min.css", os.path.join(VENDOR_DIR, "select2.min.css")),
    "https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js": ("vendor/select2.min.js", os.path.join(VENDOR_DIR, "select2.min.js")),
    "https://cdn.datatables.net/1.13.8/css/jquery.dataTables.min.css": ("vendor/jquery.dataTables.min.css", os.path.join(VENDOR_DIR, "jquery.dataTables.min.css")),
    "https://cdn.datatables.net/1.13.8/js/jquery.dataTables.min.js": ("vendor/jquery.dataTables.min.js", os.path.join(VENDOR_DIR, "jquery.dataTables.min.js")),
    "https://cdn.datatables.net/responsive/2.5.0/css/responsive.dataTables.min.css": ("vendor/responsive.dataTables.min.css", os.path.join(VENDOR_DIR, "responsive.dataTables.min.css")),
    "https://cdn.datatables.net/responsive/2.5.0/js/dataTables.responsive.min.js": ("vendor/responsive.dataTables.min.js", os.path.join(VENDOR_DIR, "responsive.dataTables.min.js")),
    "https://cdn.datatables.net/buttons/2.4.2/css/buttons.dataTables.min.css": ("vendor/buttons.dataTables.min.css", os.path.join(VENDOR_DIR, "buttons.dataTables.min.css")),
    "https://cdn.datatables.net/buttons/2.4.2/js/dataTables.buttons.min.js": ("vendor/dataTables.buttons.min.js", os.path.join(VENDOR_DIR, "dataTables.buttons.min.js")),
    "https://cdn.datatables.net/buttons/2.4.2/js/buttons.html5.min.js": ("vendor/buttons.html5.min.js", os.path.join(VENDOR_DIR, "buttons.html5.min.js")),
    "https://cdn.datatables.net/buttons/2.4.2/js/buttons.print.min.js": ("vendor/buttons.print.min.js", os.path.join(VENDOR_DIR, "buttons.print.min.js")),
    "https://cdn.datatables.net/buttons/2.4.2/js/buttons.colVis.min.js": ("vendor/buttons.colVis.min.js", os.path.join(VENDOR_DIR, "buttons.colVis.min.js")),
    "https://code.jquery.com/jquery-3.7.1.min.js": ("vendor/jquery-3.7.1.min.js", os.path.join(VENDOR_DIR, "jquery-3.7.1.min.js")),
    "https://unpkg.com/just-validate@4.3.0/dist/just-validate.production.min.js": ("vendor/just-validate.production.min.js", os.path.join(VENDOR_DIR, "just-validate.production.min.js")),
    "https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js": ("vendor/jszip.min.js", os.path.join(VENDOR_DIR, "jszip.min.js")),
    "https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.2.7/pdfmake.min.js": ("vendor/pdfmake.min.js", os.path.join(VENDOR_DIR, "pdfmake.min.js")),
    "https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.2.7/vfs_fonts.js": ("vendor/vfs_fonts.js", os.path.join(VENDOR_DIR, "vfs_fonts.js")),
    "https://unpkg.com/html5-qrcode@2.3.8/html5-qrcode.min.js": ("vendor/html5-qrcode.min.js", os.path.join(VENDOR_DIR, "html5-qrcode.min.js")),
}

EXTRA_FILES = {
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-solid-900.woff2": os.path.join(FONTAWESOME_WEBFONTS_DIR, "fa-solid-900.woff2"),
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-solid-900.ttf": os.path.join(FONTAWESOME_WEBFONTS_DIR, "fa-solid-900.ttf"),
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-regular-400.woff2": os.path.join(FONTAWESOME_WEBFONTS_DIR, "fa-regular-400.woff2"),
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-regular-400.ttf": os.path.join(FONTAWESOME_WEBFONTS_DIR, "fa-regular-400.ttf"),
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-brands-400.woff2": os.path.join(FONTAWESOME_WEBFONTS_DIR, "fa-brands-400.woff2"),
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-brands-400.ttf": os.path.join(FONTAWESOME_WEBFONTS_DIR, "fa-brands-400.ttf"),
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-v4compatibility.woff2": os.path.join(FONTAWESOME_WEBFONTS_DIR, "fa-v4compatibility.woff2"),
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-v4compatibility.ttf": os.path.join(FONTAWESOME_WEBFONTS_DIR, "fa-v4compatibility.ttf"),
}

def download_file(url, target_path):
    if os.path.exists(target_path) and os.path.getsize(target_path) > 0:
        return
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        content = resp.read()
    with open(target_path, "wb") as f:
        f.write(content)

for url, (_, target_path) in URL_MAPPING.items():
    download_file(url, target_path)

for url, target_path in EXTRA_FILES.items():
    download_file(url, target_path)

index_html_path = os.path.join(WWW_DIR, "index.html")
if os.path.exists(index_html_path):
    with open(index_html_path, "r", encoding="utf-8") as f:
        content = f.read()
    for remote_url, (local_rel, _) in URL_MAPPING.items():
        content = content.replace(f'src="{remote_url}"', f'src="{local_rel}"')
        content = content.replace(f"src='{remote_url}'", f"src='{local_rel}'")
        content = content.replace(f'href="{remote_url}"', f'href="{local_rel}"')
        content = content.replace(f"href='{remote_url}'", f"href='{local_rel}'")
    content = re.sub(r'<link[^>]*href=["\']https://fonts\.googleapis\.com[^"\']*["\'][^>]*>', '', content)
    content = re.sub(r'<link[^>]*href=["\']https://fonts\.gstatic\.com[^"\']*["\'][^>]*>', '', content)
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(content)

snakes_html_path = os.path.join(WWW_DIR, "snakes.html")
if os.path.exists(snakes_html_path):
    with open(snakes_html_path, "r", encoding="utf-8") as f:
        content = f.read()
    for remote_url, (local_rel, _) in URL_MAPPING.items():
        content = content.replace(f'src="{remote_url}"', f'src="{local_rel}"')
        content = content.replace(f"src='{remote_url}'", f"src='{local_rel}'")
        content = content.replace(f'href="{remote_url}"', f'href="{local_rel}"')
        content = content.replace(f"href='{remote_url}'", f"href='{local_rel}'")
    with open(snakes_html_path, "w", encoding="utf-8") as f:
        f.write(content)

