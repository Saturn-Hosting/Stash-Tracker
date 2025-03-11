from fastapi import FastAPI, HTTPException, Depends
import sqlite3
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

def get_db():
    conn = sqlite3.connect("stash_tracker.db")
    conn.row_factory = sqlite3.Row
    return conn

class Stash(BaseModel):
    name: str
    location: str

class Kit(BaseModel):
    name: str
    stash_id: int

class Item(BaseModel):
    name: Optional[str] = None
    minecraft_item: str
    kit_id: int
    count: int

@app.post("/stashes/")
def create_stash(stash: Stash, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("INSERT INTO stash (name, location) VALUES (?, ?)", (stash.name, stash.location))
    db.commit()
    return {"id": cursor.lastrowid, **stash.dict()}

@app.get("/stashes/", response_model=List[dict])
def get_stashes(db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM stash")
    return [dict(row) for row in cursor.fetchall()]

@app.post("/kits/")
def create_kit(kit: Kit, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("INSERT INTO kit (name, stash_id) VALUES (?, ?)", (kit.name, kit.stash_id))
    db.commit()
    return {"id": cursor.lastrowid, **kit.dict()}

@app.get("/kits/", response_model=List[dict])
def get_kits(db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM kit")
    return [dict(row) for row in cursor.fetchall()]

@app.post("/items/")
def create_item(item: Item, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("INSERT INTO item (name, minecraft_item, kit_id, count) VALUES (?, ?, ?, ?)", (item.name, item.minecraft_item, item.kit_id, item.count))
    db.commit()
    return {"id": cursor.lastrowid, **item.dict()}

@app.get("/items/", response_model=List[dict])
def get_items(db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM item")
    return [dict(row) for row in cursor.fetchall()]

uvicorn.run(app, host="0.0.0.0", port=8000)
