# Python Testing Practice
# Demonstrates basic Python concepts used in QA and test automation


# Variables
test_name = "Login Test"
expected_status = 200
actual_status = 200


# Strings
browser = "Chrome"
environment = "QA"

print(f"Running {test_name}")
print(f"Browser: {browser}")
print(f"Environment: {environment}")


# If / Else
if actual_status == expected_status:
    print("Test Passed")
else:
    print("Test Failed")


# List
test_cases = [
    "Login with valid credentials",
    "Login with invalid password",
    "Login with invalid email"
]

print("\nTest Cases:")

# For Loop
for test_case in test_cases:
    print(test_case)


# Dictionary
test_result = {
    "test_name": "Login Test",
    "expected_status": 200,
    "actual_status": 200,
    "result": "Passed"
}

print("\nTest Result:")
print(test_result)


# Function
def verify_status(expected, actual):
    if expected == actual:
        return "Passed"
    else:
        return "Failed"


result = verify_status(200, 200)

print(f"\nAPI Test Result: {result}")


# Exception Handling
try:
    response_code = int("200")
    print(f"Response Code: {response_code}")
except ValueError:
    print("Invalid response code")