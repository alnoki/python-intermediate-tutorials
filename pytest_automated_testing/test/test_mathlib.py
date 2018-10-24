"""Module for testing mathlib via pytest"""
# References https://www.youtube.com/watch?v=l32bsaIDoWk&index=2&t=0s&list=PLeo1K3hjS3utzQYDNRNluzqJqpMXx6hHu

import src.mathlib as mathlib
import pytest


# @pytest.mark.skipif(sys.version_info > (3, 5), reason="Python version")
# @pytest.mark.skip(reason="Not running for current test case")
def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == 9


def test_calc_multiply():
    result = mathlib.calc_multiply(10, 3)
    assert result == 30


def test_dummy():
    assert True


@pytest.mark.windows  # Marks the test with windows marker
def test_windows_1():
    assert True


@pytest.mark.windows  # Marks the test with windows marker
def test_windows_2():
    assert True


@pytest.mark.mac  # Marks the test with mac marker
def test_mac_1():
    assert True


@pytest.mark.mac  # Marks the test with mac marker
def test_mac_2():
    assert True
