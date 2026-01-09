from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
import sqlite3
import csv
import os
from datetime import datetime
from typing import Optional
from contextlib import asynccontextmanager

# Database initialization
def init_db():
    conn = sqlite3.connect('medical_tourism.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT NOT NULL,
        country TEXT,
        age_range TEXT,
        area_of_interest TEXT,
        timeframe TEXT,
        message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

# Initialize CSV file
def init_csv():
    if not os.path.exists('inquiries.csv'):
        with open('inquiries.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Email', 'Country', 'Age Range', 'Area of Interest', 'Timeframe', 'Message', 'Created At'])

# Initialize database and CSV on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    init_csv()
    yield
    # Shutdown
    pass

app = FastAPI(
    title="Chengdu Medical Tourism", 
    description="Medical Tourism and Wellness in Chengdu, China",
    lifespan=lifespan
)

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes
@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/services", response_class=HTMLResponse)
async def services_page(request: Request):
    return templates.TemplateResponse("services.html", {"request": request})

@app.get("/process", response_class=HTMLResponse)
async def process_page(request: Request):
    return templates.TemplateResponse("process.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/admin/inquiries", response_class=HTMLResponse)
async def view_inquiries(request: Request):
    """Admin page to view all inquiries from the database"""
    try:
        conn = sqlite3.connect('medical_tourism.db')
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT id, name, email, country, age_range, area_of_interest, timeframe, message, created_at 
        FROM inquiries 
        ORDER BY created_at DESC
        ''')
        
        inquiries = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries for easier template rendering
        inquiries_list = []
        for row in inquiries:
            inquiries_list.append({
                'id': row[0],
                'name': row[1] or 'N/A',
                'email': row[2],
                'country': row[3] or 'N/A',
                'age_range': row[4] or 'N/A',
                'area_of_interest': row[5] or 'N/A',
                'timeframe': row[6] or 'N/A',
                'message': row[7] or 'N/A',
                'created_at': row[8]
            })
        
        return templates.TemplateResponse("admin_inquiries.html", {
            "request": request, 
            "inquiries": inquiries_list,
            "count": len(inquiries_list)
        })
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving inquiries: {str(e)}")

@app.post("/submit-inquiry")
async def submit_inquiry(
    request: Request,
    name: Optional[str] = Form(None),
    email: str = Form(...),
    country: Optional[str] = Form(None),
    age_range: Optional[str] = Form(None),
    area_of_interest: Optional[str] = Form(None),
    timeframe: Optional[str] = Form(None),
    message: Optional[str] = Form(None)
):
    try:
        # Save to SQLite
        conn = sqlite3.connect('medical_tourism.db')
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO inquiries (name, email, country, age_range, area_of_interest, timeframe, message)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, country, age_range, area_of_interest, timeframe, message))
        
        inquiry_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # Append to CSV
        with open('inquiries.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                inquiry_id, name, email, country, age_range, 
                area_of_interest, timeframe, message, 
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ])
        
        return templates.TemplateResponse("success.html", {"request": request, "name": name or "Friend"})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error submitting inquiry: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)