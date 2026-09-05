import os
import traceback
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()


class LangChainService:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-flash-latest",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.2,
            max_tokens=1024
        )

    def ask(self, prompt: str):

        try:

            response = self.llm.invoke(
                [HumanMessage(content=prompt)]
            )

            # Latest LangChain returns content as a list
            if isinstance(response.content, list):

                final_text = ""

                for item in response.content:

                    if isinstance(item, dict):

                        if item.get("type") == "text":
                            final_text += item.get("text", "")

                    elif isinstance(item, str):

                        final_text += item

                return final_text.strip()

            return str(response.content)

        except Exception:

            traceback.print_exc()

            raise

    def summarize_incident(self, incident):

        prompt = f"""
You are an AI Infrastructure Monitoring Assistant.

Analyze the following monitoring incident.

Incident

{incident}

Provide

1. Root Cause
2. Severity
3. Recommended Fix
4. Preventive Action

Keep the answer professional.
"""

        return self.ask(prompt)

    def explain_metric(self, metric_name, metric_value):

        prompt = f"""
Explain the following infrastructure metric.

Metric

{metric_name}

Value

{metric_value}

Explain

• What it means

• Why it matters

• Whether it is healthy

• Recommended action
"""

        return self.ask(prompt)

    def compare_incidents(self, current_incident, previous_incident):

        prompt = f"""
Compare these two incidents.

Current Incident

{current_incident}

Previous Incident

{previous_incident}

Explain

1. Similarities

2. Differences

3. Whether the same solution can be applied
"""

        return self.ask(prompt)