"""
Accurate Nepali Date Converter
Converts between Nepali BS (Bikram Sambat) and English AD (Anno Domini) dates
"""

import datetime

class NepaliDateConverter:
    def __init__(self):
        # Accurate Nepali calendar data with days in each month for different years
        # This data is based on official Nepali calendar
        self.nepali_months_data = {
            2000: [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2001: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2002: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2003: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2004: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2005: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2006: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2007: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2008: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2009: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2010: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2011: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2012: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2013: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2014: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2015: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2016: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2017: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2018: [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2019: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2020: [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
            2021: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2022: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 30],
            2023: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2024: [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
            2025: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2026: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 30],
            2027: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2028: [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
            2029: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2030: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 30],
            2031: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2032: [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
            2033: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2034: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 30],
            2035: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2036: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2037: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2038: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2039: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2040: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2041: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2042: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2043: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2044: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2045: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2046: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2047: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2048: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2049: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2050: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2051: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2052: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2053: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2054: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2055: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2056: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2057: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2058: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2059: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2060: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2061: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2062: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2063: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2064: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2065: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2066: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2067: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2068: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2069: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2070: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2071: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2072: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2073: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2074: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2075: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2076: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2077: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2078: [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
            2079: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2080: [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
            2081: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2082: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 30],
            2083: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2084: [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
            2085: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2086: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 30],
            2087: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
            2088: [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
            2089: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
            2090: [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 30],
        }
        
        # Base reference dates
        self.base_ad_date = datetime.date(1943, 4, 14)  # 1943-04-14 AD
        self.base_bs_year = 2000
        self.base_bs_month = 1
        self.base_bs_day = 1
        
    def get_days_in_nepali_month(self, year, month):
        """Get number of days in a specific Nepali month and year"""
        if year in self.nepali_months_data:
            return self.nepali_months_data[year][month - 1]
        else:
            # Default approximation for years not in data
            default_days = [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30]
            return default_days[month - 1]
    
    def count_total_days_from_base_bs(self, year, month, day):
        """Count total days from base BS date to given BS date"""
        total_days = 0
        
        # Add days for complete years
        for y in range(self.base_bs_year, year):
            for m in range(1, 13):
                total_days += self.get_days_in_nepali_month(y, m)
        
        # Add days for complete months in the target year
        for m in range(1, month):
            total_days += self.get_days_in_nepali_month(year, m)
        
        # Add remaining days
        total_days += (day - self.base_bs_day)
        
        return total_days
    
    def bs_to_ad(self, bs_year, bs_month, bs_day):
        """Convert Nepali BS date to English AD date"""
        try:
            # Calculate total days from base BS date
            total_days = self.count_total_days_from_base_bs(bs_year, bs_month, bs_day)
            
            # Add to base AD date
            ad_date = self.base_ad_date + datetime.timedelta(days=total_days)
            
            return ad_date.strftime('%Y-%m-%d')
        except Exception as e:
            raise ValueError(f"Error converting BS to AD: {str(e)}")
    
    def ad_to_bs(self, ad_year, ad_month, ad_day):
        """Convert English AD date to Nepali BS date"""
        try:
            ad_date = datetime.date(ad_year, ad_month, ad_day)
            
            # Calculate days difference from base AD date
            days_diff = (ad_date - self.base_ad_date).days
            
            # Start from base BS date
            bs_year = self.base_bs_year
            bs_month = self.base_bs_month
            bs_day = self.base_bs_day
            
            # Add the days difference
            remaining_days = days_diff
            
            # Handle negative days (dates before base date)
            if remaining_days < 0:
                raise ValueError("Date is before the supported range")
            
            # Add days by iterating through years and months
            while remaining_days > 0:
                days_in_current_month = self.get_days_in_nepali_month(bs_year, bs_month)
                days_left_in_month = days_in_current_month - bs_day + 1
                
                if remaining_days >= days_left_in_month:
                    # Move to next month
                    remaining_days -= days_left_in_month
                    bs_month += 1
                    bs_day = 1
                    
                    if bs_month > 12:
                        bs_month = 1
                        bs_year += 1
                else:
                    # Add remaining days to current month
                    bs_day += remaining_days
                    remaining_days = 0
            
            return f"{bs_year}-{bs_month:02d}-{bs_day:02d}"
        except Exception as e:
            raise ValueError(f"Error converting AD to BS: {str(e)}")
    
    def convert_date(self, date_str, conversion_type):
        """Main conversion function"""
        try:
            if conversion_type == 'bs_to_ad':
                year, month, day = map(int, date_str.split('-'))
                return self.bs_to_ad(year, month, day)
            elif conversion_type == 'ad_to_bs':
                year, month, day = map(int, date_str.split('-'))
                return self.ad_to_bs(year, month, day)
            else:
                raise ValueError("Invalid conversion type")
        except ValueError as e:
            raise e
        except Exception as e:
            raise ValueError(f"Invalid date format. Please use YYYY-MM-DD format. Error: {str(e)}")
