import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app_2 import multiply


def test_multiply_passes():
    """This test passes: 3 * 4 equals 12."""
    assert multiply(3, 4) == 12


def test_multiply_fails():
    """This test fails intentionally: 3 * 4 does not equal 99."""
    assert multiply(3, 4) == 99
