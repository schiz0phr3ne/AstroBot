"""
This module provides the necessary context for running tests for the AstroBot project.

It adds the project directory to the sys.path, allowing the tests to import the required modules.

Usage:
    import context

"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import astrobot
