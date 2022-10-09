import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def start():
    return 'hello world build from github'

if __name__ == "__main__":
    uvicorn.run("app:app",host = '0.0.0.0', port=5000)
