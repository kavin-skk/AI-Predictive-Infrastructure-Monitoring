import requests

BASE = "http://localhost:5000"


def test_health():
    r = requests.get(f"{BASE}/health", timeout=10)
    assert r.status_code == 200


def test_prediction_engine():
    r = requests.get(f"{BASE}/phase2/predictions", timeout=10)
    assert r.status_code == 200

    data = r.json()

    assert data["status"] == "Prediction Engine Active"
    assert len(data["predictions"]) == 3

    metrics = [x["metric"] for x in data["predictions"]]

    assert "Memory Usage" in metrics
    assert "CPU Usage" in metrics
    assert "Database Storage" in metrics


def test_risk_dashboard():
    r = requests.get(f"{BASE}/phase2/risk", timeout=10)
    assert r.status_code == 200

    data = r.json()

    assert data["status"] == "ACTIVE"
    assert 0 <= data["overall_risk"] <= 100
    assert len(data["predictions"]) == 3


def test_alert_classification():
    r = requests.get(f"{BASE}/phase2/classification", timeout=10)
    assert r.status_code == 200

    data = r.json()

    assert data["status"] == "Alert Classification Active"
    assert len(data["classification_results"]) == 3

    for alert in data["classification_results"]:
        assert alert["classification"]
        assert alert["severity"]
        assert alert["action"]


def test_incident_scenarios():
    r = requests.get(f"{BASE}/phase2/scenarios", timeout=10)
    assert r.status_code == 200

    data = r.json()

    assert data["status"] == "Controlled Incident Simulation"
    assert data["scenario_count"] == 5
    assert len(data["scenarios"]) == 5


def test_e2e_pipeline():
    r = requests.get(f"{BASE}/phase2/e2e", timeout=10)
    assert r.status_code == 200

    data = r.json()

    assert data["status"] == "END-TO-END DEMONSTRATION PASSED"
    assert data["prediction_count"] == 3
    assert data["scenario_count"] == 5
    assert len(data["pipeline"]) >= 5
