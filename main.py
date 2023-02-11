from fastapi import FastAPI
from loguru import logger

app = FastAPI()
logger.add("app_logs/requests.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
@app.get("/")
def root():
    # loguru.logger.info("This is a log message")
    logger.debug("That's it, beautiful and simple logging!")
    return {"message": "Hello World"}


if __name__ == "__main__":
    logger.info("Starting server...")
