from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Tyre Prediction Service is Running!"}
