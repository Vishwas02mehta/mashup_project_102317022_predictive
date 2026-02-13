import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form.get("singer")
        videos = request.form.get("videos")
        duration = request.form.get("duration")
        email = request.form.get("email")

        return f"""
        <h2>Request Submitted Successfully ✅</h2>
        <p><b>Singer:</b> {singer}</p>
        <p><b>No. of Videos:</b> {videos}</p>
        <p><b>Duration:</b> {duration} seconds</p>
        <p><b>Email:</b> {email}</p>
        <p><i>Mashup generation is handled offline due to cloud restrictions.</i></p>
        """

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
