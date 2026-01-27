# Backend Setup and Migration Script

Write-Host "=== DB Assistant Backend Setup ===" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check if old Backend .env exists
Write-Host "Step 1: Checking for existing .env file..." -ForegroundColor Yellow
if (Test-Path "..\Backend\.env") {
    Write-Host "✅ Found .env in old Backend" -ForegroundColor Green
    Write-Host "Copying to Backend_New..." -ForegroundColor Yellow
    Copy-Item "..\Backend\.env" ".env"
    Write-Host "✅ .env copied successfully" -ForegroundColor Green
} else {
    Write-Host "⚠️  No .env found in old Backend" -ForegroundColor Red
    Write-Host "Please create .env from .env.example and configure:" -ForegroundColor Yellow
    Write-Host "  - OPENAI_API_KEY" -ForegroundColor White
    Write-Host "  - DB_HOST, DB_USER, DB_PASSWORD, DB_NAME" -ForegroundColor White
    exit 1
}

Write-Host ""

# Step 2: Install dependencies
Write-Host "Step 2: Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""

# Step 3: Verify installation
Write-Host "Step 3: Verifying installation..." -ForegroundColor Yellow
python -c "import fastapi, langchain, langgraph, psycopg2; print('✅ All core packages installed')"

Write-Host ""

# Step 4: Start server
Write-Host "Step 4: Starting FastAPI server..." -ForegroundColor Yellow
Write-Host "Server will start on http://localhost:8000" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
Write-Host ""

python main.py
