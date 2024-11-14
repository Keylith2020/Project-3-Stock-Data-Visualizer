import unittest
from datetime import datetime
import re
from app import symbols

class TestInputConstraints(unittest.TestCase):
    
    # Test symbol: capitalized, 1-7 alpha characters
    def test_symbol(self):
        def is_valid_symbol(symbol):
            return bool(re.match(r'^[A-Z]{1,7}$', symbol))
        
        # Valid symbols
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertTrue(is_valid_symbol("GOOGL"))
        self.assertTrue(is_valid_symbol("TSLA"))
        
        # Invalid symbols
        self.assertFalse(is_valid_symbol("aapl"))
        self.assertFalse(is_valid_symbol("APPLE123"))
        self.assertFalse(is_valid_symbol("TOOLONGSYM"))

    # Test chart type: 1 numeric character, must be 1 or 2
    def test_chart_type(self):
        def is_valid_chart_type(chart_type):
            return chart_type in {"1", "2"}
        
        # Valid chart types
        self.assertTrue(is_valid_chart_type("1"))
        self.assertTrue(is_valid_chart_type("2"))
        
        # Invalid chart types
        self.assertFalse(is_valid_chart_type("3"))
        self.assertFalse(is_valid_chart_type("A"))
        self.assertFalse(is_valid_chart_type("12"))

    # Test time series: 1 numeric character, 1 - 4
    def test_time_series(self):
        def is_valid_time_series(time_series):
            return time_series in {"1", "2", "3", "4"}
        
        # Valid time series
        self.assertTrue(is_valid_time_series("1"))
        self.assertTrue(is_valid_time_series("2"))
        self.assertTrue(is_valid_time_series("3"))
        self.assertTrue(is_valid_time_series("4"))
        
        # Invalid time series
        self.assertFalse(is_valid_time_series("0"))
        self.assertFalse(is_valid_time_series("5"))
        self.assertFalse(is_valid_time_series("10"))

    # 4. Test start date: date type YYYY-MM-DD
    def test_start_date(self):
        def is_valid_date(date_text):
            try:
                datetime.strptime(date_text, "%Y-%m-%d")
                return True
            except ValueError:
                return False
        
        # Valid start dates
        self.assertTrue(is_valid_date("2023-01-01"))
        self.assertTrue(is_valid_date("2020-12-31"))
        
        # Invalid start dates
        self.assertFalse(is_valid_date("01-01-2023"))
        self.assertFalse(is_valid_date("2023/01/01"))
        self.assertFalse(is_valid_date("2023-13-01"))

    # Test end date: date type YYYY-MM-DD
    def test_end_date(self):
        def is_valid_date(date_text):
            try:
                datetime.strptime(date_text, "%Y-%m-%d")
                return True
            except ValueError:
                return False
        
        # Valid end dates
        self.assertTrue(is_valid_date("2023-12-31"))
        self.assertTrue(is_valid_date("2024-02-29"))    # leap year
        
        # Invalid end dates
        self.assertFalse(is_valid_date("2023-02-30"))   # invalid day
        self.assertFalse(is_valid_date("31-12-2023"))   # incorrect format
        self.assertFalse(is_valid_date("2023-01"))      # incomplete date

if __name__ == "__main__":
    unittest.main()