from pathlib import Path
from collections import Counter, defaultdict
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
user_ips = defaultdict(set)

for line in logs:
    match = re.search(
        r"Failed login for user (\S+) from (\d{1,3}(?:\.\d{1,3}){3})",
        line
    )

    if match:
        username = match.group(1)
        ip_address = match.group(2)

        failed_logins[(username, ip_address)] += 1
        user_ips[username].add(ip_address)

print("Mini SOC - Authentication Log Analysis")
print("-" * 42)

alerts = []
alerted_users = set()

# Rule 1: Detect repeated failed logins from the same IP
for (username, ip_address), count in failed_logins.items():
    print(f"Target username: {username}")
    print(f"Source IP address: {ip_address}")
    print(f"Failed login attempts: {count}")

    if count >= 3:
        severity = "HIGH" if count >= 5 else "MEDIUM"

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

# Rule 2: Detect failed logins from multiple source IPs
for username, ip_addresses in user_ips.items():
    if len(ip_addresses) >= 3:
        # Avoid creating a duplicate multi-IP alert for the same user
        if username not in alerted_users:
            alert = (
                f"{datetime.now():%Y-%m-%d %H:%M:%S} | "
                f"Severity: MEDIUM | "
                f"Failed logins from multiple source IPs | "
                f"User: {username} | "
                f"Distinct source IPs: {len(ip_addresses)}"
            )

            print(
                f"ALERT [MEDIUM]: User {username} has failed "
                f"logins from {len(ip_addresses)} different IP addresses!"
            )

            alerts.append(alert)
            alerted_users.add(username)

# Save a fresh report
report_file.parent.mkdir(parents=True, exist_ok=True)

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
        report.write("No security alerts detected.\n")

# Display final result
if alerts:
    print(f"{len(alerts)} alert(s) saved to reports/alerts.txt")
else:
    print("No security alerts detected.")

print("Report updated: reports/alerts.txt")