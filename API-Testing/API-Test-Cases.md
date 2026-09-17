# API Testing Project

## Project Overview

This project demonstrates API testing using REST APIs. The objective is to validate API endpoints, HTTP methods, status codes, response data, and error handling.

## API Test Cases

### TC-API-001: Verify GET Request

**Test Scenario:** Verify that a GET request successfully retrieves user data.

**HTTP Method:** GET

**Expected Status Code:** 200 OK

**Test Steps:**
1. Open Postman.
2. Select the GET method.
3. Enter the API endpoint.
4. Click Send.
5. Verify the response.

**Expected Result:** The API should return a 200 OK status code and valid response data.

---

### TC-API-002: Verify POST Request

**Test Scenario:** Verify that a new user can be created using a POST request.

**HTTP Method:** POST

**Expected Status Code:** 201 Created

**Test Steps:**
1. Open Postman.
2. Select the POST method.
3. Enter the API endpoint.
4. Add valid JSON data in the request body.
5. Click Send.
6. Verify the response.

**Expected Result:** The API should successfully create the resource and return the appropriate success status code.

---

### TC-API-003: Verify Invalid API Endpoint

**Test Scenario:** Verify API behavior when an invalid endpoint is requested.

**HTTP Method:** GET

**Expected Status Code:** 404 Not Found

**Test Steps:**
1. Open Postman.
2. Select the GET method.
3. Enter an invalid API endpoint.
4. Click Send.
5. Verify the response status code.

**Expected Result:** The API should return an appropriate error response such as 404 Not Found.