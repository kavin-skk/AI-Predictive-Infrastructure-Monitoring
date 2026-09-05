from flask import Blueprint, render_template_string

phase2_ui = Blueprint("phase2_ui", __name__)

HTML = r"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Predictive Infrastructure Monitoring</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #0b1120;
            color: #e5e7eb;
        }

        .topbar {
            height: 72px;
            background: #111827;
            border-bottom: 1px solid #263244;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 34px;
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
            font-size: 21px;
            font-weight: bold;
        }

        .title {
            font-size: 20px;
            font-weight: 700;
        }

        .subtitle {
            color: #94a3b8;
            font-size: 12px;
            margin-top: 3px;
        }

        .status {
            display: flex;
            align-items: center;
            gap: 8px;
            background: #10251b;
            border: 1px solid #1f6b43;
            padding: 8px 14px;
            border-radius: 20px;
            color: #4ade80;
            font-size: 13px;
            font-weight: 600;
        }

        .dot {
            width: 8px;
            height: 8px;
            background: #4ade80;
            border-radius: 50%;
        }

        .container {
            padding: 30px 36px 50px;
            max-width: 1500px;
            margin: auto;
        }

        .heading {
            display: flex;
            justify-content: space-between;
            align-items: end;
            margin-bottom: 24px;
        }

        h1 {
            margin: 0;
            font-size: 28px;
        }

        .muted {
            color: #94a3b8;
            font-size: 13px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            margin-bottom: 24px;
        }

        .card {
            background: #111827;
            border: 1px solid #263244;
            border-radius: 14px;
            padding: 20px;
            box-shadow: 0 8px 25px rgba(0,0,0,.18);
        }

        .card-label {
            color: #94a3b8;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: .8px;
        }

        .card-value {
            font-size: 32px;
            font-weight: 700;
            margin-top: 10px;
        }

        .risk-high {
            color: #f59e0b;
        }

        .risk-critical {
            color: #ef4444;
        }

        .risk-low {
            color: #4ade80;
        }

        .section {
            margin-top: 26px;
        }

        .section-title {
            font-size: 17px;
            font-weight: 700;
            margin-bottom: 14px;
        }

        .prediction-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
        }

        .prediction {
            background: #111827;
            border: 1px solid #263244;
            border-radius: 14px;
            padding: 22px;
        }

        .prediction-head {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
        }

        .metric-name {
            font-size: 18px;
            font-weight: 700;
        }

        .badge {
            padding: 5px 9px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            background: #3b1d1d;
            color: #f87171;
        }

        .values {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .value-box {
            background: #0b1120;
            border: 1px solid #202b3d;
            border-radius: 9px;
            padding: 13px;
        }

        .value-label {
            font-size: 11px;
            color: #94a3b8;
        }

        .value-number {
            font-size: 23px;
            font-weight: 700;
            margin-top: 5px;
        }

        .arrow {
            color: #60a5fa;
            margin: 0 4px;
        }

        .bar-bg {
            margin-top: 17px;
            height: 9px;
            background: #1f2937;
            border-radius: 8px;
            overflow: hidden;
        }

        .bar {
            height: 100%;
            border-radius: 8px;
            background: #ef4444;
        }

        .risk-info {
            display: flex;
            justify-content: space-between;
            margin-top: 8px;
            font-size: 12px;
            color: #94a3b8;
        }

        .model {
            margin-top: 17px;
            padding-top: 14px;
            border-top: 1px solid #263244;
            color: #93c5fd;
            font-size: 12px;
        }

        .prediction-text {
            margin-top: 8px;
            color: #cbd5e1;
            font-size: 13px;
        }

        .pipeline {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 8px;
            align-items: center;
        }

        .step {
            background: #111827;
            border: 1px solid #263244;
            border-radius: 12px;
            padding: 17px 10px;
            text-align: center;
            min-height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 600;
        }

        .arrow-step {
            color: #60a5fa;
            text-align: center;
            font-size: 20px;
        }

        .footer {
            margin-top: 35px;
            color: #64748b;
            font-size: 11px;
            text-align: right;
        }

        @media(max-width: 1000px) {
            .cards,
            .prediction-grid {
                grid-template-columns: 1fr;
            }

            .pipeline {
                grid-template-columns: 1fr 1fr;
            }
        }
    </style>
</head>

<body>

<div class="topbar">
    <div class="brand">
        <div class="logo">AI</div>
        <div>
            <div class="title">AI Predictive Infrastructure Monitoring</div>
            <div class="subtitle">Infrastructure Health • Failure Prediction • Risk Analytics</div>
        </div>
    </div>

    <div class="status">
        <span class="dot"></span>
        Prediction Engine Active
    </div>
</div>

<div class="container">

    <div class="heading">
        <div>
            <h1>Predicted Infrastructure Risk</h1>
            <div class="muted">
                AI-assisted failure prediction and infrastructure risk analysis
            </div>
        </div>

        <div class="muted" id="timestamp">Loading...</div>
    </div>

    <div class="cards">

        <div class="card">
            <div class="card-label">Overall Risk</div>
            <div class="card-value risk-critical" id="overallRisk">--</div>
            <div class="muted">Highest predicted infrastructure risk</div>
        </div>

        <div class="card">
            <div class="card-label">Highest Risk Metric</div>
            <div class="card-value" id="highestMetric">--</div>
            <div class="muted">Requires attention</div>
        </div>

        <div class="card">
            <div class="card-label">Prediction Models</div>
            <div class="card-value">03</div>
            <div class="muted">Memory • CPU • Database</div>
        </div>

        <div class="card">
            <div class="card-label">Prediction Status</div>
            <div class="card-value risk-low">ACTIVE</div>
            <div class="muted">Analysis engine operational</div>
        </div>

    </div>

    <div class="section">
        <div class="section-title">Failure Prediction Analysis</div>

        <div class="prediction-grid" id="predictions">
            <div class="card">Loading prediction data...</div>
        </div>
    </div>

    <div class="section">

        <div class="section-title">Predictive Monitoring Pipeline</div>

        <div class="pipeline">
            <div class="step">Metric<br>Collection</div>
            <div class="arrow-step">→</div>
            <div class="step">Prediction<br>Engine</div>
            <div class="arrow-step">→</div>
            <div class="step">Risk<br>Scoring</div>
            <div class="arrow-step">→</div>
        </div>

        <div class="pipeline" style="margin-top:8px">
            <div class="step">Alert<br>Classification</div>
            <div class="arrow-step">→</div>
            <div class="step">Incident<br>Simulation</div>
            <div class="arrow-step">→</div>
            <div class="step">Dashboard<br>Output</div>
            <div class="step">E2E<br>Validation</div>
        </div>

    </div>

    <div class="footer">
        AI Predictive Infrastructure Monitoring System • Live application data
    </div>

</div>

<script>

function riskClass(score) {
    if (score >= 90) return "risk-critical";
    if (score >= 70) return "risk-high";
    return "risk-low";
}

function renderPredictions(data) {

    const list = data.predictions || [];

    document.getElementById("predictions").innerHTML =
        list.map(p => {

            const score = Number(p.risk_score || 0);
            const cls = riskClass(score);

            return `
                <div class="prediction">

                    <div class="prediction-head">
                        <div class="metric-name">${p.metric}</div>
                        <div class="badge">${score >= 90 ? "CRITICAL" : "HIGH RISK"}</div>
                    </div>

                    <div class="muted">
                        Component: ${p.component}
                    </div>

                    <div class="values">

                        <div class="value-box">
                            <div class="value-label">CURRENT</div>
                            <div class="value-number">
                                ${p.current} ${p.unit}
                            </div>
                        </div>

                        <div class="value-box">
                            <div class="value-label">PREDICTED</div>
                            <div class="value-number ${cls}">
                                ${p.predicted} ${p.unit}
                            </div>
                        </div>

                    </div>

                    <div class="bar-bg">
                        <div class="bar" style="width:${score}%"></div>
                    </div>

                    <div class="risk-info">
                        <span>Risk Score</span>
                        <strong class="${cls}">${score}%</strong>
                    </div>

                    <div class="model">
                        MODEL: ${p.model}
                    </div>

                    <div class="prediction-text">
                        ${p.prediction}
                    </div>

                </div>
            `;

        }).join("");
}

async function loadDashboard() {

    try {

        const riskResponse =
            await fetch("/phase2/risk");

        const riskData =
            await riskResponse.json();

        document.getElementById("overallRisk").innerText =
            riskData.overall_risk + "%";

        document.getElementById("highestMetric").innerText =
            riskData.highest_risk_metric;

        document.getElementById("timestamp").innerText =
            new Date(riskData.timestamp).toLocaleString();

        renderPredictions(riskData);

    } catch (error) {

        document.getElementById("predictions").innerHTML =
            `<div class="card">
                Unable to load prediction service.
             </div>`;

    }

}

loadDashboard();

setInterval(loadDashboard, 30000);

</script>

</body>
</html>
"""


@phase2_ui.route("/phase2/dashboard")
def dashboard():
    return render_template_string(HTML)



@phase2_ui.route("/phase2/alerts-ui")
def alerts_ui():

    ALERT_HTML = r"""
<!DOCTYPE html>
<html>
<head>
<title>Infrastructure Alert Classification</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: #0b1120;
    color: #e5e7eb;
}

.topbar {
    height: 72px;
    background: #111827;
    border-bottom: 1px solid #263244;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 34px;
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
    font-size: 20px;
    font-weight: bold;
}

.title {
    font-size: 20px;
    font-weight: 700;
}

.subtitle {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 3px;
}

.status {
    padding: 8px 15px;
    border-radius: 20px;
    border: 1px solid #1f6b43;
    background: #10251b;
    color: #4ade80;
    font-size: 13px;
    font-weight: 600;
}

.container {
    max-width: 1450px;
    margin: auto;
    padding: 32px 36px 50px;
}

.heading {
    display: flex;
    justify-content: space-between;
    align-items: end;
    margin-bottom: 25px;
}

h1 {
    margin: 0;
    font-size: 28px;
}

.muted {
    color: #94a3b8;
    font-size: 13px;
}

.summary {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-bottom: 28px;
}

.card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 14px;
    padding: 20px;
}

.label {
    color: #94a3b8;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: .8px;
}

.number {
    font-size: 32px;
    font-weight: 700;
    margin-top: 9px;
}

.green { color: #4ade80; }
.red { color: #ef4444; }
.orange { color: #f59e0b; }

.section-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 15px;
}

.alert-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
}

.alert-card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 14px;
    padding: 22px;
}

.alert-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.alert-title {
    font-size: 17px;
    font-weight: 700;
}

.badge {
    padding: 5px 10px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
}

.critical {
    background: #3b1717;
    color: #f87171;
}

.high {
    background: #3b2914;
    color: #fbbf24;
}

.alert-text {
    margin-top: 18px;
    padding: 13px;
    background: #0b1120;
    border: 1px solid #202b3d;
    border-radius: 9px;
    color: #cbd5e1;
    font-size: 13px;
    line-height: 1.5;
}

.classification {
    margin-top: 16px;
}

.classification-label {
    color: #94a3b8;
    font-size: 11px;
    text-transform: uppercase;
}

.classification-value {
    color: #60a5fa;
    font-size: 16px;
    font-weight: 700;
    margin-top: 5px;
}

.action {
    margin-top: 15px;
    padding-top: 15px;
    border-top: 1px solid #263244;
    color: #cbd5e1;
    font-size: 13px;
}

.footer {
    margin-top: 35px;
    text-align: right;
    color: #64748b;
    font-size: 11px;
}

@media(max-width: 1000px) {
    .summary,
    .alert-grid {
        grid-template-columns: 1fr;
    }
}
</style>
</head>

<body>

<div class="topbar">

    <div class="brand">
        <div class="logo">AI</div>

        <div>
            <div class="title">
                AI Predictive Infrastructure Monitoring
            </div>

            <div class="subtitle">
                Intelligent Alert Classification & Incident Triage
            </div>
        </div>
    </div>

    <div class="status">
        ● Alert Classification Active
    </div>

</div>

<div class="container">

    <div class="heading">

        <div>
            <h1>Infrastructure Alert Classification</h1>

            <div class="muted">
                AI-assisted classification of infrastructure alerts
                and recommended operational actions
            </div>
        </div>

        <div class="muted" id="timestamp">
            Loading...
        </div>

    </div>


    <div class="summary">

        <div class="card">
            <div class="label">Alerts Analyzed</div>
            <div class="number" id="total">--</div>
            <div class="muted">Current alert set</div>
        </div>

        <div class="card">
            <div class="label">Critical Alerts</div>
            <div class="number red" id="critical">--</div>
            <div class="muted">Immediate attention</div>
        </div>

        <div class="card">
            <div class="label">High Severity</div>
            <div class="number orange" id="high">--</div>
            <div class="muted">Requires investigation</div>
        </div>

        <div class="card">
            <div class="label">Classification Status</div>
            <div class="number green">ACTIVE</div>
            <div class="muted">Alert triage operational</div>
        </div>

    </div>


    <div class="section-title">
        Classified Infrastructure Alerts
    </div>

    <div class="alert-grid" id="alerts">

        <div class="card">
            Loading alert classification...
        </div>

    </div>


    <div class="footer">
        Live classification data from Phase-2 monitoring application
    </div>

</div>


<script>

async function loadAlerts() {

    try {

        const response =
            await fetch("/phase2/classification");

        const data =
            await response.json();

        const alerts =
            data.classification_results || [];

        document.getElementById("total").innerText =
            alerts.length;

        document.getElementById("critical").innerText =
            alerts.filter(a => a.severity === "Critical").length;

        document.getElementById("high").innerText =
            alerts.filter(a => a.severity === "High").length;

        document.getElementById("timestamp").innerText =
            new Date().toLocaleString();

        document.getElementById("alerts").innerHTML =
            alerts.map(a => {

                const severityClass =
                    a.severity === "Critical"
                    ? "critical"
                    : "high";

                return `
                    <div class="alert-card">

                        <div class="alert-header">

                            <div class="alert-title">
                                ${a.classification}
                            </div>

                            <div class="badge ${severityClass}">
                                ${a.severity.toUpperCase()}
                            </div>

                        </div>

                        <div class="alert-text">
                            <b>Alert:</b><br>
                            ${a.alert}
                        </div>

                        <div class="classification">

                            <div class="classification-label">
                                Classification
                            </div>

                            <div class="classification-value">
                                ${a.classification}
                            </div>

                        </div>

                        <div class="action">
                            <b>Recommended Action</b><br><br>
                            ${a.action}
                        </div>

                    </div>
                `;

            }).join("");

    } catch(error) {

        document.getElementById("alerts").innerHTML =
            `<div class="card">
                Unable to load classification service.
             </div>`;

    }

}

loadAlerts();

setInterval(loadAlerts, 30000);

</script>

</body>
</html>
"""

    return render_template_string(ALERT_HTML)


@phase2_ui.route("/phase2/incidents")
def incidents():
    return render_template_string(HTML.replace(
        "Predicted Infrastructure Risk",
        "Controlled Incident Scenarios"
    ))


@phase2_ui.route("/phase2/e2e-ui")
def e2e_ui():
    return render_template_string(HTML.replace(
        "Predicted Infrastructure Risk",
        "End-to-End Monitoring Validation"
    ))

@phase2_ui.route("/phase2/incidents-ui")
def incidents_ui():

    INCIDENT_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Incident Simulation</title>
<style>
*{box-sizing:border-box}
body{
margin:0;
font-family:Arial,sans-serif;
background:#0b1120;
color:#e5e7eb
}
.top{
height:70px;
background:#111827;
border-bottom:1px solid #263244;
display:flex;
align-items:center;
justify-content:space-between;
padding:0 35px
}
.logo{
background:#2563eb;
padding:11px 14px;
border-radius:10px;
font-weight:bold;
font-size:20px
}
.brand{
display:flex;
align-items:center;
gap:14px
}
.title{font-size:20px;font-weight:bold}
.sub{font-size:12px;color:#94a3b8}
.active{
color:#4ade80;
border:1px solid #1f6b43;
background:#10251b;
padding:8px 14px;
border-radius:20px;
font-size:13px
}
.container{
max-width:1450px;
margin:auto;
padding:35px
}
h1{margin:0;font-size:28px}
.desc{color:#94a3b8;margin-top:6px;font-size:13px}
.summary{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:18px;
margin:25px 0
}
.stat{
background:#111827;
border:1px solid #263244;
border-radius:14px;
padding:20px
}
.label{
font-size:11px;
color:#94a3b8;
text-transform:uppercase
}
.num{
font-size:30px;
font-weight:bold;
margin-top:8px
}
.grid{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:18px
}
.incident{
background:#111827;
border:1px solid #263244;
border-radius:14px;
padding:22px
}
.head{
display:flex;
justify-content:space-between;
align-items:center
}
.name{
font-size:17px;
font-weight:bold
}
.badge{
padding:6px 10px;
border-radius:6px;
font-size:10px;
font-weight:bold
}
.critical{
background:#3b1717;
color:#f87171
}
.high{
background:#3b2914;
color:#fbbf24
}
.row{
margin-top:18px;
padding:12px;
background:#0b1120;
border-radius:8px;
border:1px solid #202b3d
}
.key{
font-size:10px;
color:#94a3b8;
text-transform:uppercase
}
.value{
margin-top:5px;
font-size:14px
}
.pred{
color:#60a5fa;
font-weight:bold
}
.footer{
margin-top:30px;
color:#64748b;
font-size:11px;
text-align:right
}
</style>
</head>

<body>

<div class="top">
<div class="brand">
<div class="logo">AI</div>
<div>
<div class="title">AI Predictive Infrastructure Monitoring</div>
<div class="sub">Controlled Incident Simulation & Failure Analysis</div>
</div>
</div>
<div class="active">● Simulation Active</div>
</div>

<div class="container">

<h1>Infrastructure Incident Simulation</h1>
<div class="desc">
Controlled failure scenarios used to validate predictive monitoring and risk analysis
</div>

<div class="summary">
<div class="stat">
<div class="label">Scenarios</div>
<div class="num" id="count">--</div>
</div>

<div class="stat">
<div class="label">Critical</div>
<div class="num" id="critical">--</div>
</div>

<div class="stat">
<div class="label">High Severity</div>
<div class="num" id="high">--</div>
</div>
</div>

<div class="grid" id="grid"></div>

<div class="footer">
Live scenario data from Phase-2 monitoring application
</div>

</div>

<script>

async function load(){

const r=await fetch("/phase2/scenarios");
const d=await r.json();
const s=d.scenarios;

document.getElementById("count").innerText=s.length;
document.getElementById("critical").innerText=
s.filter(x=>x.severity==="Critical").length;
document.getElementById("high").innerText=
s.filter(x=>x.severity==="High").length;

document.getElementById("grid").innerHTML=s.map(x=>`

<div class="incident">

<div class="head">
<div class="name">${x.scenario}</div>
<div class="badge ${x.severity==="Critical"?"critical":"high"}">
${x.severity.toUpperCase()}
</div>
</div>

<div class="row">
<div class="key">Monitored Metric</div>
<div class="value">${x.metric}</div>
</div>

<div class="row">
<div class="key">Predicted Condition</div>
<div class="value pred">${x.prediction}</div>
</div>

<div class="row">
<div class="key">Estimated Lead Time</div>
<div class="value">${x.lead_time}</div>
</div>

</div>

`).join("");

}

load();
setInterval(load,30000);

</script>

</body>
</html>
"""

    return render_template_string(INCIDENT_HTML)

@phase2_ui.route("/phase2/regression-ui")
def regression_ui():

    REGRESSION_HTML = r"""
<!DOCTYPE html>
<html>
<head>

<title>Final Regression Validation</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #0b1120;
    color: #e5e7eb;
    font-family: Arial, Helvetica, sans-serif;
}

.topbar {
    height: 72px;
    background: #111827;
    border-bottom: 1px solid #263244;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 34px;
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
    font-size: 20px;
}

.title {
    font-size: 20px;
    font-weight: 700;
}

.subtitle {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 3px;
}

.status {
    color: #4ade80;
    border: 1px solid #1f6b43;
    background: #10251b;
    padding: 8px 15px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
}

.container {
    max-width: 1450px;
    margin: auto;
    padding: 34px 36px 50px;
}

.heading {
    display: flex;
    justify-content: space-between;
    align-items: end;
    margin-bottom: 25px;
}

h1 {
    margin: 0;
    font-size: 28px;
}

.description {
    margin-top: 7px;
    color: #94a3b8;
    font-size: 13px;
}

.timestamp {
    color: #94a3b8;
    font-size: 12px;
}

.summary {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-bottom: 28px;
}

.card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 14px;
    padding: 20px;
}

.label {
    color: #94a3b8;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: .8px;
}

.number {
    font-size: 32px;
    font-weight: 700;
    margin-top: 9px;
}

.green {
    color: #4ade80;
}

.red {
    color: #ef4444;
}

.section-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 15px;
}

.tests {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 14px;
    overflow: hidden;
}

.test {
    display: grid;
    grid-template-columns: 55px 1fr 130px;
    align-items: center;
    min-height: 72px;
    padding: 0 24px;
    border-bottom: 1px solid #263244;
}

.test:last-child {
    border-bottom: none;
}

.check {
    width: 27px;
    height: 27px;
    border-radius: 50%;
    background: #12351f;
    color: #4ade80;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}

.test-name {
    font-size: 15px;
    font-weight: 600;
}

.test-description {
    color: #94a3b8;
    font-size: 11px;
    margin-top: 4px;
}

.result {
    text-align: right;
    color: #4ade80;
    font-size: 12px;
    font-weight: 700;
}

.final {
    margin-top: 25px;
    background: #10251b;
    border: 1px solid #1f6b43;
    border-radius: 14px;
    padding: 22px;
    text-align: center;
}

.final-title {
    color: #4ade80;
    font-size: 22px;
    font-weight: 700;
}

.final-text {
    color: #94a3b8;
    margin-top: 7px;
    font-size: 13px;
}

.footer {
    text-align: right;
    color: #64748b;
    font-size: 11px;
    margin-top: 30px;
}

</style>
</head>

<body>

<div class="topbar">

    <div class="brand">

        <div class="logo">AI</div>

        <div>
            <div class="title">
                AI Predictive Infrastructure Monitoring
            </div>

            <div class="subtitle">
                Automated Quality Assurance & Regression Validation
            </div>
        </div>

    </div>

    <div class="status">
        ● Regression Validation Active
    </div>

</div>


<div class="container">

    <div class="heading">

        <div>

            <h1>Final Regression Validation</h1>

            <div class="description">
                Live validation of Phase-2 monitoring and prediction services
            </div>

        </div>

        <div class="timestamp" id="timestamp">
            Running validation...
        </div>

    </div>


    <div class="summary">

        <div class="card">
            <div class="label">Total Tests</div>
            <div class="number" id="total">--</div>
        </div>

        <div class="card">
            <div class="label">Passed</div>
            <div class="number green" id="passed">--</div>
        </div>

        <div class="card">
            <div class="label">Failed</div>
            <div class="number red" id="failed">--</div>
        </div>

        <div class="card">
            <div class="label">Suite Status</div>
            <div class="number green" id="suite">RUNNING</div>
        </div>

    </div>


    <div class="section-title">
        Regression Test Results
    </div>


    <div class="tests" id="tests">

        <div class="test">
            <div></div>
            <div>Running live regression checks...</div>
            <div></div>
        </div>

    </div>


    <div class="final">

        <div class="final-title" id="finalTitle">
            VALIDATING
        </div>

        <div class="final-text" id="finalText">
            Executing live application checks...
        </div>

    </div>


    <div class="footer">
        Results generated from live Phase-2 application endpoints
    </div>

</div>


<script>

async function runRegression() {

    try {

        const response =
            await fetch("/phase2/regression");

        const data =
            await response.json();

        document.getElementById("total").innerText =
            data.total;

        document.getElementById("passed").innerText =
            data.passed;

        document.getElementById("failed").innerText =
            data.failed;

        document.getElementById("timestamp").innerText =
            new Date(data.timestamp).toLocaleString();

        document.getElementById("suite").innerText =
            data.status;

        if (data.status === "PASSED") {

            document.getElementById("suite").className =
                "number green";

            document.getElementById("finalTitle").innerText =
                "✓ REGRESSION SUITE PASSED";

            document.getElementById("finalText").innerText =
                data.passed + " of " + data.total +
                " live validation checks completed successfully.";

        } else {

            document.getElementById("suite").className =
                "number red";

            document.getElementById("finalTitle").innerText =
                "REGRESSION ISSUES DETECTED";

            document.getElementById("finalText").innerText =
                "Review failed checks before final validation.";

        }


        document.getElementById("tests").innerHTML =
            data.tests.map(t => `

                <div class="test">

                    <div class="check">
                        ✓
                    </div>

                    <div>

                        <div class="test-name">
                            ${t.name}
                        </div>

                        <div class="test-description">
                            ${t.description}
                        </div>

                    </div>

                    <div class="result">
                        ${t.result}
                    </div>

                </div>

            `).join("");

    }

    catch(error) {

        document.getElementById("suite").innerText =
            "ERROR";

        document.getElementById("suite").className =
            "number red";

        document.getElementById("finalTitle").innerText =
            "VALIDATION ERROR";

        document.getElementById("finalText").innerText =
            "Unable to execute live regression validation.";

    }

}

runRegression();

setInterval(runRegression, 30000);

</script>

</body>
</html>
"""

    return render_template_string(REGRESSION_HTML)


@phase2_ui.route("/phase2/regression")
def regression():

    import urllib.request
    from datetime import datetime

    checks = [
        (
            "Health Endpoint",
            "Monitoring application health endpoint",
            "/health"
        ),
        (
            "Prediction Engine",
            "Memory, CPU and database prediction service",
            "/phase2/predictions"
        ),
        (
            "Risk Dashboard",
            "Predicted infrastructure risk calculation",
            "/phase2/risk"
        ),
        (
            "Alert Classification",
            "Infrastructure alert classification service",
            "/phase2/classification"
        ),
        (
            "Incident Scenarios",
            "Five controlled incident scenarios",
            "/phase2/scenarios"
        ),
        (
            "End-to-End Pipeline",
            "Complete Phase-2 monitoring pipeline",
            "/phase2/e2e"
        )
    ]

    results = []

    for name, description, endpoint in checks:

        try:

            url = "http://127.0.0.1:5000" + endpoint

            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Phase2-Regression"}
            )

            with urllib.request.urlopen(req, timeout=10) as response:

                code = response.status

                if code == 200:

                    results.append({
                        "name": name,
                        "description": description,
                        "result": "PASSED"
                    })

                else:

                    results.append({
                        "name": name,
                        "description": description,
                        "result": "FAILED"
                    })

        except Exception:

            results.append({
                "name": name,
                "description": description,
                "result": "FAILED"
            })

    passed = sum(
        1 for x in results if x["result"] == "PASSED"
    )

    failed = len(results) - passed

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total": len(results),
        "passed": passed,
        "failed": failed,
        "status": "PASSED" if failed == 0 else "FAILED",
        "tests": results
    }


@phase2_ui.route("/phase2/architecture-ui")
def architecture_ui():

    ARCH_HTML = r"""
<!DOCTYPE html>
<html>
<head>

<title>System Architecture</title>

<style>

*{box-sizing:border-box}

body{
margin:0;
background:#0b1120;
color:#e5e7eb;
font-family:Arial,Helvetica,sans-serif
}

.topbar{
height:72px;
background:#111827;
border-bottom:1px solid #263244;
display:flex;
align-items:center;
justify-content:space-between;
padding:0 34px
}

.brand{
display:flex;
align-items:center;
gap:14px
}

.logo{
width:42px;
height:42px;
border-radius:10px;
background:#2563eb;
display:flex;
align-items:center;
justify-content:center;
font-size:20px;
font-weight:bold
}

.title{
font-size:20px;
font-weight:700
}

.subtitle{
font-size:12px;
color:#94a3b8;
margin-top:3px
}

.status{
padding:8px 15px;
border-radius:20px;
border:1px solid #1f6b43;
background:#10251b;
color:#4ade80;
font-size:13px;
font-weight:600
}

.container{
max-width:1450px;
margin:auto;
padding:34px 36px 50px
}

.heading{
display:flex;
justify-content:space-between;
align-items:end;
margin-bottom:25px
}

h1{
margin:0;
font-size:28px
}

.desc{
margin-top:7px;
color:#94a3b8;
font-size:13px
}

.timestamp{
color:#94a3b8;
font-size:12px
}

.architecture{
background:#111827;
border:1px solid #263244;
border-radius:16px;
padding:30px;
margin-bottom:25px
}

.arch-title{
font-size:18px;
font-weight:700;
margin-bottom:25px
}

.flow{
display:flex;
align-items:center;
justify-content:center;
gap:10px;
flex-wrap:wrap
}

.node{
min-width:145px;
padding:18px 15px;
border:1px solid #334155;
background:#0f172a;
border-radius:12px;
text-align:center
}

.node-icon{
font-size:24px;
margin-bottom:8px
}

.node-name{
font-size:13px;
font-weight:700
}

.node-desc{
font-size:10px;
color:#94a3b8;
margin-top:5px
}

.arrow{
font-size:24px;
color:#60a5fa
}

.components{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:18px
}

.component{
background:#111827;
border:1px solid #263244;
border-radius:14px;
padding:20px
}

.component-title{
font-size:16px;
font-weight:700;
margin-bottom:12px
}

.component-status{
display:flex;
align-items:center;
gap:8px;
color:#4ade80;
font-size:12px;
font-weight:600;
margin-bottom:15px
}

.dot{
width:9px;
height:9px;
border-radius:50%;
background:#4ade80
}

.item{
padding:9px 0;
border-top:1px solid #263244;
font-size:12px;
color:#cbd5e1
}

.item:first-of-type{
border-top:none
}

.validation{
margin-top:25px;
background:#10251b;
border:1px solid #1f6b43;
border-radius:14px;
padding:22px;
text-align:center
}

.validation-title{
color:#4ade80;
font-size:20px;
font-weight:700
}

.validation-text{
color:#94a3b8;
font-size:12px;
margin-top:7px
}

.footer{
text-align:right;
color:#64748b;
font-size:11px;
margin-top:25px
}

</style>

</head>

<body>

<div class="topbar">

<div class="brand">

<div class="logo">AI</div>

<div>

<div class="title">
AI Predictive Infrastructure Monitoring
</div>

<div class="subtitle">
System Architecture & Component Integration
</div>

</div>

</div>

<div class="status">
● System Integration Active
</div>

</div>


<div class="container">

<div class="heading">

<div>

<h1>System Architecture</h1>

<div class="desc">
End-to-end infrastructure monitoring, prediction and risk analysis architecture
</div>

</div>

<div class="timestamp">
Live Phase-2 System
</div>

</div>


<div class="architecture">

<div class="arch-title">
End-to-End Monitoring Pipeline
</div>

<div class="flow">

<div class="node">
<div class="node-icon">🖥</div>
<div class="node-name">Infrastructure</div>
<div class="node-desc">Flask · Docker · PostgreSQL</div>
</div>

<div class="arrow">→</div>

<div class="node">
<div class="node-icon">📊</div>
<div class="node-name">Metric Collection</div>
<div class="node-desc">Prometheus exporters</div>
</div>

<div class="arrow">→</div>

<div class="node">
<div class="node-icon">🤖</div>
<div class="node-name">Prediction Engine</div>
<div class="node-desc">Memory · CPU · DB</div>
</div>

<div class="arrow">→</div>

<div class="node">
<div class="node-icon">⚠</div>
<div class="node-name">Risk Scoring</div>
<div class="node-desc">Predictive risk analysis</div>
</div>

<div class="arrow">→</div>

<div class="node">
<div class="node-icon">🔎</div>
<div class="node-name">Alert Classification</div>
<div class="node-desc">Failure categorization</div>
</div>

<div class="arrow">→</div>

<div class="node">
<div class="node-icon">📈</div>
<div class="node-name">Grafana</div>
<div class="node-desc">Monitoring dashboards</div>
</div>

</div>

</div>


<div class="components">


<div class="component">

<div class="component-title">
Infrastructure Layer
</div>

<div class="component-status">
<span class="dot"></span>
Operational
</div>

<div class="item">Flask Monitoring Application</div>
<div class="item">Docker Container Environment</div>
<div class="item">PostgreSQL Database</div>

</div>


<div class="component">

<div class="component-title">
Observability Layer
</div>

<div class="component-status">
<span class="dot"></span>
Operational
</div>

<div class="item">Prometheus Metrics</div>
<div class="item">cAdvisor Container Metrics</div>
<div class="item">PostgreSQL Exporter</div>
<div class="item">OpenTelemetry / Jaeger</div>

</div>


<div class="component">

<div class="component-title">
AI & Analytics Layer
</div>

<div class="component-status">
<span class="dot"></span>
Operational
</div>

<div class="item">Memory Prediction</div>
<div class="item">CPU Forecast</div>
<div class="item">Database Storage Prediction</div>
<div class="item">Alert Classification</div>

</div>


</div>


<div class="validation">

<div class="validation-title">
✓ End-to-End Architecture Operational
</div>

<div class="validation-text">
Infrastructure metrics flow through monitoring, predictive analysis,
risk scoring and classification before dashboard presentation.
</div>

</div>


<div class="footer">
Phase-2 architecture overview · AI Predictive Infrastructure Monitoring
</div>

</div>

</body>
</html>
"""

    return render_template_string(ARCH_HTML)

