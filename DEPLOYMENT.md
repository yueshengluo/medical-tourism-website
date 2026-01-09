# Deployment Guide for Render

## Step 1: Push to GitHub

1. Make sure your code is in a GitHub repository
2. Commit and push all files including the new `render.yaml`

```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

## Step 2: Deploy on Render

### Option A: Using Blueprint (Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New"** → **"Blueprint"**
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml` file
5. Click **"Apply"** to deploy

### Option B: Manual Setup

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the following:
   - **Name**: `medical-tourism-demo`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free (or your preferred plan)

5. Click **"Create Web Service"**

## Step 3: Wait for Deployment

- Render will build and deploy your application (takes 2-5 minutes)
- You'll get a URL like: `https://medical-tourism-demo.onrender.com`

## Step 4: View Your Data

### Access the Admin Dashboard

Once deployed, visit:
```
https://your-app-name.onrender.com/admin/inquiries
```

This page shows all form submissions from the SQLite database in a nice table format.

### Features:
- ✅ View all inquiries in real-time
- ✅ See submission details (name, email, country, interests, etc.)
- ✅ Sorted by most recent first
- ✅ Total count of submissions
- ✅ Clean, responsive table design

## Important Notes

### ⚠️ Database Persistence

**Free Render Plan**: The SQLite database file will be **reset** every time the service restarts or redeploys. This is because free tier services don't have persistent disk storage.

**Solutions**:
1. **Upgrade to Paid Plan** ($7/month) - Includes persistent disk storage
2. **Use Managed Database** - Add a PostgreSQL database on Render
3. **Export Data Regularly** - Download the CSV file or database before redeployments

### CSV File Location

The `inquiries.csv` file is stored on the server filesystem. To access it:
1. Go to your Render service dashboard
2. Click **"Shell"** tab
3. Run: `cat inquiries.csv` to view contents
4. Or download it using Render's file browser (paid plans only)

## Testing Locally Before Deployment

```bash
# Activate virtual environment
source venv/bin/activate

# Run the app
python main.py

# Test the admin page
open http://localhost:8000/admin/inquiries
```

## Troubleshooting

### Build Failed
- Check that `requirements.txt` is correct
- Verify Python version compatibility

### Service Won't Start
- Check Render logs in the dashboard
- Verify the start command is correct

### Database Empty After Restart
- This is expected on free plans
- Consider upgrading or using external database

## Security Recommendation

For production, add authentication to the `/admin/inquiries` endpoint to prevent public access to sensitive data.

Example: Add basic password protection or use Render's IP whitelisting feature.

## Next Steps

1. Test form submissions on your live site
2. Monitor the admin dashboard for inquiries
3. Consider adding email notifications when forms are submitted
4. Set up database backups if using persistent storage
