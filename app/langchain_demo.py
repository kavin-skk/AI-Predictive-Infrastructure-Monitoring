from ai.langchain_service import LangChainService

ai = LangChainService()

print("\n")
print("=" * 80)
print("INFRASTRUCTURE INCIDENT SUMMARY")
print("=" * 80)

incident = """
CPU Usage : 96%
Memory Usage : 92%
Database Connections : 180
Status : Critical
"""

print(ai.summarize_incident(incident))

print("\n")
print("=" * 80)
print("METRIC EXPLANATION")
print("=" * 80)

print(ai.explain_metric("CPU Usage", "96%"))

print("\n")
print("=" * 80)
print("INCIDENT COMPARISON")
print("=" * 80)

current = """
CPU Usage : 95%
Database Timeout
"""

previous = """
CPU Usage : 97%
Application Crash
"""

print(ai.compare_incidents(current, previous))