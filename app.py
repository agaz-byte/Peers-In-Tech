from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(_name_)

# Load phone data from JSON file
with open("phones.json", "r") as f:
    phone_data = json.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("phone_name").lower()
        results = []

        # Search for matching phones (brand or model)
        for phone in phone_data:
            if query in phone["brand"].lower() or query in phone["model"].lower():
                results.append(phone)

        return render_template("result.html", results=results, query=query)

    return render_template("index.html")

if _name_ == "_main_":
    app.run(debug=True)