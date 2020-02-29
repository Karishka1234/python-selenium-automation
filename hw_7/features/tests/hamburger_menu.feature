# Created by HP at 11/10/2019
Feature: Hamburger menu functionality

  Scenario: Amazon Music has 6 menu items
 Given Open Amazon page
 When Click on hamburger menu
 And Click on Amazon Music menu item
 Then 6 menu items are present