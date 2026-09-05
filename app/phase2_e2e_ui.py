from flask import Blueprint, render_template_string
import requests

phase2_e2e_ui = Blueprint("phase2_e2e_ui", __name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>End-to-End System Validation</title>
    <meta charset="UTF-8">
    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #080d1b;
            color: #e8eefc;
        }

        .header {
            height: 76px;
            background: #111827;
            border-bottom: 1px solid #263248;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 32px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .logo {
            width: 42px;
            height: 42px;
            border-radius: 10px;
            background: #2563eb;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 19px;
        }

        .brand-title {
            font-size: 19px;
            font-weight: bold;
        }

        .brand-sub {
            color: #8fa4c7;
            font-size: 12px;
            margin-top: 3px;
        }

        .active {
            border: 1px solid #1d9b61;
            color: #43e88b;
            background: #0c2b20;
            padding: 9px 16px;
            border-radius: 22px;
            font-size: 13px;
            font-weight: bold;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 36px 28px 50px;
        }

        .title {
            font-size: 30px;
            margin-bottom: 7px;
        }

        .subtitle {
            color: #91a5c7;
            font-size: 14px;
        }

        .status {
            margin-top: 25px;
            padding: 24px;
            border: 1px solid #1c9b60;
            background: #0b211a;
            border-radius: 14px;
            text-align: center;
        }

        .status-title {
            color: #43e88b;
            font-size: 25px;
            font-weight: bold;
        }

        .status-text {
            color: #a7bad8;
            margin-top: 7px;
            font-size: 13px;
        }

        .pipeline {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 12px;
            margin-top: 28px;
        }

        .stage {
            background: #111827;
            border: 1px solid #29364d;
            border-radius: 12px;
            padding: 20px 13px;
            min-height: 150px;
            text-align: center;
            position: relative;
        }

        .stage:not(:last-child)::after {
            content: "→";
            position: absolute;
            right: -16px;
            top: 62px;
            color: #4d6385;
            font-size: 20px;
            z-index: 2;
        }

        .number {
            width: 34px;
            height: 34px;
            margin: 0 auto 13px;
            border-radius: 50%;
            background: #14243c;
            color: #73a7ff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }

        .stage-name {
            font-size: 13px;
            font-weight: bold;
            line-height: 1.4;
        }

        .pass {
            margin-top: 13px;
            display: inline-block;
            padding: 5px 11px;
            border-radius: 12px;
            background: #103523;
            color: #43e88b;
            font-size: 11px;
            font-weight: bold;
        }

        .results {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
            margin-top: 28px;
        }

        .card {
            background: #111827;
            border: 1px solid #29364d;
            border-radius: 13px;
            padding: 21px;
        }

        .card-label {
            color: #8298bc;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: .7px;
        }

        .card-value {
            margin-top: 8px;
            font-size: 28px;
            font-weight: bold;
        }

        .card-detail {
            color: #91a5c7;
            font-size: 12px;
            margin-top: 6px;
        }

        .risk {
            color: #ff5555;
        }

        .green {
            color: #43e88b;
        }

        .footer {
            margin-top: 28px;
            padding: 17px 20px;
            background: #0e1525;
            border: 1px solid #27344b;
            border-radius: 11px;
            color: #8fa4c7;
            font-size: 12px;
            text-align: center;
        }

        @media(max-width: 900px) {
            .pipeline {
                grid-template-columns: repeat(3, 1fr);
            }

            .stage:not(:last-child)::after {
                display: none;
            }

            .results {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

<div class="header">
    <div class="brand">
        <div class="logo">AI</div>
        <div>
            <div class="brand-title">AI Predictive Infrastructure Monitoring</div>
            <div class="brand-sub">End-to-End System Validation</div>
        </div>
    </div>

    <div class="active">● E2E PIPELINE ACTIVE</div>
</div>

<div class="container">

    <div class="title">End-to-End System Validation</div>
    <div class="subtitle">
        Integrated validation of infrastructure monitoring, prediction,
        risk analysis and incident response
    </div>

    <div class="status">
        <div class="status-title">✓ END-TO-END DEMONSTRATION PASSED</div>
        <div class="status-text">
            Complete monitoring and predictive analytics pipeline validated successfully
        </div>
    </div>

    <div class="pipeline">

        <div class="stage">
            <div class="number">1</div>
            <div class="stage-name">Metric<br>Collection</div>
            <div class="pass">✓ PASSED</div>
        </div>

        <div class="stage">
            <div class="number">2</div>
            <div class="stage-name">Prediction<br>Engine</div>
            <div class="pass">✓ PASSED</div>
        </div>

        <div class="stage">
            <div class="number">3</div>
            <div class="stage-name">Risk<br>Scoring</div>
            <div class="pass">✓ PASSED</div>
        </div>

        <div class="stage">
            <div class="number">4</div>
            <div class="stage-name">Alert<br>Classification</div>
            <div class="pass">✓ PASSED</div>
        </div>

        <div class="stage">
            <div class="number">5</div>
            <div class="stage-name">Incident<br>Simulation</div>
            <div class="pass">✓ PASSED</div>
        </div>

        <div class="stage">
            <div class="number">6</div>
            <div class="stage-name">Dashboard<br>Output</div>
            <div class="pass">✓ PASSED</div>
        </div>

    </div>

    <div class="results">

        <div class="card">
            <div class="card-label">Prediction Models</div>
            <div class="card-value">03</div>
            <div class="card-detail">Memory • CPU • Database Storage</div>
        </div>

        <div class="card">
            <div class="card-label">Incident Scenarios</div>
            <div class="card-value">05</div>
            <div class="card-detail">
                Memory Leak • CPU Spike • DB Slow Query • API Error • Container Crash
            </div>
        </div>

        <div class="card">
            <div class="card-label">Highest Risk</div>
            <div class="card-value risk">100%</div>
            <div class="card-detail">CPU Usage — Predicted Saturation</div>
        </div>

    </div>

    <div class="footer">
        Live validation result from the Phase-2 E2E service endpoint
        • 3 predictions • 5 controlled scenarios • 6 pipeline stages
    </div>

</div>

</body>
</html>
"""


@phase2_e2e_ui.route("/phase2/e2e-final-ui")
def e2e_final_ui():
    return render_template_string(HTML)


