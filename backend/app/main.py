from fastapi import FastAPI

from api.v1.routes import routers as routers_v1

app = FastAPI()
app.include_router(routers_v1)

@app.get("/")
async def root():
    return {"message": "travel agency backend"}