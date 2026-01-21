Feature: Scenario outline

    Scenario Outline: Scenario Outline Test
        Given There are <initial_fruits> fruits
        When I buy <fruits_bought> fruits
        Then I should have <total_fruits> fruits

        Examples:
            | initial_fruits | fruits_bought | total_fruits |
            | 10             | 5             | 15           |
            | 20             | 10            | 20           |
            | 0              | 7             | 7            |