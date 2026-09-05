from ai.chroma_service import ChromaService

db = ChromaService()

print("=" * 80)
print("ADDING INCIDENTS")
print("=" * 80)

print(
    db.add_incident(
        "INC001",
        """
CPU Usage = 98%

Memory = 95%

Reason = High API Traffic

Solution = Restart Application
""",
        {
            "severity": "Critical"
        }
    )
)

print(
    db.add_incident(
        "INC002",
        """
Database Timeout

Connections = 200

Reason = Connection Pool Exhausted

Solution = Increase Connection Pool
""",
        {
            "severity": "Critical"
        }
    )
)

print()

print("=" * 80)
print("TOTAL INCIDENTS")
print("=" * 80)

print(db.count())

print()

print("=" * 80)
print("SEARCH RESULT")
print("=" * 80)

result = db.search_incident(
    "CPU usage is very high"
)

print(result)

print()

print("=" * 80)
print("ALL INCIDENTS")
print("=" * 80)

print(db.get_all_incidents())