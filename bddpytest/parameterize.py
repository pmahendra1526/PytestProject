from pytest_bdd import scenario, given, when, then, scenarios,parsers
import pytest
from pathlib import Path


featureFileDir="myfeatures"
featureFile="parameterize.feature"
BASE_DIR=Path(__file__).resolve().parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
print(FEATURE_FILE)

scenarios(FEATURE_FILE)

@given("A set of 3 elements",target_fixture="my_set")
def set_create():
    my_set={"India","USA","UK"}
    print("Initial set:", my_set)
    return my_set

@when("Add same elements to set")
def add_elements(my_set):
    my_set.add("India")
    print("After adding elements:", my_set)

@then("The set should have 3 elements")
def check_set_size(my_set): 
    assert len(my_set) == 3
    print("Final set size is correct:", len(my_set))

@then("If we add different element")
def add_different_element(my_set):
    my_set.add("Germany")
    print("After adding different element:", my_set)
    assert len(my_set) == 4
    print("Final set size after adding different element is correct:", len(my_set))

@then(parsers.parse("The set should have {expected_size:d} elements"))
def check_set_size_param(my_set, expected_size):
    assert len(my_set) == expected_size
    print(f"Final set size is correct: {len(my_set)}")



@given(parsers.parse("There are {count:d} fruits"),target_fixture="existing_fruits")
def existing_fruits(count):
    return dict(start=count,eat=0)

@when(parsers.parse("I eat {eat_count:d} fruits"))
def eat_fruits(existing_fruits,eat_count):
    print("Existing fruits before eating:", existing_fruits)
    existing_fruits['eat'] += eat_count
    print("Fruits eaten:", existing_fruits)

@then(parsers.parse("I should have {remaining_count:d} fruits"))
def check_remaining_fruits(existing_fruits, remaining_count):
    remaining = existing_fruits['start'] - existing_fruits['eat']
    assert remaining == remaining_count
    print("Fruits left after eating:", remaining)
