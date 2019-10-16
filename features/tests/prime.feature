# Created by HP at 10/15/2019
Feature: Test scenarios for amazon prime
  # Enter feature description here

  Scenario: # Amazon Prime page has 8 boxes
    Given Open Amazon web site
    When Click on TryPrime icon
    Then Verify that page has 8 boxes