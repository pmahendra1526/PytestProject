from pytest_bdd import scenario, given, when, then
import pytest
from pathlib import Path


featureFileDir="myfeatures"
featureFile="first101.feature"
BASE_DIR=Path(__file__).resolve().parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
print(FEATURE_FILE)

def pytest_configure():
    pytest.AMT=0

@scenario(FEATURE_FILE,"Withdrawal of Money")
def test_withdrawal():
    print("End of Withdrawal Test")

@given("The account balance is 100")
def current_balance():
    pytest.AMT=100

@when("The account holder withdraw 30")
def withdraw_amount():
    pytest.AMT=pytest.AMT-30

@then("The account balance should be 70")
def final_balance():
    assert pytest.AMT==70

####################################################
@scenario(FEATURE_FILE,"Deposit Money")
def test_depsit():
    print("End of Deposit Test")

@given("The account balance is 100")
def current_balance():
    pytest.AMT=100

@when("The account holder deposit 50")
def deposit_amount():
    pytest.AMT=pytest.AMT+50

@then("The account balance should be 150")
def final_balance():
    assert pytest.AMT==150

####################################################
@scenario(FEATURE_FILE,"Removal of Items from set")
def test_removalOfItems():
    print("End of Deposit Test")

@given("A set of 3 fruits", target_fixture="myset")
def set_create():
    myset={"Appple","Banana","Goa"}
    return myset

@when("Remove a fruit from a set")
def remove_fruit(myset):
    myset.pop()
    print(myset)

@then("The set will have two fruits")
def final_set(myset):
    assert len(myset)==2

