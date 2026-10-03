# README BIPM - Data Science module
This is a simple commit to do the assignment from the mail.

## Journey page

My introduction page for the BIPM course: **https://arslanchaudhry65.github.io/BIPM/**

| File | What it is |
|---|---|
| `index.html` | The page itself, built from `src/index.src.html` by `build.py` |
| `map.html` | The embedded map, built by `myJourney.ipynb` (folium + OpenStreetMap, no API key) |
| `myJourney.ipynb` | Notebook that builds the map; runs locally or in Google Colab |
| `images/portrait.jpg` | The portrait at the top of the page |
| `assets/plex.css` | IBM Plex fonts, embedded so the page needs no font host |

To change the text, edit `src/index.src.html` and run `python build.py`.
To change the map, edit the stops in `myJourney.ipynb` and run all cells.
