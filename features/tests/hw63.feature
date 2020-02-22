# Created by HP at 2/22/2020
Feature: HW 6 3

  Scenario: Hw 6 3 test
    Given Open web page
    When Search for stainless work table
    Then Check the search result ensuring every product item has the word Table its title
    And Add the last of found items to Cart.
    And Empty Cart.
