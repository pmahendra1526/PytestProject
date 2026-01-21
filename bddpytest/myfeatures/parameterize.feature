
Feature: Parameterized Tests
    Tests pertaining to parameterized scenarios

    Scenario: Adding items to a set
        Given A set of 3 elements
        When Add same elements to set
        Then The set should have 3 elements
        But If we add different element
        Then The set should have 4 elements
        Examples:
            | initial_size | elements_to_add | final_size |
            | 3            | 1               | 4          |
            | 3            | 0               | 3          |

    Scenario: Benefits of Parameterrization
        Given There are 5 fruits
        When I eat 3 fruits
        And I eat 2 fruits
        Then I should have 0 fruits
        Examples:
            | initial_fruits | fruits_eaten1 | fruits_eaten2 | remaining_fruits |
            | 5              | 3             | 2             | 0                 |


    