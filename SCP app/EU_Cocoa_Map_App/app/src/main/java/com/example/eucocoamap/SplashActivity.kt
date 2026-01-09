package com.example.eucocoamap

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.util.DisplayMetrics
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity

class SplashActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        val logo = findViewById<ImageView>(R.id.splashLogo)

        // ➤ Resize ImageView to 70% of screen width
        val dm = DisplayMetrics()
        windowManager.defaultDisplay.getMetrics(dm)
        val screenWidth = dm.widthPixels
        val targetWidth = (screenWidth * 0.70).toInt()

        val params = logo.layoutParams
        params.width = targetWidth
        logo.layoutParams = params

        // ➤ Open your ArcGIS URL after 1.5 seconds
        Handler(Looper.getMainLooper()).postDelayed({
            val intent = Intent(Intent.ACTION_VIEW,
                Uri.parse("https://experience.arcgis.com/experience/1dee92e965b744e080ea8df7036159bc")
            )
            startActivity(intent)
            finish()
        }, 1500)
    }
}

