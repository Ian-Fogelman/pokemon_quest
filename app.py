import os
import duckdb
from flask import Flask, render_template_string, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

MUSIC_FOLDER = os.path.join(app.static_folder, "music")
os.makedirs(MUSIC_FOLDER, exist_ok=True)

ALLOWED_AUDIO = {"mp3", "ogg", "wav", "m4a"}
MAX_UPLOAD_BYTES = 20 * 1024 * 1024  # 20 MB


def allowed_audio(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_AUDIO


@app.route("/")
@app.route("/pokemon-quest")
def pokemon_quest():
    con = duckdb.connect("pokemon_quest.duckdb")
    rows = con.execute("SELECT * FROM pokemon ORDER BY id").df().to_dict("records")
    con.close()
    html = open("pokemon_quest.html", encoding="utf-8").read()
    return render_template_string(html, pokemon=rows)


@app.route("/upload-music", methods=["POST"])
def upload_music():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    f = request.files["file"]
    if not f.filename:
        return jsonify({"error": "No file selected"}), 400
    if not allowed_audio(f.filename):
        return jsonify({"error": "Only audio files (mp3, ogg, wav, m4a) are allowed"}), 400
    if request.content_length and request.content_length > MAX_UPLOAD_BYTES:
        return jsonify({"error": "File too large (max 20 MB)"}), 413
    filename = secure_filename(f.filename)
    f.save(os.path.join(MUSIC_FOLDER, filename))
    return jsonify({"url": f"/static/music/{filename}", "name": filename})


@app.route("/music-list")
def music_list():
    files = []
    if os.path.exists(MUSIC_FOLDER):
        files = [
            {"name": fname, "url": f"/static/music/{fname}"}
            for fname in sorted(os.listdir(MUSIC_FOLDER))
            if "." in fname and fname.rsplit(".", 1)[1].lower() in ALLOWED_AUDIO
        ]
    return jsonify(files)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
