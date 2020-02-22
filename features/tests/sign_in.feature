# Created by HP at 11/4/2019
Feature: Sign in page

  Scenario: Logged out user sees Sign in page when clicking Orders
  Given Open Amazon page
  When Click Amazon Orders link
  Then Verify Sign-In page is opened