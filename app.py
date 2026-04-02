from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook is live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("---- NEW REQUEST ----")
    
    data = request.get_json(silent=True)
    print("JSON:", data)

    # Extract main info
    session_id = data.get("session", {}).get("external_id", "unknown")
    phone = data.get("user", {}).get("cellphone", "unknown")
    if data.get("event_type") != "session.close":
    return jsonify({"status": "ignored"}), 200

messages = data.get("messages", [])

    file_name = "conversations.txt"

    try:
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(f"\n\n=== Conversation {session_id} ({phone}) ===\n")

            for msg in messages:
                sender = msg.get("sender")
                text = msg.get("text", {}).get("message", "")
                time = msg.get("created_at")

                f.write(f"{time} | {sender}: {text}\n")

        print("✅ Conversation saved successfully")

    except Exception as e:
        print("❌ Error writing file:", str(e))

    return jsonify({"status": "ok"}), 200


# 👇 TEMPORARY: View file in browser
@app.route('/view')
def view():
    try:
        with open("conversations.txt", "r", encoding="utf-8") as f:
            content = f.read()
            return f"<pre>{content}</pre>"
    except:
        return "No file found yet."


if __name__ == "__main__":
    app.run()
