
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
import re


LOG_PATTERN = re.compile(
    r"Failed login for user (\S+) from (\d{1,3}(?:\.\d{1,3}){3})"
)


def analyze_logs(log_lines):
    """Analyze authentication logs and return security alerts."""
    failed_logins = Counter()
    user_ips = defaultdict(set)

    for line in log_lines:
        match = LOG_PATTERN.search(line)

        if match:
            username, ip_address = match.groups()
            failed_logins[(username, ip_address)] += 1
            user_ips[username].add(ip_address)

    alerts = []

    # Rule 1: Repeated failed logins from the same IP
    for (username, ip_address), count in failed_logins.items():
        if count >= 3:
            severity = "HIGH" if count >= 5 else "MEDIUM"

            alerts.append({
                "severity": severity,
                "type": "brute_force",
                "username": username,
                "ip": ip_address,
                "failed_attempts": count,
            })

    # Rule 2: Failed logins from multiple source IPs
    for username, ip_addresses in user_ips.items():
        if len(ip_addresses) >= 3:
            alerts.append({
                "severity": "MEDIUM",
                "type": "multiple_source_ips",
                "username": username,
                "distinct_ips": len(ip_addresses),
            })

    return alerts


def main():
    project_dir = Path(__file__).parent
    log_file = project_dir / "logs" / "sample_auth.log"
    report_file = project_dir / "reports" / "alerts.txt"

    with log_file.open("r", encoding="utf-8") as file:
        alerts = analyze_logs(file.readlines())

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Mini SOC - Authentication Log Analysis")
    print("-" * 42)

    for alert in alerts:
        print(
            f"ALERT [{alert['severity']}]: "
            f"{alert['type']} | User: {alert['username']}"
        )

    report_file.parent.mkdir(parents=True, exist_ok=True)

    with report_file.open("w", encoding="utf-8") as report:
        report.write("MINI SOC - SECURITY ALERT REPORT\n")
        report.write("=" * 40 + "\n")
        report.write(f"Report generated: {timestamp}\n")
        report.write(f"Total alerts: {len(alerts)}\n\n")

        if not alerts:
            report.write("No security alerts detected.\n")

        for alert in alerts:
            if alert["type"] == "brute_force":
                details = (
                    f"Possible brute-force activity | "
                    f"User: {alert['username']} | "
                    f"IP: {alert['ip']} | "
                    f"Failed attempts: {alert['failed_attempts']}"
                )
            else:
                details = (
                    f"Failed logins from multiple source IPs | "
                    f"User: {alert['username']} | "
                    f"Distinct source IPs: {alert['distinct_ips']}"
                )

            report.write(
                f"{timestamp} | Severity: {alert['severity']} | "
                f"{details}\n"
            )

    print(f"Total alerts: {len(alerts)}")
    print("Report updated: reports/alerts.txt")


if __name__ == "__main__":
    main()
