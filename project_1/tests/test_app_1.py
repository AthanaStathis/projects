import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app_1 import add


def test_add_passes():
    """This test passes: 2 + 3 equals 5."""
    assert add(2, 3) == 5


def test_add_fails():
    """This test fails intentionally: 2 + 3 does not equal 99."""
    assert add(2, 3) == 99
