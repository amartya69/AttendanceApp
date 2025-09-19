from fastapi import FastAPI

app = FastAPI()  # This is your FastAPI app

@app.get("/")
def read_root():
    return {"message": "Hello World"}
