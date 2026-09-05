from ai.incident_summary import IncidentSummary

summary = IncidentSummary()

incident = """
CPU Usage = 96%

Memory Usage = 92%

Database Connections = 180

Status = Critical
"""

print("=" * 80)
print("AI INCIDENT SUMMARY")
print("=" * 80)

print(summary.generate_summary(incident))