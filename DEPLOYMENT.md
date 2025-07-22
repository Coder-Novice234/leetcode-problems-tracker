# Hosting Your LeetCode Problems Tracker on GitHub

You have several options to host your Flask application on GitHub. Here are the most popular and practical approaches:

## Option 1: Heroku (Free Tier Available)

Heroku is one of the easiest platforms to deploy Flask applications:

### Steps:
1. **Create a Heroku account** at [heroku.com](https://heroku.com)

2. **Install Heroku CLI** on your local machine

3. **Initialize git repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Create Heroku app**:
   ```bash
   heroku create your-leetcode-tracker
   ```

5. **Deploy**:
   ```bash
   git push heroku main
   ```

Your app will be available at: `https://your-leetcode-tracker.herokuapp.com`

### Important Notes for Heroku:
- The `problems_data.json` file won't persist between deployments (Heroku uses ephemeral filesystem)
- Consider using Heroku PostgreSQL addon for persistent storage
- Files included: `Procfile`, `requirements.txt`, `runtime.txt`

## Option 2: Railway

Railway is a modern alternative to Heroku:

### Steps:
1. **Create account** at [railway.app](https://railway.app)
2. **Connect your GitHub repository**
3. **Deploy directly from GitHub**

Railway will automatically detect your Flask app and deploy it.

## Option 3: Render

Render offers free hosting for Flask applications:

### Steps:
1. **Create account** at [render.com](https://render.com)
2. **Connect GitHub repository**
3. **Create a new Web Service**
4. **Configure**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## Option 4: PythonAnywhere (Free Tier Available)

Great for Python web applications:

### Steps:
1. **Create account** at [pythonanywhere.com](https://pythonanywhere.com)
2. **Upload your code** via their file browser
3. **Create a web app** in the Web tab
4. **Configure WSGI file** to point to your Flask app

## Option 5: GitHub Pages + GitHub Actions (Static Alternative)

If you want to keep everything on GitHub, you could:
1. Convert the Flask app to generate static HTML files
2. Use GitHub Actions to build and deploy to GitHub Pages
3. This would require significant modifications to remove server-side functionality

## Recommended Approach: Heroku or Railway

For your use case, I recommend **Railway** or **Heroku** because:
- Easy deployment from GitHub
- Free tiers available
- Good for Flask applications
- Automatic deployments when you push to GitHub

## GitHub Repository Setup

1. **Create a new repository** on GitHub
2. **Push your code**:
   ```bash
   git remote add origin https://github.com/yourusername/leetcode-tracker.git
   git branch -M main
   git push -u origin main
   ```

## Files Included for Deployment

I've created these files for easy deployment:

- **`Procfile`**: Tells Heroku how to run your app
- **`requirements.txt`**: Updated with gunicorn for production
- **`runtime.txt`**: Specifies Python version
- **`app.py`**: Your Flask application with authentication

## Important Security Notes

Before deploying to production:

1. **Change the secret key** in `app.py`:
   ```python
   app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')
   ```

2. **Set environment variables** for credentials:
   ```python
   DEFAULT_CREDENTIALS = {
       'admin': os.environ.get('ADMIN_PASSWORD', 'password123'),
       # ... other credentials
   }
   ```

3. **Use environment variables** for sensitive data

## Data Persistence

⚠️ **Important**: Most free hosting platforms use ephemeral storage, meaning your `problems_data.json` file will be reset on each deployment.

### Solutions:
1. **Use a database** (PostgreSQL, MongoDB)
2. **Use cloud storage** (AWS S3, Google Cloud Storage)
3. **Accept that data resets** on deployments (for demo purposes)

## Quick Deploy to Heroku

If you want to try Heroku immediately:

```bash
# Install Heroku CLI first
pip install gunicorn
git add .
git commit -m "Add Heroku deployment files"
heroku create your-app-name
git push heroku main
heroku open
```

Your app will be live at the Heroku URL!

## Access Your App

Once deployed, you can access your app with these credentials:
- **Username**: admin, **Password**: password123
- **Username**: user, **Password**: leetcode2025  
- **Username**: student, **Password**: study123

Remember to change these credentials before public deployment!
