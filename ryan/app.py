import os 
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# EDIT --> proper engine + .env is needed
engine = create_engine("GOOD PATH HERE", echo=False)
Base = automap_base()
Base.prepare(engine, reflect=True)

# EDIT --> load proper tables 
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route('/')
def dashboard():
    return make_response()
