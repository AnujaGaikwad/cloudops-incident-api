from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "notification-service"
    })


@app.route("/notify", methods=["POST"])
def notify():

    incident = request.get_json()

    print("\n" + "=" * 40)
    print("🚨 NEW INCIDENT")
    print("=" * 40)

    print(f"ID: {incident.get('id')}")
    print(f"Title: {incident.get('title')}")
    print(f"Severity: {incident.get('severity')}")
    print(f"Status: {incident.get('status')}")

    print("Notification processed successfully.")
    print("=" * 40 + "\n")

    return jsonify({
        "message": "Notification processed successfully",
        "incident_id": incident.get("id")
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )