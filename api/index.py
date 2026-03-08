"""
Vercel Serverless Function Adapter for ConstructMarket API
This file adapts the FastAPI application for Vercel serverless deployment.
"""

import sys
import os
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_dir))

# Set environment variables for Vercel
os.environ.setdefault("DB_NAME", os.environ.get("DB_NAME", "constructmarket"))

# Import the FastAPI app from server.py
from server import app

# Mangum adapter for ASGI to WSGI
from mangum import Mangum

# Create the handler
handler = Mangum(app, lifespan="off")

# Vercel expects a specific handler function
def main(request):
    """Main entry point for Vercel serverless function"""
    return handler(request)
