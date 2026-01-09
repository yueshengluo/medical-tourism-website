#!/bin/bash

# Chengdu Medical Tourism Demo Website Startup Script

echo "🏥 Starting Chengdu Medical Tourism Demo Website..."
echo ""

# Change to the demo-website directory
cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first:"
    echo "   python3 -m venv venv"
    echo "   source venv/bin/activate"
    echo "   pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment and start the server
echo "🚀 Activating virtual environment and starting FastAPI server..."
source venv/bin/activate
python main.py

echo ""
echo "🏥 Server stopped. Thank you for using Chengdu Medical Tourism Demo!"