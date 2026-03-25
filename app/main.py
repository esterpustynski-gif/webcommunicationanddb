from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Yelloooo!"}
@app.get("/api/ip")
def get_ip(request: Request):
    return {"ip": request.client.host}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"id": item_id, "q": q}