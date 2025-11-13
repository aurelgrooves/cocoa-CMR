import os, zipfile, shutil

APP_NAME = "EU_Cocoa_Map_App"
URL = "https://experience.arcgis.com/experience/e7e146d12dbd41c5928b15c75df61590"
COLOR = "#6B3A1E"

# Create folder tree
dirs = [
    f"{APP_NAME}/app/src/main/java/com/example/eucocoamap",
    f"{APP_NAME}/app/src/main/res/drawable",
    f"{APP_NAME}/app/src/main/res/layout",
    f"{APP_NAME}/app/src/main/res/values",
    f"{APP_NAME}/app/src/main/res/mipmap-anydpi-v26",
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Kotlin activity
main_kt = f"""package com.example.eucocoamap
import android.content.Intent
import android.net.Uri
import androidx.activity.ComponentActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
class MainActivity : ComponentActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Handler(Looper.getMainLooper()).postDelayed({{
            val target = "{URL}"
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse(target)).apply {{
                addCategory(Intent.CATEGORY_BROWSABLE)
            }}
            startActivity(intent)
            finish()
        }}, 1500)
    }}
}}
"""
open(f"{APP_NAME}/app/src/main/java/com/example/eucocoamap/MainActivity.kt","w").write(main_kt)

# Manifest
manifest = """<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.eucocoamap">
    <application
        android:allowBackup="true"
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher"
        android:theme="@style/Theme.EUCocoaMap.Splash">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:theme="@style/Theme.EUCocoaMap.Splash">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>"""
open(f"{APP_NAME}/app/src/main/AndroidManifest.xml","w").write(manifest)

# activity_main
layout = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:background="@drawable/splash_bg">
</LinearLayout>"""
open(f"{APP_NAME}/app/src/main/res/layout/activity_main.xml","w").write(layout)

# themes
themes = f"""<resources xmlns:tools="http://schemas.android.com/tools">
    <style name="Theme.EUCocoaMap" parent="Theme.Material3.DayNight.NoActionBar" />
    <style name="Theme.EUCocoaMap.Splash" parent="Theme.SplashScreen">
        <item name="windowSplashScreenBackground">{COLOR}</item>
        <item name="windowSplashScreenAnimatedIcon">@drawable/splash_bg</item>
        <item name="postSplashScreenTheme">@style/Theme.EUCocoaMap</item>
    </style>
</resources>"""
open(f"{APP_NAME}/app/src/main/res/values/themes.xml","w").write(themes)

# strings
open(f"{APP_NAME}/app/src/main/res/values/strings.xml","w").write(
    '<resources><string name="app_name">EU Sustainable Cocoa Programme Map Platform</string></resources>'
)

# colors
open(f"{APP_NAME}/app/src/main/res/values/colors.xml","w").write(
    f'<resources><color name="brown_primary">{COLOR}</color></resources>'
)

# splash background
splash_bg = """<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@color/brown_primary" />
    <item>
        <bitmap android:gravity="center" android:src="@drawable/splash_image" />
    </item>
</layer-list>"""
open(f"{APP_NAME}/app/src/main/res/drawable/splash_bg.xml","w").write(splash_bg)

# Gradle basics
open(f"{APP_NAME}/settings.gradle","w").write('rootProject.name = "EU_Cocoa_Map_App"\ninclude(":app")\n')
open(f"{APP_NAME}/build.gradle","w").write("task clean(type: Delete) { delete rootProject.buildDir }\n")
open(f"{APP_NAME}/app/build.gradle","w").write("""plugins { id 'com.android.application' }
android { namespace 'com.example.eucocoamap'; compileSdk 34
defaultConfig { applicationId "com.example.eucocoamap"; minSdk 26; targetSdk 34; versionCode 1; versionName "1.0" }
buildTypes { release { minifyEnabled false } } }
dependencies { implementation 'androidx.activity:activity-ktx:1.9.0' }
""")

# Zip everything
zip_path = f"{APP_NAME}.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(APP_NAME):
        for f in files:
            path = os.path.join(root, f)
            z.write(path, os.path.relpath(path, APP_NAME))

print(f"Created {zip_path}")
""
