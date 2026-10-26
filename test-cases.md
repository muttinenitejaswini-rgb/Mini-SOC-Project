# Mini SOC - Test Cases

## Test Case 1: Medium Severity Brute-Force Alert

- **Objective:** Verify detection of repeated failed login attempts.
- **Input:** 3 failed login attempts for `admin` from `192.168.1.25`.
- **Expected Result:** A MEDIUM severity alert should be generated.
- **Status:** Passed, if the output matches the expected result.

## Test Case 2: High Severity Brute-Force Alert

- **Objective:** Verify detection of a higher number of failed login attempts.
- **Input:** 5 failed login attempts for `admin` from `192.168.1.25`.
- **Expected Result:** A HIGH severity alert should be generated.
- **Status:** Passed, if the output matches the expected result.

## Test Case 3: Multiple Source IP Detection

- **Objective:** Identify failed login attempts for the same username from multiple IP addresses.
- **Input:** Failed login attempts for `student` from 3 distinct source IP addresses.
- **Expected Result:** A MEDIUM severity alert should be generated.
- **Status:** Passed, if the output matches the expected result.

## Test Case 4: Below Detection Threshold

- **Objective:** Verify that fewer than 3 failed attempts do not trigger a brute-force alert.
- **Input:** 2 failed login attempts for one username from one source IP.
- **Expected Result:** No brute-force alert should be generated for that username and IP.
- **Status:** Pending verification.
