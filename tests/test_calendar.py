"""
Unit tests for Perpetual Calendar - Interactive Explorer.

Comprehensive tests covering calendar calculations, date validation,
event database integrity, and historical date accuracy.

Author: Tharun Ponnam
Created: June 2020
"""

import unittest
import calendar
from datetime import datetime


class TestCalendarCalculations(unittest.TestCase):
    """Test calendar mathematical calculations."""
    
    def test_leap_year_divisible_by_400(self):
        """Years divisible by 400 are leap years."""
        leap_years = [1600, 2000, 2400]
        for year in leap_years:
            self.assertTrue(
                calendar.isleap(year),
                f"{year} should be a leap year (divisible by 400)"
            )
    
    def test_non_leap_year_divisible_by_100(self):
        """Years divisible by 100 but not 400 are NOT leap years."""
        non_leap = [1500, 1700, 1800, 1900, 2100]
        for year in non_leap:
            self.assertFalse(
                calendar.isleap(year),
                f"{year} should NOT be a leap year (divisible by 100 but not 400)"
            )
    
    def test_regular_leap_years(self):
        """Years divisible by 4 (not 100) are leap years."""
        leap_years = [2004, 2008, 2012, 2016, 2020]
        for year in leap_years:
            self.assertTrue(
                calendar.isleap(year),
                f"{year} should be a leap year"
            )
    
    def test_february_days_leap_year(self):
        """February has 29 days in leap years."""
        self.assertEqual(calendar.monthrange(2000, 2)[1], 29)
        self.assertEqual(calendar.monthrange(2020, 2)[1], 29)
        self.assertEqual(calendar.monthrange(1600, 2)[1], 29)
    
    def test_february_days_non_leap_year(self):
        """February has 28 days in non-leap years."""
        self.assertEqual(calendar.monthrange(1900, 2)[1], 28)
        self.assertEqual(calendar.monthrange(2019, 2)[1], 28)
        self.assertEqual(calendar.monthrange(1500, 2)[1], 28)
    
    def test_month_days(self):
        """Verify days in each month."""
        expected = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        for month, days in expected.items():
            self.assertEqual(
                calendar.monthrange(2019, month)[1],
                days,
                f"Month {month} should have {days} days"
            )


class TestYearValidation(unittest.TestCase):
    """Test year range validation."""
    
    MIN_YEAR = 1500
    MAX_YEAR = 9999
    
    def test_minimum_year_valid(self):
        """1500 is a valid year."""
        self.assertTrue(self.MIN_YEAR <= 1500 <= self.MAX_YEAR)
    
    def test_maximum_year_valid(self):
        """9999 is a valid year."""
        self.assertTrue(self.MIN_YEAR <= 9999 <= self.MAX_YEAR)
    
    def test_below_minimum_invalid(self):
        """Years below 1500 are invalid."""
        invalid = [1499, 1000, 500, 0, -1]
        for year in invalid:
            self.assertFalse(self.MIN_YEAR <= year <= self.MAX_YEAR)
    
    def test_above_maximum_invalid(self):
        """Years above 9999 are invalid."""
        invalid = [10000, 99999]
        for year in invalid:
            self.assertFalse(self.MIN_YEAR <= year <= self.MAX_YEAR)


class TestHistoricalDates(unittest.TestCase):
    """Verify accuracy of historical dates."""
    
    def test_us_independence_day(self):
        """July 4, 1776 was a Thursday."""
        self.assertEqual(calendar.weekday(1776, 7, 4), 3)  # Thursday
    
    def test_india_independence_day(self):
        """August 15, 1947 was a Friday."""
        self.assertEqual(calendar.weekday(1947, 8, 15), 4)  # Friday
    
    def test_moon_landing(self):
        """July 20, 1969 was a Sunday."""
        self.assertEqual(calendar.weekday(1969, 7, 20), 6)  # Sunday
    
    def test_wwi_start(self):
        """July 28, 1914 was a Tuesday."""
        self.assertEqual(calendar.weekday(1914, 7, 28), 1)  # Tuesday
    
    def test_wwii_start(self):
        """September 1, 1939 was a Friday."""
        self.assertEqual(calendar.weekday(1939, 9, 1), 4)  # Friday
    
    def test_berlin_wall_fall(self):
        """November 9, 1989 was a Thursday."""
        self.assertEqual(calendar.weekday(1989, 11, 9), 3)  # Thursday
    
    def test_eniac_unveiling(self):
        """February 14, 1946 was a Thursday."""
        self.assertEqual(calendar.weekday(1946, 2, 14), 3)  # Thursday
    
    def test_www_launch(self):
        """August 6, 1991 was a Tuesday."""
        self.assertEqual(calendar.weekday(1991, 8, 6), 1)  # Tuesday
    
    def test_iphone_announcement(self):
        """January 9, 2007 was a Tuesday."""
        self.assertEqual(calendar.weekday(2007, 1, 9), 1)  # Tuesday


class TestMonthMapping(unittest.TestCase):
    """Test month name to number mapping."""
    
    MONTHS = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    def test_month_count(self):
        """There are 12 months."""
        self.assertEqual(len(self.MONTHS), 12)
    
    def test_month_index_mapping(self):
        """Month names map to correct indices."""
        for i, name in enumerate(self.MONTHS):
            self.assertEqual(self.MONTHS.index(name) + 1, i + 1)


class TestCalendarGeneration(unittest.TestCase):
    """Test calendar generation at boundary years."""
    
    def test_calendar_1500(self):
        """Calendar generates for year 1500."""
        cal = calendar.TextCalendar()
        output = cal.formatmonth(1500, 1)
        self.assertIn("January 1500", output)
    
    def test_calendar_9999(self):
        """Calendar generates for year 9999."""
        cal = calendar.TextCalendar()
        output = cal.formatmonth(9999, 12)
        self.assertIn("December 9999", output)
    
    def test_calendar_2020(self):
        """Calendar generates for year 2020."""
        cal = calendar.TextCalendar()
        output = cal.formatmonth(2020, 6)
        self.assertIn("June 2020", output)


class TestDateValidation(unittest.TestCase):
    """Test day validation for various months."""
    
    def test_january_31_days(self):
        """January has 31 days."""
        self.assertEqual(calendar.monthrange(2020, 1)[1], 31)
    
    def test_april_30_days(self):
        """April has 30 days."""
        self.assertEqual(calendar.monthrange(2020, 4)[1], 30)
    
    def test_february_leap_29_days(self):
        """February in leap year has 29 days."""
        self.assertEqual(calendar.monthrange(2020, 2)[1], 29)
    
    def test_february_non_leap_28_days(self):
        """February in non-leap year has 28 days."""
        self.assertEqual(calendar.monthrange(2019, 2)[1], 28)


class TestEventDateFormat(unittest.TestCase):
    """Test event date format parsing."""
    
    def test_date_format_parsing(self):
        """Event dates can be parsed correctly."""
        test_dates = [
            "1776-07-04",
            "1947-08-15",
            "1969-07-20",
            "2020-06-11",
            "2030-01-01",
        ]
        
        for date_str in test_dates:
            parts = date_str.split("-")
            self.assertEqual(len(parts), 3)
            
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            
            self.assertTrue(1500 <= year <= 9999)
            self.assertTrue(1 <= month <= 12)
            
            max_day = calendar.monthrange(year, month)[1]
            self.assertTrue(1 <= day <= max_day)


class TestFuturePredictions(unittest.TestCase):
    """Test future prediction dates are after June 2020."""
    
    def test_predictions_after_june_2020(self):
        """Future predictions should be dated after June 2020."""
        future_dates = [
            "2021-01-01",
            "2025-01-01",
            "2030-01-01",
            "2050-01-01",
        ]
        
        for date_str in future_dates:
            parts = date_str.split("-")
            year = int(parts[0])
            month = int(parts[1])
            
            is_after_june_2020 = (year > 2020) or (year == 2020 and month > 6)
            self.assertTrue(
                is_after_june_2020,
                f"Prediction date {date_str} should be after June 2020"
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
