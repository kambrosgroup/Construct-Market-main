#!/bin/bash
# Start the FastAPI backend server on localhost:8000

echo "Starting ConstructMarket Backend Server..."
echo "Server will run on http://localhost:8000"
echo "API docs available at http://localhost:8000/docs"
echo ""

cd /Users/karlambrosius/Documents/Construct-Market-main/backend
uvicorn server:app --reload --port 8000
