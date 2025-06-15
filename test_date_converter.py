#!/usr/bin/env python3
"""
Test script for Nepali Date Converter
"""

import sys
import os

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main.nepali_date_converter import NepaliDateConverter

def test_converter():
    converter = NepaliDateConverter()
    
    print("=== Nepali Date Converter Test ===\n")
    
    # Test the specific example: 2059-06-09 BS should convert to 2002-09-25 AD
    print("Test 1: BS to AD Conversion")
    print("Input: 2059-06-09 (BS)")
    try:
        result = converter.bs_to_ad(2059, 6, 9)
        print(f"Output: {result} (AD)")
        if result == "2002-09-25":
            print("✅ PASS: Correct conversion!")
        else:
            print("❌ FAIL: Expected 2002-09-25")
    except Exception as e:
        print(f"❌ ERROR: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test reverse conversion: 2002-09-25 AD should convert to 2059-06-09 BS
    print("Test 2: AD to BS Conversion")
    print("Input: 2002-09-25 (AD)")
    try:
        result = converter.ad_to_bs(2002, 9, 25)
        print(f"Output: {result} (BS)")
        if result == "2059-06-09":
            print("✅ PASS: Correct reverse conversion!")
        else:
            print("❌ FAIL: Expected 2059-06-09")
    except Exception as e:
        print(f"❌ ERROR: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test a few more known conversions
    test_cases = [
        # (BS_year, BS_month, BS_day, expected_AD)
        (2000, 1, 1, "1943-04-14"),  # Base reference date
        (2080, 1, 1, "2023-04-14"),  # New Year 2080 BS
        (2081, 1, 1, "2024-04-13"),  # New Year 2081 BS
    ]
    
    print("Test 3: Additional Test Cases")
    for i, (bs_y, bs_m, bs_d, expected_ad) in enumerate(test_cases, 1):
        print(f"\nTest 3.{i}: {bs_y}-{bs_m:02d}-{bs_d:02d} (BS)")
        try:
            result = converter.bs_to_ad(bs_y, bs_m, bs_d)
            print(f"Result: {result} (AD)")
            print(f"Expected: {expected_ad} (AD)")
            if result == expected_ad:
                print("✅ PASS")
            else:
                print("❌ FAIL")
        except Exception as e:
            print(f"❌ ERROR: {e}")
    
    print("\n" + "="*50 + "\n")
    print("Test completed!")

if __name__ == "__main__":
    test_converter()
