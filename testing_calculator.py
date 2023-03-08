import pytest

from currency import Ils, Usd, EUR

# Create instances of the currency converter classes
ils = Ils()
usd = Usd()
eur = EUR()


def test_ils_conversion():
    # Test converting 10 USD to ILS
    input_value = 10
    expected_result = 35.2
    result = ils.calculate(input_value)
    assert result == expected_result


def test_usd_conversion():
    # Test converting 10 ILS to USD
    input_value = 10
    expected_result = 2.8000000000000003
    result = usd.calculate(input_value)
    assert result == expected_result


def test_eur_conversion():
    # Test converting 10 ILS to EUR
    input_value = 10
    expected_result = 2.3640661938534278
    result = eur.calculate(input_value)
    assert result == expected_result


def test_results_file():
    # Test checking the content of the results file
    with open('/Users/natan/Desktop/python_tests/results.txt', 'r') as f:
        result = f.read()
    assert 'USD to ILS' in result
    assert 'ILS to USD' in result
    assert 'ILS to EUR' in result
