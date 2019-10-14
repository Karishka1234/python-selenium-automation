"""XPATH
1. amazon logo field, search by class "a-icon a-icon-logo"
2. email field, search by ID, “ap_email”
3. Continue button, search by id='continue', by class 'a-button-input'
4. Need help link, search by class 'a-expander-prompt'
5. Forgot your password link, search by id 'auth-fpp-link-bottom'
6. Other issues with Sign-In link, search by id 'ap-other-signin-issues-link'
7. Create your Amazon account button, search by id 'createAccountSubmit', also by class 'a-button-text', by role 'button'
8. Conditions of ise field, search by text "//a[contains(@href, 'condition_of_use')]")


CSS SELECTORS
1. amazon logo field, search by class "a-icon-logo"
2. create account field, search by class "h1.a-spacing-small")
3. Your name field, search by id "input#ap_customer_name"
4. Email field, search by type "input[type='email'"
5. Password field, search by type "input[type='password'"
6. need help with "Passwords must be at least 6 characters." ("div[text*='Passwords must be']",  ("div[class*='Passwords must be']",  ($x("//div[contains(@text(), 'Password must be')]"), $x("//div[contains(@class, 'Password must be')]"), $x("//div[@class='a-alert-content']")
7. re-enter password field, search by id "input#ap_password_check"
8. Create amazon account field, search by class "input.a-button-input"
9. Conditions of ise field, search by href "a[href*='condition_of_use']")
10. Privacy notice field, search by href "a[href*='privacy_notice']")
11. Sign in field, search by class "a.a-link-emphasis"



"""