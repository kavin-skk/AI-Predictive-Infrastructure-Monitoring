from ai.chroma_service import ChromaService

db = ChromaService()

incidents = [

{
"id":"INC001",
"text":"""
CPU Usage = 98%

Memory = 95%

Reason = High API Traffic

Solution = Restart Application
""",
"metadata":{"severity":"Critical"}
},

{
"id":"INC002",
"text":"""
Database Timeout

Connections = 200

Reason = Connection Pool Exhausted

Solution = Increase Connection Pool Size
""",
"metadata":{"severity":"Critical"}
},

{
"id":"INC003",
"text":"""
Memory Usage = 97%

Reason = Memory Leak

Solution = Restart Service and Fix Memory Leak
""",
"metadata":{"severity":"Critical"}
},

{
"id":"INC004",
"text":"""
Disk Usage = 99%

Reason = Log Files Filled Disk

Solution = Delete Logs and Expand Storage
""",
"metadata":{"severity":"High"}
},

{
"id":"INC005",
"text":"""
High Network Latency

Reason = Network Congestion

Solution = Restart Network Interface
""",
"metadata":{"severity":"High"}
},

{
"id":"INC006",
"text":"""
PostgreSQL Deadlock

Reason = Multiple Transactions Waiting

Solution = Kill Blocking Session
""",
"metadata":{"severity":"Critical"}
},

{
"id":"INC007",
"text":"""
Application Response Time = 12 Seconds

Reason = Slow SQL Query

Solution = Optimize SQL Query
""",
"metadata":{"severity":"High"}
},

{
"id":"INC008",
"text":"""
Container Restart Loop

Reason = Application Crash

Solution = Check Logs and Restart Container
""",
"metadata":{"severity":"Critical"}
},

{
"id":"INC009",
"text":"""
Authentication Failure

Reason = Expired Token

Solution = Refresh Credentials
""",
"metadata":{"severity":"Medium"}
},

{
"id":"INC010",
"text":"""
SSL Certificate Expired

Reason = Certificate Not Renewed

Solution = Renew SSL Certificate
""",
"metadata":{"severity":"High"}
},

{
"id":"INC011",
"text":"""
Redis Cache Failure

Reason = Cache Server Down

Solution = Restart Redis Service
""",
"metadata":{"severity":"High"}
},

{
"id":"INC012",
"text":"""
Kafka Queue Backlog

Reason = Consumer Not Processing

Solution = Scale Kafka Consumers
""",
"metadata":{"severity":"High"}
},

{
"id":"INC013",
"text":"""
High Disk IO

Reason = Heavy Read Write Operations

Solution = Optimize Disk Access
""",
"metadata":{"severity":"Medium"}
},

{
"id":"INC014",
"text":"""
OOM Kill

Reason = Out Of Memory

Solution = Increase RAM
""",
"metadata":{"severity":"Critical"}
},

{
"id":"INC015",
"text":"""
High Error Rate

Reason = API Failure

Solution = Rollback Latest Deployment
""",
"metadata":{"severity":"Critical"}
},

{
"id":"INC016",
"text":"""
CPU Usage = 94%

Reason = Infinite Loop

Solution = Restart Application
""",
"metadata":{"severity":"High"}
},

{
"id":"INC017",
"text":"""
Database Connection Failure

Reason = PostgreSQL Down

Solution = Restart PostgreSQL
""",
"metadata":{"severity":"Critical"}
},

{
"id":"INC018",
"text":"""
Service Crash

Reason = Null Pointer Exception

Solution = Fix Application Code
""",
"metadata":{"severity":"Critical"}
},

{
"id":"INC019",
"text":"""
Gateway Timeout

Reason = Backend Service Slow

Solution = Optimize Backend Service
""",
"metadata":{"severity":"High"}
},

{
"id":"INC020",
"text":"""
Container CPU = 99%

Reason = High Background Processing

Solution = Scale Containers
""",
"metadata":{"severity":"Critical"}
}

]

print("="*80)
print("LOADING INCIDENTS")
print("="*80)

for incident in incidents:

    try:

        db.add_incident(

            incident_id=incident["id"],
            incident=incident["text"],
            metadata=incident["metadata"]

        )

        print(f"{incident['id']} Loaded")

    except Exception:

        print(f"{incident['id']} Already Exists")

print()

print("="*80)
print("TOTAL INCIDENTS")
print("="*80)

print(db.count())