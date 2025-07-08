# api/gbg/routes.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from .logic import GothenburgPortDataCollector

router = APIRouter(prefix="/api", tags=["Göteborgs Hamn"])
collector = GothenburgPortDataCollector()

@router.get("/port-data")
async def get_port_data():
    data = collector.collect_all_data()
    if data:
        return JSONResponse(content=data)
    raise HTTPException(status_code=500, detail="Failed to collect data")

@router.get("/container-availability")
async def get_container_availability():
    data = collector.get_container_availability()
    if data:
        return JSONResponse(content=data)
    raise HTTPException(status_code=500, detail="Failed to fetch container data")

@router.get("/port-queue")
async def get_port_queue():
    data = collector.get_port_queue()
    if data:
        return JSONResponse(content=data)
    raise HTTPException(status_code=500, detail="Failed to fetch queue data")

@router.get("/ships-in-port")
async def get_ships_in_port():
    data = collector.get_ships_in_port()
    if data:
        return JSONResponse(content=data)
    raise HTTPException(status_code=500, detail="Failed to fetch ships data")

@router.get("/weekly-data")
async def get_weekly_data():
    data = collector.get_weekly_data()
    if data:
        return JSONResponse(content=data)
    raise HTTPException(status_code=500, detail="Failed to fetch weekly data")
