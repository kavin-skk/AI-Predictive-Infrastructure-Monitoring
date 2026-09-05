import os
import json
import requests
from datetime import datetime


class AlertService:

    def __init__(self):

        self.teams_webhook_url = os.getenv("TEAMS_WEBHOOK_URL")

        self.alert_file = os.path.join(
            os.path.dirname(__file__),
            "../cache/alerts.json"
        )

        # Create the alert file if it doesn't exist
        if not os.path.exists(self.alert_file):

            with open(self.alert_file, "w") as f:

                json.dump([], f, indent=4)

    # ---------------------------------
    # Get All Alerts
    # ---------------------------------

    def get_alerts(self):

        try:

            with open(self.alert_file, "r") as f:

                return json.load(f)

        except Exception:

            return []

    # ---------------------------------
    # Add Alert
    # ---------------------------------

    def add_alert(self, metric, value, severity, message):

        alert_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        alerts = self.get_alerts()

        alerts.insert(0, {

            "time": alert_time,

            "metric": metric,

            "value": value,

            "severity": severity,

            "message": message

        })

        # Keep only latest 20 alerts
        alerts = alerts[:20]

        with open(self.alert_file, "w") as f:

            json.dump(alerts, f, indent=4)

        # ---------------------------------
        # Send Alert to Microsoft Teams
        # ---------------------------------

        if self.teams_webhook_url:

            teams_message = {
                "text": f"""🚨 Infrastructure Alert

Metric: {metric}
Value: {value}
Severity: {severity}

Message: {message}

Time: {alert_time}"""
            }

            try:

                response = requests.post(
                    self.teams_webhook_url,
                    json=teams_message,
                    timeout=10
                )

                response.raise_for_status()

                print("Teams notification sent successfully")

            except Exception as e:

                print("Teams notification failed:", e)

    # ---------------------------------
    # Clear Alerts
    # ---------------------------------

    def clear_alerts(self):

        with open(self.alert_file, "w") as f:

            json.dump([], f, indent=4)

        return "Alerts Cleared"