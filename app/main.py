from fastapi import FastAPI, Request

app = FastAPI()

@app.get ("/rooms")
def get_rooms():
    rooms = [
        {"room number": 100,
        "room type": "single",
        "price": 75},
        {"room number": 101,
        "room type": "double",
        "price": 100},
        {"room number": 102,
        "room type": "suite",
        "price": 150}
]

@app.get("/api/rooms")
def get_rooms():
    return rooms

@app.get("/")
def read_root():
    return {"msg": "Hi, yelloooo!"}
@app.get("/api/ip")
def get_ip(request: Request):
    return {"ip": request.client.host}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"id": item_id, "q": q}
