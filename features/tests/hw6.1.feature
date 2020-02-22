# Created by HP at 10/28/2019
Feature: Today's deals under 25

  Scenario: User can open and close pages, cart items would be saved in memory
  #Scenario: Adding an item from Today's deals under $25 to shopping cart
    Given Open Amazon page
    When Store original windows
    And Open a link in new window
    # And Click to open Deals under 25
    And Switch to the newly opened window
    # Today's Deals is shown
    Then Add any product into a cart
    And User can close new window and switch back to original
    And Refresh the page
    And Verify cart has 1 item




