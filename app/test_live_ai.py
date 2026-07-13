from ai.anomaly_detector import AnomalyDetector
from ai.incident_summary import IncidentSummary

print("=" * 80)
print("LIVE AI TEST")
print("=" * 80)

detector = AnomalyDetector()

anomalies = detector.detect()

if not anomalies:

    print("No anomalies detected.")

else:

    print("Anomalies Found:")
    print(anomalies)

    incident = ""

   for anomaly in anomalies:

    incident += f"""
{anomaly['metric']} = {anomaly['value']} {anomaly['unit']}

Status = {anomaly['status']}

"""

    ai = IncidentSummary()

    result = ai.generate_summary(incident)

    print()

    print("=" * 80)
    print("AI SUMMARY")
    print("=" * 80)

    print(result)