from fastapi import FastAPI, Request
from uvicorn import run
from config import HOST, PORT
from setup import system

#Application Initialized
app = FastAPI()

system.load_routers(app, {})

#Calling uvicorn to run when file is run using python command
if __name__ == "__main__":
    run(app, host=HOST, port=PORT)