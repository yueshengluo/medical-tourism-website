# Quick Start Guide - Chengdu Medical Tourism Demo

## Overview
A complete medical tourism website demo built with FastAPI, featuring a professional healthcare design, contact forms with data collection, and SQLite database storage.

## Features
✅ **5 Main Pages**: Landing, Services, Process, About, Contact  
✅ **Responsive Design**: TailwindCSS with healthcare-appropriate styling  
✅ **Contact Form**: Collects leads with validation  
✅ **Dual Storage**: SQLite database + CSV export  
✅ **Professional UI**: Clean, modern design suitable for medical services  
✅ **Local Development**: Runs entirely on your machine  

## Quick Setup (3 Steps)

### Step 1: Setup Environment
```bash
cd demo-website
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
# Option A: Direct run
python main.py

# Option B: Use startup script
./start.sh
```

### Step 3: Open Website
Visit: **http://localhost:8000**

## Project Structure
```
demo-website/
├── main.py                    # FastAPI application
├── requirements.txt           # Dependencies
├── start.sh                   # Startup script
├── README.md                  # Detailed documentation
├── medical_tourism.db         # SQLite database (auto-created)
├── inquiries.csv             # CSV export (auto-created)
├── templates/                # HTML templates
│   ├── base.html            # Navigation & layout
│   ├── landing.html         # Homepage
│   ├── services.html        # Services overview
│   ├── process.html         # How it works
│   ├── about.html           # About us
│   ├── contact.html         # Contact form
│   └── success.html         # Form confirmation
├── static/                   # CSS/JS/Images (empty - using CDN)
└── venv/                     # Virtual environment
```

## Database Schema
**inquiries** table:
- `id` (Primary Key)
- `name` (Optional)
- `email` (Required)
- `country`, `age_range`, `area_of_interest`, `timeframe`
- `message` (Optional)
- `created_at` (Timestamp)

## Form Fields
- **Name**: Optional text
- **Email**: Required email validation
- **Country**: Dropdown (US, Canada, UK, Germany, etc.)
- **Age Range**: Dropdown (Under 30, 30-40, 41-50, 51-60, 61-70, Over 70)
- **Area of Interest**: Medical services dropdown
- **Timeframe**: When patient wants treatment
- **Message**: Optional additional details

## API Endpoints
- `GET /` → Landing page
- `GET /services` → Services overview
- `GET /process` → How it works
- `GET /about` → About us
- `GET /contact` → Contact form
- `POST /submit-inquiry` → Form handler

## Tech Stack
- **Backend**: FastAPI (Python)
- **Frontend**: Jinja2 templates + TailwindCSS (CDN)
- **Database**: SQLite
- **Icons**: Font Awesome
- **Styling**: TailwindCSS utility classes

## Customization Options
- **Colors**: Modify TailwindCSS classes in templates
- **Content**: Edit template files for text/images
- **Form Fields**: Add fields in contact.html and main.py
- **Database**: Extend schema in main.py init_db()
- **Styling**: Add custom CSS in static/ directory

## Data Access
- **SQLite Database**: Use any SQLite browser/tool
- **CSV File**: Open inquiries.csv in Excel/Sheets
- **API**: Access form data via FastAPI endpoints

## Production Notes
For production deployment, consider:
- Environment variables for sensitive data
- PostgreSQL instead of SQLite
- Email notifications for form submissions
- Admin dashboard for managing inquiries
- SSL certificates and domain setup
- User authentication if needed

## Support
This is a proof-of-concept demo. For production use, additional security, scalability, and feature enhancements would be recommended.