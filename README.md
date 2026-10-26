# Mini SOC - Security Monitoring and Threat Detection

## Project Overview

This project is a beginner-friendly Security Operations Center (SOC) prototype built using Python. It analyzes sample authentication logs, detects repeated failed login attempts, assigns alert severity, and generates a security alert report.

## Objectives

- Analyze authentication log entries.
- Detect possible brute-force login activity.
- Identify the username and source IP address involved.
- Assign MEDIUM or HIGH severity based on failed login counts.
- Generate a readable security alert report.

## Tools Used

- Python 3
- Visual Studio Code
- Sample authentication logs
- Windows
- Git and GitHub

## Detection Rules

### Rule 1: Repeated Failed Login Detection
- Groups failed login attempts by username and source IP address.
- Generates an alert after 3 or more failed attempts.
- Assigns MEDIUM severity for 3–4 attempts.
- Assigns HIGH severity for 5 or more attempts.

### Rule 2: Multiple Source IP Login Detection
- Groups failed login events by username.
- Identifies usernames associated with 3 or more distinct source IP addresses.
- Generates a MEDIUM severity alert when the threshold is reached.

## Test Results

The analyzer was tested using fictional authentication logs.

- Five failed login attempts for `admin` from `192.168.1.25` generated a HIGH brute-force alert.
- Failed login attempts for `student` from 3 distinct source IP addresses generated a MEDIUM multi-IP alert.
- Both alerts were written to `reports/alerts.txt`.

## Limitations

This is a local Python-based prototype that analyzes sample logs. It does not currently monitor live systems or deploy detection rules inside Wazuh.

## Screenshots

### Terminal Output

<img src="https://raw.githubusercontent.com/muttinenitejaswini-rgb/Mini-SOC-Project/main/screenshots/mini-soc-terminal-output.png" alt="Mini SOC Terminal Output" width="700">

### Security Alert Report

<img src="https://raw.githubusercontent.com/muttinenitejaswini-rgb/Mini-SOC-Project/main/screenshots/mini-soc-alert-report.png" alt="Mini SOC Security Alert Report" width="700">

## Limitations

This is a local Python-based prototype that analyzes sample logs. It does not currently monitor live systems or deploy detection rules inside Wazuh.

## Future Improvements

- Integrate with Wazuh for security event monitoring.
- Analyze real authentication logs in a controlled lab.
- Add additional detection rules.
- Improve alert investigation and reporting.

## Author

Cybersecurity Learning Project