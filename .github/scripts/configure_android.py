import os
import shutil
import xml.etree.ElementTree as ET

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RES_DIR = os.path.join(BASE_DIR, "android", "app", "src", "main", "res")
MANIFEST_PATH = os.path.join(BASE_DIR, "android", "app", "src", "main", "AndroidManifest.xml")

ICON_MAP = {
    "mipmap-mdpi": os.path.join(BASE_DIR, "icon-72.png"),
    "mipmap-hdpi": os.path.join(BASE_DIR, "icon-72.png"),
    "mipmap-xhdpi": os.path.join(BASE_DIR, "icon-96.png"),
    "mipmap-xxhdpi": os.path.join(BASE_DIR, "icon-144.png"),
    "mipmap-xxxhdpi": os.path.join(BASE_DIR, "icon-192.png"),
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

