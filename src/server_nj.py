from fastapi import FastAPI

app = FastAPI ( title = "New Jersey API Server")

@app.get("/warehouse/{product}")
async def load_truck(product, order_qty):
    return {
        "product": "product",
        "order_qty" : order_qty,
        "units": catalog["product"]["units"]
    }
    
catalog = {
    "tomatoes" : {
        "units" : "boxes",
        "qty" : 1000
    },
    "wine": {
        "units" : "bottles",
        "qty" : 500
    }
}