"""
tests/test_reflection.py
"""

from physics.reflection import reflection_coefficient


def test_reflection_zero():
    r = reflection_coefficient(4, 4)
    assert abs(r) < 1e-6
