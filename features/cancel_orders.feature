# Created by Karina at 10/12/19
Feature: Test Scenarios for canceling orders functionality

  Scenario: User can search for a canceling order page
    Given Open help page on amazon web site
    When Input Cancel Orders into go field
    And Click on go icon
    Then Results for Cancel Items or Orders are shown
    And Results contains Cancel Items or Orders