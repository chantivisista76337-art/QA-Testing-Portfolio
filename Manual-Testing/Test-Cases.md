# Manual Testing - Login Functionality

## Project Overview

This project demonstrates manual testing of a web application's login functionality. 
The objective is to validate successful login, invalid credentials, required fields, 
and basic input validation using positive and negative test scenarios.

## Test Cases

### TC-001: Verify Login with Valid Credentials

**Test Scenario:** Verify that a registered user can log in with valid credentials.

**Precondition:** User has a valid registered account.

**Test Steps:**
1. Open the login page.
2. Enter a valid email address.
3. Enter a valid password.
4. Click the Login button.

**Test Data:**
- Email: validuser@test.com
- Password: Test@123

**Expected Result:** User should successfully log in and be redirected to the application home page.

**Priority:** High

---

### TC-002: Verify Login with Invalid Password

**Test Scenario:** Verify login behavior when the user enters an invalid password.

**Precondition:** User has a registered account.

**Test Steps:**
1. Open the login page.
2. Enter a valid email address.
3. Enter an invalid password.
4. Click the Login button.

**Test Data:**
- Email: validuser@test.com
- Password: Wrong@123

**Expected Result:** Login should fail and an appropriate error message should be displayed.

**Priority:** High

---

### TC-003: Verify Login with Empty Email

**Test Scenario:** Verify validation when the email field is left empty.

**Test Steps:**
1. Open the login page.
2. Leave the email field empty.
3. Enter a valid password.
4. Click the Login button.

**Expected Result:** User should not be logged in and a validation message should be displayed for the email field.

**Priority:** High

---

### TC-004: Verify Login with Empty Password

**Test Scenario:** Verify validation when the password field is left empty.

**Test Steps:**
1. Open the login page.
2. Enter a valid email address.
3. Leave the password field empty.
4. Click the Login button.

**Expected Result:** User should not be logged in and a validation message should be displayed for the password field.

**Priority:** High

---

### TC-005: Verify Login with Invalid Email Format

**Test Scenario:** Verify validation when an incorrectly formatted email address is entered.

**Test Steps:**
1. Open the login page.
2. Enter an invalid email format.
3. Enter a password.
4. Click the Login button.

**Test Data:**
- Email: usertest.com
- Password: Test@123

**Expected Result:** User should not be logged in and an appropriate email-format validation message should be displayed.

**Priority:** Medium