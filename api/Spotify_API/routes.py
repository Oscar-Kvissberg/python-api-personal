from fastapi import APIRouter, HTTPException, Query
import requests
import os

router = APIRouter(prefix="/spotify", tags=["Spotify"])

SPOTIFY_TOKEN = os.getenv("SPOTIFY_TOKEN", "DIN_SPOTIFY_ACCESS_TOKEN")

@router.get("/analyze")
async def analyze_track(track_id: str = Query(..., description="Spotify track ID")):
    headers = {"Authorization": f"Bearer {SPOTIFY_TOKEN}"}
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail="Spotify API error")
    data = resp.json()
    return {
        "tempo": data.get("tempo"),
        "energy": data.get("energy"),
        "danceability": data.get("danceability"),
        "track_id": track_id
    } 