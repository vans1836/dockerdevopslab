from fastapi import FastAPI
app = FastAPI()
import uvicorn
@app.get("/")
def read_root():
    return dict(name = "Tushar", Location = "Dehradun")
@app.get("/{data}")
def read_root(data):
    return dict(hi = data, Location = "Dehradun")

if _name_ == "_main_":
    uvicorn.run("main:app", host="0.0.0.0", port=8088, reload=True)