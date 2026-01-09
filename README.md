# Chengdu Medical Tourism - Demo Website

A proof-of-concept website for medical tourism and wellness services connecting North American and European patients to medical facilities in Chengdu, China.

## Project Overview

This is a FastAPI-based demo website designed to:
- Explain the medical tourism concept and value proposition
- Showcase available services and processes
- Collect early interest data through contact forms
- Store inquiries in both SQLite database and CSV files

## Features

- **Clean, responsive design** using TailwindCSS
- **FastAPI backend** with Jinja2 templates
- **SQLite database** for structured data storage
- **CSV export** for easy data analysis
- **Contact form** with validation and confirmation
- **Multiple pages**: Landing, Services, Process, About, Contact

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

4. **Access the website:**
   Open your browser and navigate to: `http://localhost:8000`

## Project Structure

```
demo-website/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── medical_tourism.db     # SQLite database (created automatically)
├── inquiries.csv          # CSV export file (created automatically)
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── landing.html      # Homepage
│   ├── services.html     # Services overview
│   ├── process.html      # How it works
│   ├── about.html        # About the company
│   ├── contact.html      # Contact form
│   └── success.html      # Form submission confirmation
└── static/               # Static files (CSS, JS, images)
```

## Database Schema

The SQLite database contains an `inquiries` table with the following fields:
- `id` (Primary Key)
- `name` (Optional)
- `email` (Required)
- `country`
- `age_range`
- `area_of_interest`
- `timeframe`
- `message`
- `created_at`

## API Endpoints

- `GET /` - Landing page
- `GET /services` - Services page
- `GET /process` - Process page
- `GET /about` - About page
- `GET /contact` - Contact form
- `POST /submit-inquiry` - Form submission handler

## Contact Form Fields

- **Name**: Optional text field
- **Email**: Required email field
- **Country**: Dropdown with major target countries
- **Age Range**: Dropdown (Under 30, 30-40, 41-50, 51-60, 61-70, Over 70)
- **Area of Interest**: Dropdown with medical services
- **Timeframe**: Dropdown for treatment timeline
- **Message**: Optional textarea for additional information

## Design Features

- Mobile-responsive design
- Healthcare-appropriate color scheme
- Font Awesome icons
- Hover effects and smooth transitions
- Professional layout suitable for medical services
- TailwindCSS for rapid styling

## Data Storage

All form submissions are stored in two formats:
1. **SQLite Database**: Structured storage for application queries
2. **CSV File**: Simple export format for data analysis

## Development Notes

- This is a proof-of-concept for demonstration purposes
- No user authentication or admin panel included
- Minimal JavaScript - focus on server-side rendering
- Form validation handled by FastAPI
- Responsive design works on mobile and desktop

## Customization

To customize the website:
1. Modify templates in the `templates/` directory
2. Update styling by editing TailwindCSS classes
3. Add new routes in `main.py`
4. Extend database schema as needed

## Future Enhancements

Potential additions for a production version:
- Admin dashboard for managing inquiries
- User authentication and patient portals
- Payment processing integration
- Multi-language support
- Advanced form validation
- Email notification system
- Integration with CRM systems

## Support

For questions or issues with this demo, please contact the development team.