import uvicorn 


if __name__ == "__main":
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)