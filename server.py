from fastapi import FastAPI, WebSocket
from starlette.responses import FileResponse 
from functions.predict import predict

app = FastAPI()

@app.get("/")
async def home():
    return FileResponse('./frontend/index.html')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
        except Exception as e:
            print("error: ", e)
        prediction = predict(data)
        await websocket.send_json(prediction)
        # await websocket.send_text(message)
