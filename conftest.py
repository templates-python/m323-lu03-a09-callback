import sys
from unittest.mock import MagicMock

# Mock the tkinter module so that it can be imported even if it's not installed
sys.modules['tkinter'] = MagicMock()
