from ai.langchain_service import LangChainService
from ai.chroma_service import ChromaService
from ai.cache_service import CacheService


class IncidentSummary:

    def __init__(self):

        self.ai = LangChainService()
        self.db = ChromaService()
        self.cache = CacheService()

    def generate_summary(self, incident):

        print("STEP 1 - Incident received")

        try:

            print("STEP 2 - Searching ChromaDB")

            search_result = self.db.search_incident(
                incident,
                results=1
            )

            previous_incident = ""

            if len(search_result["documents"][0]) > 0:
                previous_incident = search_result["documents"][0][0]

        except Exception as e:

            print("Chroma Error:", e)

            previous_incident = ""

        print("STEP 3 - Calling Gemini")

        prompt = f"""
You are an AI Infrastructure Monitoring Assistant.

Current Incident

{incident}

Historical Incident

{previous_incident}

Provide

1. Root Cause

2. Severity

3. Recommended Fix

4. Preventive Action
"""

        ai_result = self.ai.ask(prompt)

        print("STEP 4 - Saving Cache")

        cache_data = {

            "success": True,

            "status": "Critical",

            "incident": incident,

            "ai_summary": ai_result

        }

        self.cache.save(cache_data)

        print("STEP 5 - Finished")

        return ai_result