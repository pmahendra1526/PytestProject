from pytest_bdd import scenario, given, when, then, scenarios,parsers
import pytest
from pathlib import Path


featureFileDir="myfeatures"
featureFile="outline.feature"
BASE_DIR=Path(__file__).resolve().parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
print(FEATURE_FILE)


@scenario(FEATURE_FILE, "Scenario Outline Test")
def test_outline():
    pass

@given(parsers.parse('There are {initial_fruits:d} fruits'),target_fixture='fruits')
def given_fruits(initial_fruits):
    return dict(start=initial_fruits)

@when(parsers.parse('I buy {fruits_bought:d} fruits'))
def when_buy_fruits(fruits, fruits_bought):
    fruits['bought'] = fruits_bought
    print("In when: ", fruits)

@then(parsers.parse('I should have {total_fruits:d} fruits'))
def then_total_fruits(fruits, total_fruits):
    total= fruits['start'] + fruits['bought']
    assert total == total_fruits