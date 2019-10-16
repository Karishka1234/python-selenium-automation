# Created by Karina at 10/14/2019
Feature: Test scenarios for shopping cart
  # Enter feature description here

  Scenario:  Adding a product in shopping cart
   Given Open Amazon page
    When Input Learning toys for 9 month old baby in to search field
    And Click on search button
    And Find toys
    Then Add toys to a shopping cart
    And Close side window
    And Click to shopping cart
    And Verify that 2 items are there