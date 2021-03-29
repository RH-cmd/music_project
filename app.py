from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template, url_for
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect
import simplejson as json

#################################################
# Database Setup
#################################################

connection_string = "postgres:postgres@localhost:5432/music_project"
engine = create_engine(f'postgresql://{connection_string}', echo=False)
connection = engine.connect()

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################


# Either we use float for the values or use the simplejson
@app.route('/')
def home():
    return render_template("index.html")
    # return """<html>
    # <h1>Spotify Top Tracks App</h1>
    # <p><strong>All Available Routes:</strong></p>
    # <li>Sunburst and Bubble Chart Datasets: <a href="/sunburstbubble">/sunburstbubble</a></li>
    # <br>
    # <li>Heatmap Dataset: <a href="/heatmap">/heatmap</a></li>
    # <br>
    # <li>Bar Dataset: <a href="/bar">/bar</a></li>
    # </html"""

@app.route('/sunburstbubble')
def sunbubblevalues():
    result = connection.execute("""SELECT * FROM data_cleaned;""")
    print(result)
    data = []
    for row in result:
        my_dict = {
            "title":row[0],
            "artist": row[1],
            "genre": row[2],
            "genre_num": row[3],
            "subgenre": row[4],
            "year": row[5],
            "bpm": row[6],
            "nrgy": row[7],
            "dnce": row[8],
            "dB": row[9],
            "live": row[10],
            "val": row[11],
            "dur": row[12],
            "acous": row[13],
            "spch": row[14],
            "pop": row[15]
        }
        data.append(my_dict)
        print(row)
    data.append({'columns': ["title", "artist", "genre", "genre_num", "subgenre", "year", "bpm", "nrgy", "dnce", "dB", "live", "val", "dur", "acous", "spch", "pop"]})
    return(jsonify(data))

@app.route('/heatmap')
def heatmapvalues():
    result = connection.execute("""SELECT * FROM corr_heatmap_vals;""")
    data = []
    for row in result:
        my_dict = {
            "feat1":row[0],
            "feat2": row[1],
            "vals": row[2]
        }
        data.append(my_dict)
        print(row)
    return(jsonify(data))

@app.route('/bar')
def barvalues():
    result = connection.execute("""SELECT * FROM year_table;""")
    data = []
    for row in result:
        my_dict = {
            "year":row[0],
            "nrgy": row[1],
            "dnce": row[2],
            "val": row[3],
            "pop": row[4]
        }
        data.append(my_dict)
        print(row)
    return(jsonify(data))


if __name__ == "__main__":
    app.run(debug=True)