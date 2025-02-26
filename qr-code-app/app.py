from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO
import os

app = Flask(__name__)

# Define colors for different websites
COLORS = {
    "linkedin.com": (0, 119, 181),  # LinkedIn Blue
    "github.com": (36, 41, 46),     # GitHub Black
    "twitter.com": (29, 161, 242),  # Twitter Blue
    "facebook.com": (59, 89, 152)   # Facebook Blue
}

def get_qr_color(url):
    """Get the QR code color based on the URL."""
    for key, color in COLORS.items():
        if key in url:
            return color
    return (0, 0, 0)  # Default Black

@app.route("/", methods=["GET", "POST"])
def home():
    """Render the main page or generate a QR code."""
    if request.method == "POST":
        data = request.form["data"]
        qr_color = get_qr_color(data)

        # Generate QR Code
        qr = qrcode.QRCode(box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=qr_color, back_color="white")

        # Save QR code to static folder
        qr_path = os.path.join("static", "qrcode.png")
        img.save(qr_path)

        return render_template("result.html", qr_path=qr_path)

    return render_template("index.html")

@app.route("/download")
def download_qr():
    """Download the QR Code."""
    qr_path = os.path.join("static", "qrcode.png")
    return send_file(qr_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
