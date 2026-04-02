@app.route('/webhook', methods=['POST'])
def webhook():
    print("---- NEW REQUEST ----")
    
    data = request.get_json(silent=True)
    raw = request.data

    print("JSON:", data)
    print("RAW:", raw)

    return jsonify({"status": "ok"}), 200
