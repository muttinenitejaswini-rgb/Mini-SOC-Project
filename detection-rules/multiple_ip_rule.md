# Multiple Source IP Login Detection

## Objective
Detect possible suspicious authentication activity when the same username has failed login attempts from multiple source IP addresses.

## Detection Logic
- Parse failed authentication log entries.
- Group failed attempts by username.
- Count distinct source IP addresses for each username.
- Generate a MEDIUM alert when the same username has failed login attempts from 3 or more distinct IP addresses.

## Test Results
- Tested using fictional sample authentication logs.
- The username `student` had failed login attempts from 3 distinct IP addresses.
- The analyzer generated a MEDIUM severity alert.

## Implementation Status
Implemented and tested in `analyze_logs.py`.

## Limitations
This rule analyzes sample logs locally. It does not currently monitor live systems or run as a deployed Wazuh rule.