"""
    Adds "poetry_template" to sys.path.

    Now you can do imports with "from poetry_template.Sub-Package ...".
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
