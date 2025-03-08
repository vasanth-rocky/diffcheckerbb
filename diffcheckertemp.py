from flask import Flask, request, jsonify
from difflib import SequenceMatcher

app = Flask(__name__)

def compare_texts(text1, text2):
    similarity = SequenceMatcher(None, text1, text2).ratio() * 100
    return round(similarity, 2)

@app.route("/compare", methods=["POST"])

def compare():
    data = request.json
    text1 = data.get("text1", "")
    text2 = data.get("text2", "")
    similarity = compare_texts(text1, text2)
    return jsonify({"similarity": similarity})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

