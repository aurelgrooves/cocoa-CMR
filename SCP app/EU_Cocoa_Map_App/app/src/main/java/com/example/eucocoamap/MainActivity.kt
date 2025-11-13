package com.example.eucocoamap
import android.content.Intent
import android.net.Uri
import androidx.activity.ComponentActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Handler(Looper.getMainLooper()).postDelayed({
            val target = "https://experience.arcgis.com/experience/1dee92e965b744e080ea8df7036159bc"
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse(target)).apply {
                addCategory(Intent.CATEGORY_BROWSABLE)
            }
            startActivity(intent)
            finish()
        }, 1500)
    }
}
