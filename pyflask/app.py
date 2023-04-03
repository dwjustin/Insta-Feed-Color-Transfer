from flask import Flask, send_file

app = Flask(__name__)


@app.route("/image")
def image():
    # Send the image file to the client
    return send_file("image.jpg", mimetype="image/jpeg")


if __name__ == "__main__":
    app.run()
