#!/bin/bash
# Build script for Vercel deployment

echo "Installing dependencies..."
yarn install

echo "Building frontend..."
yarn build

echo "Build complete!"
