from ai.anomaly_detector import AnomalyDetector
from ai.incident_summary import IncidentSummary
from ai.alert_service import AlertService


def generate_summary():

    detector = AnomalyDetector()
    summary = IncidentSummary()
    alert_service = AlertService()

    anomalies = detector.detect()

    if anomalies:

        incident = ""

        for anomaly in anomalies:

            incident += f"""
{anomaly['metric']} = {anomaly['value']} {anomaly['unit']}

Status = {anomaly['status']}

"""

            # Automatically create an alert
            alert_service.add_alert(
                metric=anomaly["metric"],
                value=f"{anomaly['value']} {anomaly['unit']}",
                severity=anomaly["status"],
                message=f"{anomaly['metric']} exceeded the configured threshold."
            )

        summary.generate_summary(incident)

        print("AI Summary Generated Successfully")
        print("Alerts Generated Successfully")

    else:

        print("No anomalies detected")


if __name__ == "__main__":
    generate_summary()