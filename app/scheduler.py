import time

from generate_ai_summary import generate_summary

print("AI Scheduler Started...")

while True:

    try:

        print("Generating AI Summary...")

        generate_summary()

        print("AI Summary Updated")

    except Exception as e:

        print("Scheduler Error:", e)

    # Run every 60 seconds
    time.sleep(60)