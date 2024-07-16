from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["data"]
        result = summarize_text(data)
        print(result)
        return render_template("index.html", result=result, data=data)
    else:
        return render_template("index.html")


def summarize_text(text):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "Bearer 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"}
    max_length = 500
    min_length = max_length // 4

    payload = {
        "inputs": text,
        "parameters": {"min_length": min_length, "max_length": max_length},
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        response_json = response.json()
    # Print the JSON response
        if response_json and isinstance(response_json, list) and "summary_text" in response_json[0]:
            return response_json[0]["summary_text"]
        else:
            return "Error: Summary text not found in the response."
    else:
        return f"Error: Failed to fetch summary. Status code: {response.status_code}"



if __name__ == "__main__":
    app.run(debug=True)
