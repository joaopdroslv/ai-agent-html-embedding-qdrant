import uvicorn
from fastapi import FastAPI

from app.routers import chat

app = FastAPI()

app.include_router(chat.router)


@app.get("/")
async def root():
    return {"message": "API is running."}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
