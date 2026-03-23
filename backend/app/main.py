from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"AceWallet no ar!🚀"}