#!/bin/bash

# Installera dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Starta FastAPI appen med uvicorn
echo "Starting FastAPI application..."
uvicorn main:app --host 0.0.0.0 --port 8000 