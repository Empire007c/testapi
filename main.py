
from fastapi import FastAPI
import binance
import requests
import time
#import nest_asyncio
#from threading import Thread
from datetime import datetime

client = binance.Client()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/{symbol}/{limit}")
def get_data(symbol: str, limit: int):

    data = client.futures_klines(symbol=symbol, interval=client.KLINE_INTERVAL_1MINUTE, limit=5)
    data = [[26732.39, 26737.88, 26760.72, 26765.6, 26757.23], [26706.44, 26730.25, 26735.17, 26757.22, 26745.0], [26732.38, 26735.18, 26760.71, 26757.22, 26746.11]]

    url = "https://7e11-167-235-8-251.ngrok-free.app"
    path = "pattern1/"

    data = {"data": data, "ratio": 3}
    

    response = requests.post(url + path, json=data)
    return response.json()
      # Convert the response content to JSON and return it
