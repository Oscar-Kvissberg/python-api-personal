# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from api.Gbg_API.routes import router as gbg_router
from api.Hello.routes import router as hello_router
from api.Spotify_API.routes import router as spotify_router

app = FastAPI(
    title="Multi-API Server",
    description="API för Göteborgs hamn + andra endpoints",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#lägger till alla routs frpn gbg apiet... 
app.include_router(gbg_router)
app.include_router(hello_router)
app.include_router(spotify_router)

@app.get("/")
async def root():
    return {
        "message": "API är igång",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
