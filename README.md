# Clue Quest 151

A fan-made Pokémon guessing game for kids, playable in the browser.

**[Play it here →](https://ianfogelman.pythonanywhere.com/pokemon-quest)**

---

## How to Play

Guess the mystery Pokémon from the first 151 using one of three game modes:

| Mode | How it works |
|---|---|
| **Clues** | Read up to 3 text clues, one revealed at a time |
| **Picture** | Identify the Pokémon from a blurry sprite that gets clearer with each guess |
| **Silhouette** | Guess from a solid black silhouette — just like the show. Wrong guesses unlock text clues |

Each wrong guess costs a life. Run out of guesses and the answer is revealed.

## Settings

- **Guesses per round** — 1 to 10 (default 3)
- **Answer mode** — Pick from 4 choices, or type the name
- **Sound effects** — Toggle the win/miss chimes

## Scoring

Your **Guessed**, **Streak**, and **Played** counts are saved in your browser across sessions. The game tracks which Pokémon you've seen so you won't get repeats until you've gone through all 151.

## Tech Stack

- Single-page HTML/CSS/JS frontend
- Pokémon data stored in [DuckDB](https://duckdb.org/)
- Served by a Flask app hosted on [PythonAnywhere](https://www.pythonanywhere.com)
- Background music generated live by the Web Audio API
- Sprites from the [PokéAPI](https://pokeapi.co/) sprite project

---

*Pokémon names and artwork belong to their respective owners. This is a fan project.*
