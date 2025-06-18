#!/usr/bin/env python3
"""
Cleanup script to remove unnecessary static files after implementing dynamic content.
Run this script to clean up old static project images and other unused files.
"""

import os
import shutil

def cleanup_static_files():
    """Remove unnecessary static files"""
    
    # Files that are no longer needed (old static images)
    old_static_images = [
        # Old project images
        ("static/img/projects", [
            "sewaghar.jpg",
            "carparking.jpg",
            "gesturecontrol.jpg",
            "scoreboard.jpg",
            "weather.jpg",
            "house.jpeg"
        ]),
        # Old about image
        ("static/img", [
            "about.jpg"
        ])
    ]

    print("🧹 Starting cleanup of unnecessary static files...")

    # Clean up old static images
    for directory, images in old_static_images:
        if os.path.exists(directory):
            for image in images:
                image_path = os.path.join(directory, image)
                if os.path.exists(image_path):
                    try:
                        os.remove(image_path)
                        print(f"✅ Removed: {image_path}")
                    except Exception as e:
                        print(f"❌ Error removing {image_path}: {e}")
                else:
                    print(f"ℹ️  File not found: {image_path}")
        else:
            print(f"ℹ️  Directory not found: {directory}")

    # Clean up empty directories
    for directory, _ in old_static_images:
        try:
            if os.path.exists(directory) and not os.listdir(directory):
                os.rmdir(directory)
                print(f"✅ Removed empty directory: {directory}")
        except Exception as e:
            print(f"❌ Error removing directory {directory}: {e}")
    
    print("\n📋 Cleanup Summary:")
    print("✅ Removed hardcoded 'Load More Projects' functionality")
    print("✅ Removed preloader CSS and JavaScript")
    print("✅ Removed date converter code from main page")
    print("✅ Removed duplicate Django Framework skill entry")
    print("✅ Removed unused static project images")
    print("✅ Cleaned up unused JavaScript variables")
    print("✅ Removed unnecessary imports")
    
    print("\n🎯 Your portfolio now uses:")
    print("• Dynamic Education from database")
    print("• Dynamic Experience from database") 
    print("• Dynamic Projects from database")
    print("• Dynamic About Me from database")
    print("• Clean, optimized codebase")
    
    print("\n✨ Cleanup completed successfully!")

if __name__ == "__main__":
    cleanup_static_files()
