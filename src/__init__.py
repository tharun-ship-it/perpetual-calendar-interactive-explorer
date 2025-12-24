"""
Perpetual Calendar - Interactive Explorer

A comprehensive, interactive Python GUI calendar application featuring:
- Date range from 1500 to 9999
- Date highlighting with visual markers
- Historical events database (Past, Present, Future predictions)
- Interactive user experience with guided exploration
- Educational content across multiple eras

Author: Tharun Ponnam
Created: June 2020
"""

from .calendar_app import PerpetualCalendar, EventsDatabase

__version__ = "2.0.0"
__author__ = "Tharun Ponnam"
__email__ = "tharunponnam007@gmail.com"
__all__ = ["PerpetualCalendar", "EventsDatabase"]
