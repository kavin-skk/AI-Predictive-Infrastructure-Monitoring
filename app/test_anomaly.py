from ai.anomaly_detector import AnomalyDetector

detector = AnomalyDetector()

print("=" * 80)
print("ANOMALY DETECTION")
print("=" * 80)

anomalies = detector.detect()

if anomalies:

    print("Anomalies Detected\n")

    for anomaly in anomalies:

        print(anomaly)

else:

    print("No Anomalies Found")