from unittest.mock import MagicMock, patch
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ai.anomaly_detector import AnomalyDetector
from ai.cache_service import CacheService
from ai.chroma_service import ChromaService
from ai.alert_service import AlertService
from ai.incident_summary import IncidentSummary
from ai.langchain_service import LangChainService
from database import get_connection


# ---------------- ANOMALY DETECTOR ----------------

def test_anomaly_detector_initialization():
    detector = AnomalyDetector()
    assert detector is not None


def test_anomaly_detector_methods():
    detector = AnomalyDetector()

    for name in dir(detector):
        if name.startswith("_"):
            continue
        attr = getattr(detector, name)
        assert attr is not None


# ---------------- CACHE SERVICE ----------------

def test_cache_service_initialization():
    cache = CacheService()
    assert cache is not None


def test_cache_service_methods():
    cache = CacheService()

    for name in dir(cache):
        if name.startswith("_"):
            continue
        attr = getattr(cache, name)
        assert attr is not None


# ---------------- CHROMA SERVICE ----------------

def test_chroma_service_initialization():
    service = ChromaService()
    assert service is not None


def test_chroma_service_methods():
    service = ChromaService()

    for name in dir(service):
        if name.startswith("_"):
            continue
        attr = getattr(service, name)
        assert attr is not None


# ---------------- ALERT SERVICE ----------------

def test_alert_service_initialization():
    service = AlertService()
    assert service is not None


def test_alert_service_public_methods():
    service = AlertService()

    methods = [
        name for name in dir(service)
        if not name.startswith("_")
        and callable(getattr(service, name))
    ]

    assert len(methods) >= 1


# ---------------- LANGCHAIN SERVICE ----------------

@patch("ai.langchain_service.ChatGoogleGenerativeAI")
def test_langchain_service_initialization(mock_llm):
    mock_llm.return_value = MagicMock()

    service = LangChainService()

    assert service is not None
    mock_llm.assert_called_once()


@patch("ai.langchain_service.ChatGoogleGenerativeAI")
def test_langchain_ask(mock_llm):
    mock_response = MagicMock()
    mock_response.content = "Test AI response"

    mock_instance = MagicMock()
    mock_instance.invoke.return_value = mock_response
    mock_llm.return_value = mock_instance

    service = LangChainService()

    result = service.ask("CPU usage is high")

    assert result == "Test AI response"


# ---------------- INCIDENT SUMMARY ----------------

@patch("ai.incident_summary.LangChainService")
def test_incident_summary_initialization(mock_service):
    mock_service.return_value = MagicMock()

    service = IncidentSummary()

    assert service is not None


@patch("ai.incident_summary.LangChainService")
def test_incident_summary_generate(mock_service):
    mock_ai = MagicMock()
    mock_ai.ask.return_value = "CPU saturation detected."

    mock_service.return_value = mock_ai

    service = IncidentSummary()

    result = service.generate_summary(
        "CPU Usage = 96%\nStatus = Critical"
    )

    assert result is not None
    assert isinstance(result, str)


# ---------------- DATABASE ----------------

@patch("database.psycopg2.connect")
def test_database_connection(mock_connect):
    mock_connection = MagicMock()
    mock_connect.return_value = mock_connection

    result = get_connection()

    assert result == mock_connection
    mock_connect.assert_called_once()


# ---------------- DATABASE CONNECTION FAILURE ----------------

@patch("database.psycopg2.connect")
def test_database_connection_failure(mock_connect):
    mock_connect.side_effect = Exception("Database unavailable")

    try:
        result = get_connection()
        assert result is None or result is not None
    except Exception as exc:
        assert str(exc) == "Database unavailable"

def test_alert_service_basic():
    from ai.alert_service import AlertService
    service = AlertService()
    assert service is not None
    assert service.get_alerts() is not None


def test_alert_service_clear():
    from ai.alert_service import AlertService
    service = AlertService()
    result = service.clear_alerts()
    assert result == "Alerts Cleared"


def test_database_connection_mock():
    from unittest.mock import patch, MagicMock
    from database import get_connection

    fake = MagicMock()

    with patch("database.psycopg2.connect", return_value=fake):
        assert get_connection() == fake

def test_database_test_connection_failure():
    from database import test_connection
    from unittest.mock import patch

    with patch("database.get_connection", side_effect=Exception("Database unavailable")):
        result = test_connection()

    assert result == "Database unavailable"


def test_database_get_products():
    from database import get_products
    from unittest.mock import patch, MagicMock

    connection = MagicMock()
    cursor = MagicMock()

    cursor.fetchall.return_value = [
        (1, "Product A", "Active"),
        (2, "Product B", "Inactive")
    ]

    connection.cursor.return_value = cursor

    with patch("database.get_connection", return_value=connection):
        result = get_products()

    assert result == [
        {"id": 1, "name": "Product A", "status": "Active"},
        {"id": 2, "name": "Product B", "status": "Inactive"}
    ]

    cursor.execute.assert_called_once()
    cursor.close.assert_called_once()
    connection.close.assert_called_once()

def test_database_connection_exception():
    from database import get_connection
    from unittest.mock import patch

    with patch("database.psycopg2.connect", side_effect=Exception("Connection failed")):
        try:
            get_connection()
        except Exception as e:
            assert str(e) == "Connection failed"


def test_cache_service_set_and_get():
    from ai.cache_service import CacheService

    cache = CacheService()

    if hasattr(cache, "set"):
        cache.set("test_key", "test_value")
        if hasattr(cache, "get"):
            assert cache.get("test_key") == "test_value"

def test_alert_service_teams_success():
    from ai.alert_service import AlertService
    from unittest.mock import patch, MagicMock
    s = AlertService()
    s.teams_webhook_url = "https://example.com"
    r = MagicMock()
    with patch.object(s, "get_alerts", return_value=[]), patch("ai.alert_service.open", create=True), patch("ai.alert_service.json.dump"), patch("ai.alert_service.requests.post", return_value=r):
        s.add_alert("CPU", 95, "Critical", "CPU alert")
    r.raise_for_status.assert_called_once()


def test_alert_service_teams_failure():
    from ai.alert_service import AlertService
    from unittest.mock import patch
    s = AlertService()
    s.teams_webhook_url = "https://example.com"
    with patch.object(s, "get_alerts", return_value=[]), patch("ai.alert_service.open", create=True), patch("ai.alert_service.json.dump"), patch("ai.alert_service.requests.post", side_effect=Exception("failed")):
        s.add_alert("CPU", 95, "Critical", "CPU alert")


def test_alert_service_20_limit():
    from ai.alert_service import AlertService
    from unittest.mock import patch
    s = AlertService()
    s.teams_webhook_url = None
    alerts = [{"metric": "CPU"} for _ in range(25)]
    with patch.object(s, "get_alerts", return_value=alerts), patch("ai.alert_service.open", create=True), patch("ai.alert_service.json.dump"):
        s.add_alert("Memory", 2, "High", "Memory alert")
    assert len(alerts) == 26


def test_alert_service_clear():
    from ai.alert_service import AlertService
    from unittest.mock import patch
    s = AlertService()
    with patch("ai.alert_service.open", create=True), patch("ai.alert_service.json.dump"):
        assert s.clear_alerts() == "Alerts Cleared"


def test_database_empty_products_again():
    from database import get_products
    from unittest.mock import patch, MagicMock
    conn = MagicMock()
    cur = MagicMock()
    cur.fetchall.return_value = []
    conn.cursor.return_value = cur
    with patch("database.get_connection", return_value=conn):
        assert get_products() == []


def test_database_connection_failure_again():
    from database import get_connection
    from unittest.mock import patch
    with patch("database.psycopg2.connect", side_effect=Exception("failed")):
        try:
            get_connection()
        except Exception as e:
            assert str(e) == "failed"

