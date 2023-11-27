
from fastapi import FastAPI
import binance
import requests
client = binance.Client()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/{symbol}/{limit}")
def get_data(symbol: str, limit: int):

    data = client.get_klines(symbol=symbol, interval=client.KLINE_INTERVAL_1MINUTE, limit=5)
    data = [[26732.39, 26737.88, 26760.72, 26765.6, 26757.23], [26706.44, 26730.25, 26735.17, 26757.22, 26745.0], [26732.38, 26735.18, 26760.71, 26757.22, 26746.11]]

    '''url = "https://baa1-35-201-190-150.ngrok.io/"
    path = "pattern1/"

    data = {"data": data, "ratio": 3}
    print(data)

    response = requests.post(url + path, json=data)
    return response.json()'''
    return data
      # Convert the response content to JSON and return it
