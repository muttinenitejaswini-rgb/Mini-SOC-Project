
# Brute-Force Login Detection Rule

## Rule Name
Repeated Failed Login Detection

## Objective
Identify repeated failed login attempts that may indicate a brute-force attack.

## Log Source
Sample authentication logs stored in logs/sample_auth.log.

## Detection Logic
- Identify failed login events.
- Group events by username and source IP address.
- Count failed attempts for each username and IP combination.
- Generate an alert when the count reaches 3 or more.

## Test Case
Username: admin
Source IP: 192.168.1.25
Failed login attempts: 3

Expected Result: Alert generated for possible brute-force activity.

## Recommended Investigation
1. Review the failed login timestamps.
2. Identify the targeted account and source IP.
3. Check whether a successful login followed the failures.
4. Investigate the source before deciding on a response.

## Current Status
Tested with fictional sample logs using a custom Python script.

Note: This is a documented custom detection rule, not yet a deployed Wazuh rule.
