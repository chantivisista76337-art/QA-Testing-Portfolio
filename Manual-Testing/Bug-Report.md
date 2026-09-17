# Bug Report - Login Functionality

## Bug ID: BUG-001

**Title:** User is not shown an error message after entering an invalid password

**Module:** Login

**Environment:**
- Application: Sample Web Application
- Browser: Google Chrome
- Operating System: Windows 11

**Precondition:**
- User has a registered account.
- Login page is accessible.

## Steps to Reproduce

1. Open the application login page.
2. Enter a valid registered email address.
3. Enter an invalid password.
4. Click the Login button.

## Test Data

- Email: validuser@test.com
- Password: Wrong@123

## Expected Result

The user should not be logged in, and an appropriate error message such as
"Invalid email or password" should be displayed.

## Actual Result

The user is not logged in, but no error message is displayed.

## Severity

**Medium**

## Priority

**High**

## Status

**Open**

## Reproducibility

**Always**

## Attachment / Evidence

Screenshot or screen recording can be attached when reproducing the defect.

---

## Notes

This is a sample defect report created to demonstrate bug reporting and
defect documentation skills as part of a QA testing portfolio.