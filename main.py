from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI(
    title="FastAPI Lesson 2"
)


@app.get("/", response_class=FileResponse)
async def root():
    return FileResponse("index.html")
