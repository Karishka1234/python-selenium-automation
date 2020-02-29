# Created by HP at 2/22/2020
Feature: count historic books

  Scenario: a test case that count historic books
    Given Open amazon page
    When Send history book
    And Count how many books would be shown in result list
    Then If last book has Best Seller label, will add it in the cart
    #1.4* If first book has price higher 10$, will add it in the cart (go to page of book)
