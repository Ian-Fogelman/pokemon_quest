import os
import duckdb
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Place MP3 files in static/music/ to make them available as music options.
# The three preset tracks the game expects:
#   static/music/town.mp3       — calm/town vibe
#   static/music/battle.mp3     — upbeat/battle vibe
#   static/music/adventure.mp3  — exploration/adventure vibe
#
# Good sources for free CC-licensed game music:
#   https://opengameart.org  (search "pokemon", "chiptune", "town", "battle")
#   https://filmmusic.io     (Kevin MacLeod — search "hero", "adventure", "chiptune")

MUSIC_FOLDER = os.path.join(app.static_folder, "music")
os.makedirs(MUSIC_FOLDER, exist_ok=True)

AUDIO_EXTENSIONS = {"mp3", "ogg", "wav", "m4a"}


@app.route("/")
@app.route("/pokemon-quest")
def pokemon_quest():
    con = duckdb.connect("pokemon_quest.duckdb")
    rows = con.execute("SELECT * FROM pokemon ORDER BY id").df().to_dict("records")
    con.close()
    html = open("pokemon_quest.html", encoding="utf-8").read()
    return render_template_string(html, pokemon=rows)


@app.route("/music-list")
def music_list():
    """Returns any extra MP3s placed in static/music/ beyond the three presets."""
    files = []
    if os.path.exists(MUSIC_FOLDER):
        files = [
            {"name": fname, "url": f"/static/music/{fname}"}
            for fname in sorted(os.listdir(MUSIC_FOLDER))
            if "." in fname and fname.rsplit(".", 1)[1].lower() in AUDIO_EXTENSIONS
        ]
    return jsonify(files)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
