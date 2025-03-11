from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

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

@app.delete("/stashes/{stash_id}")
def delete_stash(stash_id: int, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM stash WHERE id = ?", (stash_id,))
    db.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Stash not found")
    
    return {"message": "Stash deleted successfully"}

@app.put("/stashes/{stash_id}")
def update_stash(stash_id: int, stash: Stash, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("UPDATE stash SET name = ?, location = ? WHERE id = ?", (stash.name, stash.location, stash_id))
    db.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Stash not found")
    
    return {"message": "Stash updated successfully", "id": stash_id, **stash.dict()}

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

@app.delete("/kits/{kit_id}")
def delete_kit(kit_id: int, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM kit WHERE id = ?", (kit_id,))
    db.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Kit not found")
    
    return {"message": "Kit deleted successfully"}

@app.put("/kits/{kit_id}")
def update_kit(kit_id: int, kit: Kit, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("UPDATE kit SET name = ?, stash_id = ? WHERE id = ?", (kit.name, kit.stash_id, kit_id))
    db.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Kit not found")
    
    return {"message": "Kit updated successfully", "id": kit_id, **kit.dict()}

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

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM item WHERE id = ?", (item_id,))
    db.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"message": "Item deleted successfully"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("UPDATE item SET name = ?, minecraft_item = ?, kit_id = ?, count = ? WHERE id = ?", 
                   (item.name, item.minecraft_item, item.kit_id, item.count, item_id))
    db.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"message": "Item updated successfully", "id": item_id, **item.dict()}

uvicorn.run(app, host="0.0.0.0", port=8000)
