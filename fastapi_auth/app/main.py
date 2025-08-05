from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel
from request_validators import LoginRequest, RegisterRequest

def create_application():
    application = FastAPI()
    return application


app = create_application()


@app.get("/")
async def root():
    return {"message": "Hi, I am Describly. Awesome - Your setrup is done & working."}
    
@app.post("/auth/login")
async def login_handler(request: LoginRequest):
    return {"message": "Login successful", "data": request.model_dump()}


@app.post("/auth/register")
async def register_handler(request: RegisterRequest):
    print(request.email, request.username, request.password)
    return 5

if __name__ == "__main__":
    uvicorn.run("main:app", port=3000, log_level="info", reload=True)
