import uvicorn

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 6050
    uvicorn.run("neopay_api.api:app", host=host, port=port, reload=True)
