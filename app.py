@app.route('/webhook', methods=['POST'])
def webhook():
    print("---- NEW REQUEST ----")
    
    data = request.get_json(silent=True)
    print("JSON:", data)

    # Extract fields safely
    conversation_id = str(data.get("conversation_id", "unknown"))
    message = str(data.get("message", ""))
    timestamp = str(data.get("timestamp", ""))

    file_name = "conversations.txt"

    with open(file_name, "a", encoding="utf-8") as f:
        f.write(f"\n--- Conversation {conversation_id} ---\n")
        f.write(f"{timestamp}: {message}\n")

    return jsonify({"status": "ok"}), 200
