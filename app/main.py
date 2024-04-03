#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# from models import Item
import json
import requests

import os
import MySQLdb
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html = True), name="static")

HOST = os.environ.get('DBHOST')
USER = os.environ.get('DBUSER')
PASS = os.environ.get('DBPASS')
DB = "rde6mn"

# The URL for this API has a /docs endpoint that lets you see and test
# your various endpoints/methods.

#This shows all albums
@app.get("/albums")
def get_all_albums():
    db = MySQLdb.connect(host=HOST, user=USER, passwd=PASS, db=DB)
    c = db.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT * FROM albums ORDER BY name")
    results = c.fetchall()
    db.close()
    return results

#This shows one album by id. Commented out to run first code block separatley

#@app.get("/albums/{id}")
#def get_one_album(id):
#    db = MySQLdb.connect(host=HOST, user=USER, passwd=PASS, db=DB)
#    c = db.cursor(MySQLdb.cursors.DictCursor)
#    c.execute("SELECT * FROM albums WHERE id=" + id)
#    results = c.fetchall()
#    db.close()
#    return results
    
