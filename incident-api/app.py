from flask import Flask, jsonify, request
import requests
import uuid
import os

app = Flask(__name__)

# Notification service URL
# Local development: http://localhost:5001
# Docker Compose will override this with:
# http://notification-service:5001
NOTIFICATION_URL = os.getenv(
    "NOTIFICATION_URL",
    "http://localhost:5001"
)

incidents = []


# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "incident-api"
    })


# -----------------------------
# GET ALL INCIDENTS
# -----------------------------
@app.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify(incidents)


# -----------------------------
# CREATE INCIDENT
# -----------------------------
@app.route("/incidents", methods=["POST"])
def create_incident():

    data = request.get_json()

    incident = {
        "id": "INC-" + str(uuid.uuid4())[:8],
        "title": data.get("title"),
        "severity": data.get("severity", "MEDIUM"),
        "status": "OPEN"
    }

    incidents.append(incident)

    # Send incident to Notification Service
    try:
        response = requests.post(
            f"{NOTIFICATION_URL}/notify",
            json=incident,
            timeout=2
        )

        print(
            f"Notification service response: "
            f"{response.status_code}"
        )

    except requests.exceptions.RequestException:
        print("Notification service unavailable")

    return jsonify(incident), 201


# -----------------------------
# GET SINGLE INCIDENT
# -----------------------------
@app.route("/incidents/<incident_id>", methods=["GET"])
def get_incident(incident_id):

    for incident in incidents:
        if incident["id"] == incident_id:
            return jsonify(incident)

    return jsonify({
        "error": "Incident not found"
    }), 404


# -----------------------------
# UPDATE INCIDENT
# -----------------------------
@app.route("/incidents/<incident_id>", methods=["PUT"])
def update_incident(incident_id):

    data = request.get_json()

    for incident in incidents:

        if incident["id"] == incident_id:

            incident["title"] = data.get(
                "title",
                incident["title"]
            )

            incident["severity"] = data.get(
                "severity",
                incident["severity"]
            )

            incident["status"] = data.get(
                "status",
                incident["status"]
            )

            return jsonify(incident)

    return jsonify({
        "error": "Incident not found"
    }), 404


# -----------------------------
# START APPLICATION
# -----------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )