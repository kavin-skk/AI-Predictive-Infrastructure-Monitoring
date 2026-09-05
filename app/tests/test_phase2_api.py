import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import phase2_api


def test_linear_regression():
    slope, intercept, prediction = phase2_api.linear_regression(
        [1, 2, 3, 4, 5]
    )

    assert slope > 0
    assert intercept >= 0
    assert prediction > 5


def test_ar_forecast():
    result = phase2_api.ar_forecast([10, 20, 30, 40, 50])

    assert result == 80


def test_risk_score():
    assert phase2_api.risk_score(50, 100) == 50
    assert phase2_api.risk_score(150, 100) == 100
    assert phase2_api.risk_score(-10, 100) == 0


def test_build_prediction_data():
    predictions = phase2_api.build_prediction_data()

    assert len(predictions) == 3

    metrics = [x["metric"] for x in predictions]

    assert "Memory Usage" in metrics
    assert "CPU Usage" in metrics
    assert "Database Storage" in metrics

    for prediction in predictions:
        assert prediction["current"] is not None
        assert prediction["predicted"] is not None
        assert prediction["risk_score"] >= 0
        assert prediction["risk_score"] <= 100


def test_predictions_route():
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(phase2_api.phase2)

    client = app.test_client()

    response = client.get("/phase2/predictions")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "Prediction Engine Active"
    assert len(data["predictions"]) == 3


def test_risk_route():
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(phase2_api.phase2)

    client = app.test_client()

    response = client.get("/phase2/risk")

    assert response.status_code == 200

    data = response.get_json()

    assert data["dashboard"] == "Predicted Risk Dashboard"
    assert data["status"] == "ACTIVE"
    assert data["overall_risk"] >= 0
    assert data["highest_risk_metric"]


def test_scenarios_route():
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(phase2_api.phase2)

    client = app.test_client()

    response = client.get("/phase2/scenarios")

    assert response.status_code == 200

    data = response.get_json()

    assert data["scenario_count"] == 5
    assert len(data["scenarios"]) == 5

    scenario_names = [x["scenario"] for x in data["scenarios"]]

    assert "Memory Leak" in scenario_names
    assert "CPU Spike" in scenario_names
    assert "DB Slow Query" in scenario_names
    assert "API Error Surge" in scenario_names
    assert "Container Crash" in scenario_names


def test_classification_route():
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(phase2_api.phase2)

    client = app.test_client()

    response = client.get("/phase2/classification")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "Alert Classification Active"
    assert len(data["classification_results"]) == 3

    for result in data["classification_results"]:
        assert result["classification"]
        assert result["severity"]
        assert result["action"]


def test_load_test_route():
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(phase2_api.phase2)

    client = app.test_client()

    response = client.get("/phase2/load-test")

    assert response.status_code == 200

    data = response.get_json()

    assert data["events_processed"] == 500
    assert data["data_loss"] == 0
    assert data["status"] == "PASSED"
    assert data["events_per_second"] > 0


def test_qa_route():
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(phase2_api.phase2)

    client = app.test_client()

    response = client.get("/phase2/qa")

    assert response.status_code == 200

    data = response.get_json()

    assert data["total_checks"] == 8
    assert data["passed"] == 8
    assert data["failed"] == 0
    assert data["status"] == "PASSED"


def test_e2e_route():
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(phase2_api.phase2)

    client = app.test_client()

    response = client.get("/phase2/e2e")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "END-TO-END DEMONSTRATION PASSED"
    assert data["prediction_count"] == 3
    assert data["scenario_count"] == 5
    assert data["highest_risk"]
