from pytest_bdd import scenario, given, when, then, scenarios
import pytest
from pathlib import Path


featureFileDir="myfeatures"
featureFile="fixtures.feature"
BASE_DIR=Path(__file__).resolve().parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
print(FEATURE_FILE)

scenarios(FEATURE_FILE)

@pytest.fixture
def setup_set():
    print("In fixture setup function")
    # countries={"India","USA","UK"}
    # countries=set()
    countries={"India","USA","UK","Germany"}
    return countries

@given("A set of 3 elements")
def set_create(setup_set):
    if len(setup_set) == 0:
        pytest.xfail("Set is empty, cannot proceed with test")
    elif len(setup_set) > 3:
        while len(setup_set)>3:
            setup_set.pop()
    print("Initial set:", setup_set)
    return setup_set
    
@when("Add two elements to set")
def add_element(setup_set):
    setup_set.add("Australia")
    setup_set.add("America")
    print("After adding element:", setup_set)

@then("The set should have 5 elements")
def check_set_size(setup_set):
    assert len(setup_set) == 5
    print("Final set size is correct:", len(setup_set))