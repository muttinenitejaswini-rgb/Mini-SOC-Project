
import unittest
from analyze_logs import analyze_logs


class TestMiniSOCAnalyzer(unittest.TestCase):

    def test_three_failed_attempts_medium_alert(self):
        logs = [
            "Failed login for user admin from 192.168.1.25\n"
        ] * 3

        alerts = analyze_logs(logs)

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["severity"], "MEDIUM")
        self.assertEqual(alerts[0]["type"], "brute_force")

    def test_five_failed_attempts_high_alert(self):
        logs = [
            "Failed login for user admin from 192.168.1.25\n"
        ] * 5

        alerts = analyze_logs(logs)

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["severity"], "HIGH")

    def test_two_failed_attempts_no_alert(self):
        logs = [
            "Failed login for user admin from 192.168.1.25\n"
        ] * 2

        alerts = analyze_logs(logs)

        self.assertEqual(len(alerts), 0)

    def test_three_distinct_ips_medium_alert(self):
        logs = [
            "Failed login for user student from 192.168.1.10\n",
            "Failed login for user student from 192.168.1.11\n",
            "Failed login for user student from 192.168.1.12\n",
        ]

        alerts = analyze_logs(logs)

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["severity"], "MEDIUM")
        self.assertEqual(alerts[0]["type"], "multiple_source_ips")
        self.assertEqual(alerts[0]["distinct_ips"], 3)


    def test_malformed_logs_are_ignored(self):
        logs = [
            "This is not a valid authentication log\n",
            "Failed login without an IP address\n",
            "Successful login for user admin\n",
        ]

        alerts = analyze_logs(logs)

        self.assertEqual(len(alerts), 0)
if __name__ == "__main__":
    unittest.main(verbosity=2)
