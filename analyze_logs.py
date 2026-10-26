
from pathlib import Path
from collections import Counter
from datetime import datetime
import re

# Project file locations
project_dir = Path(__file__).parent
log_file = project_dir / "logs" / "sample_auth.log"
report_file = project_dir / "reports" / "alerts.txt"

# Read sample authentication logs
with log_file.open("r", encoding="utf-8") as file:
    logs = file.readlines()

# Count failed logins by username and source IP
failed_logins = Counter()

for line in logs:
    match = re.search(
        r"Failed login for user (\S+) from (\d{1,3}(?:\.\d{1,3}){3})",
        line
    )

    if match:
        username = match.group(1)
        ip_address = match.group(2)
        failed_logins[(username, ip_address)] += 1

print("Mini SOC - Authentication Log Analysis")
print("-" * 42)

alerts = []

# Analyze failed login attempts
for (username, ip_address), count in failed_logins.items():
    print(f"Target username: {username}")
    print(f"Source IP address: {ip_address}")
    print(f"Failed login attempts: {count}")

    if count >= 3:
        if count >= 5:
            severity = "HIGH"
        else:
            severity = "MEDIUM"

        alert = (
            f"{datetime.now():%Y-%m-%d %H:%M:%S} | "
            f"Severity: {severity} | "
            f"Possible brute-force activity | "
            f"User: {username} | IP: {ip_address} | "
            f"Failed attempts: {count}"
        )

        print(f"ALERT [{severity}]: Possible brute-force activity detected!")
        alerts.append(alert)

    print()

# Save a fresh report with a header and alert count
with report_file.open("w", encoding="utf-8") as report:
    report.write("MINI SOC - SECURITY ALERT REPORT\n")
    report.write("=" * 40 + "\n")
    report.write(
        f"Report generated: {datetime.now():%Y-%m-%d %H:%M:%S}\n"
    )
    report.write(f"Total alerts: {len(alerts)}\n\n")

    if alerts:
        for alert in alerts:
            report.write(alert + "\n")
    else:
        report.write("No brute-force alerts detected.\n")

# Display final result
if alerts:
    print(f"{len(alerts)} alert(s) saved to reports/alerts.txt")
else:
    print("No brute-force alerts detected.")

print("Report updated: reports/alerts.txt")
