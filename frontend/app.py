from flask import Flask, render_template, request, redirect, jsonify
import requests
import os

app = Flask(__name__)

API_URL = os.getenv("API_URL", "http://localhost:5000")


@app.route("/")
def dashboard():
    api_online = True

    try:
        response = requests.get(f"{API_URL}/incidents", timeout=3)
        response.raise_for_status()
        incidents = response.json()
    except requests.exceptions.RequestException:
        incidents = []
        api_online = False

    total = len(incidents)
    open_count = sum(1 for i in incidents if i.get("status") == "OPEN")
    resolved_count = sum(1 for i in incidents if i.get("status") == "RESOLVED")
    critical_count = sum(1 for i in incidents if i.get("severity") == "CRITICAL")
    high_count = sum(1 for i in incidents if i.get("severity") == "HIGH")
    medium_count = sum(1 for i in incidents if i.get("severity") == "MEDIUM")
    low_count = sum(1 for i in incidents if i.get("severity") == "LOW")

    return render_template(
        "index.html",
        incidents=incidents,
        total=total,
        open_count=open_count,
        resolved_count=resolved_count,
        critical_count=critical_count,
        high_count=high_count,
        medium_count=medium_count,
        low_count=low_count,
        api_online=api_online,
    )


@app.route("/create", methods=["POST"])
def create_incident():
    payload = {
        "title": request.form.get("title", "").strip(),
        "severity": request.form.get("severity", "MEDIUM"),
    }

    try:
        requests.post(f"{API_URL}/incidents", json=payload, timeout=3)
    except requests.exceptions.RequestException:
        pass

    return redirect("/")


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "frontend"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
