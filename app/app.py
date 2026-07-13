from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from database import test_connection, get_products
from ai.incident_summary import IncidentSummary
from ai.anomaly_detector import AnomalyDetector
from ai.cache_service import CacheService
from ai.alert_service import AlertService

# ----------------------------
# OpenTelemetry Imports
# ----------------------------
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# ----------------------------
# Configure OpenTelemetry
# ----------------------------
resource = Resource.create({
    "service.name": "monitoring-app"
})

provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

otlp_exporter = OTLPSpanExporter(
    endpoint="otel-collector:4317",
    insecure=True
)

provider.add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

# ----------------------------
# Flask App
# ----------------------------
app = Flask(__name__)

FlaskInstrumentor().instrument_app(app)

# ----------------------------
# AI Services
# ----------------------------
summary = IncidentSummary()
detector = AnomalyDetector()
cache = CacheService()
alert_service = AlertService()

# ----------------------------
# Prometheus Counter
# ----------------------------
REQUEST_COUNT = Counter(
    "home_page_requests_total",
    "Total number of requests to the home page"
)

# ==========================================================
# HOME
# ==========================================================

@app.route("/")
def home():

    REQUEST_COUNT.inc()

    return """
    <h1>AI Predictive Infrastructure Monitoring System</h1>

    <p>Flask Application Running Successfully</p>
    """

# ==========================================================
# HEALTH
# ==========================================================

@app.route("/health")
def health():

    return jsonify({

        "status": "Healthy",
        "application": "Infrastructure Monitoring",
        "version": "1.0"

    })

# ==========================================================
# DATABASE TEST
# ==========================================================

@app.route("/dbtest")
def dbtest():

    result = test_connection()

    if result is True:

        return jsonify({

            "status": "Database Connected Successfully"

        })

    return jsonify({

        "status": "Database Connection Failed",
        "error": result

    })

# ==========================================================
# PRODUCTS
# ==========================================================

@app.route("/products")
def products():

    return jsonify({

        "products": get_products()

    })

# ==========================================================
# CHECKOUT
# ==========================================================

@app.route("/checkout")
def checkout():

    return jsonify({

        "message": "Checkout Successful"

    })

# ==========================================================
# AI INCIDENT SUMMARY
# ==========================================================

@app.route("/ai-summary")
def ai_summary():

    try:

        return jsonify(
            cache.load()
        )

    except Exception as e:

        return jsonify({

            "success": False,
            "error": str(e)

        }), 500


# ==========================================================
# ALERTS
# ==========================================================

@app.route("/alerts")
def alerts():

    try:

        return jsonify({

            "success": True,
            "alerts": alert_service.get_alerts()

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "error": str(e)

        }), 500


# ==========================================================
# PROMETHEUS METRICS
# ==========================================================

@app.route("/metrics")
def metrics():

    return generate_latest(), 200, {

        "Content-Type": CONTENT_TYPE_LATEST

    }

# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000

    )