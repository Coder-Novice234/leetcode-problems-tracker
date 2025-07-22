# LeetCode Problems Tracker

A Flask web application to track your LeetCode problem-solving progress with authentication, comments, status tracking, and persistence.

## 🌟 Features

- **🔐 User Authentication**: Secure login system with default credentials
- **📊 Progress Tracking**: Mark problems as done/undone with checkboxes
- **💬 Comments System**: Add personal notes, approaches, and comments for each problem
- **📈 Statistics Dashboard**: View completion stats, progress bar, and counters
- **🔍 Smart Filtering**: Filter by completion status (All/Completed/Pending) and difficulty (Easy/Medium/Hard)
- **💾 Data Persistence**: All data is saved locally in JSON format
- **⚡ Auto-save**: Comments are automatically saved as you type
- **🔗 Direct Links**: Click problem titles to open them on LeetCode
- **📱 Responsive Design**: Works well on desktop and mobile devices
- **🚀 Easy Deployment**: Ready for GitHub Pages, Heroku, Railway, and other platforms

## 🖥️ Screenshots

### Login Page
- Beautiful gradient design with demo credentials
- Click on any credential to auto-fill the form

### Main Dashboard
- Statistics cards showing progress overview
- Interactive progress bar
- Filter buttons for easy navigation

### Problem Table
- Checkboxes for marking completion status
- Comment sections for each problem
- Direct links to LeetCode problems

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Local Installation

1. **Clone or download this repository**
2. **Navigate to the project directory**:
   ```bash
   cd Att-Prep-DSA
   ```

3. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and go to: `http://localhost:5000`

## 🔑 Default Login Credentials

| Username | Password    | Purpose         |
|----------|-------------|-----------------|
| admin    | password123 | Administrator   |
| user     | leetcode2025| Regular user    |
| student  | study123    | Student account |

> 💡 **Tip**: Click on any credential in the login page to auto-fill the form!

## 📖 Usage Guide

### Getting Started
1. **Login** using any of the default credentials
2. **View your dashboard** with progress statistics
3. **Browse problems** from your CSV data

### Tracking Progress
- **✅ Mark Complete**: Click the checkbox next to each problem
- **📝 Add Comments**: Write notes about your solution approach, time complexity, etc.
- **💾 Auto-save**: Comments save automatically after 2 seconds
- **🔄 Manual Save**: Click the save button for immediate saving

### Filtering and Navigation
- **📊 View All**: See all problems at once
- **✅ Completed**: Filter to show only solved problems
- **⏳ Pending**: Show only unsolved problems
- **🎯 By Difficulty**: Filter by Easy, Medium, or Hard
- **🔄 Reset Data**: Clear all progress and start fresh

### Data Management
- **📁 Local Storage**: Progress saved in `problems_data.json`
- **🔄 Persistent**: Data survives app restarts
- **📤 Export Ready**: JSON format for easy backup/migration

## 📁 Project Structure

```
Att-Prep-DSA/
├── app.py                 # Main Flask application
├── all.csv               # Your LeetCode problems data
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment config
├── runtime.txt          # Python version for deployment
├── problems_data.json   # User progress storage (auto-created)
├── templates/
│   ├── index.html      # Main dashboard interface
│   └── login.html      # Authentication page
├── venv/               # Virtual environment (local)
├── README.md           # This file
├── DEPLOYMENT.md       # Hosting and deployment guide
└── .gitignore         # Git ignore rules
```

## 🌐 Hosting on GitHub

### Yes, you can definitely host this on GitHub! Here are your options:

### Option 1: Heroku (Recommended)
1. Create Heroku account
2. Connect your GitHub repository
3. Deploy with one click
4. **URL**: `https://your-app-name.herokuapp.com`

### Option 2: Railway
1. Connect GitHub repository at [railway.app](https://railway.app)
2. Automatic deployment on every push
3. Free tier available

### Option 3: Render
1. Connect repository at [render.com](https://render.com)
2. Zero-config deployment
3. Free SSL certificates

### Option 4: PythonAnywhere
1. Upload code to [pythonanywhere.com](https://pythonanywhere.com)
2. Configure WSGI application
3. Free tier for small applications

> 📖 **Detailed deployment instructions** are available in [`DEPLOYMENT.md`](DEPLOYMENT.md)

## 🔧 Configuration

### Environment Variables (for production)

```bash
SECRET_KEY=your-secret-key-here
ADMIN_PASSWORD=your-admin-password
USER_PASSWORD=your-user-password
STUDENT_PASSWORD=your-student-password
PORT=5000
FLASK_ENV=production
```

### Customizing Credentials

Edit the credentials in `app.py`:
```python
DEFAULT_CREDENTIALS = {
    'admin': os.environ.get('ADMIN_PASSWORD', 'password123'),
    'user': os.environ.get('USER_PASSWORD', 'leetcode2025'),
    'student': os.environ.get('STUDENT_PASSWORD', 'study123')
}
```

## 📊 Data Format

The application stores progress in `problems_data.json`:

```json
{
  "1": {
    "comment": "Used hash map approach. O(n) time complexity.",
    "status": true,
    "last_updated": "2025-07-22T10:30:00"
  },
  "3": {
    "comment": "Sliding window technique works well here.",
    "status": false,
    "last_updated": "2025-07-22T11:15:00"
  }
}
```

## 🎨 Customization

### Styling
- Modify CSS in `templates/index.html` and `templates/login.html`
- Bootstrap 5 classes for responsive design
- Font Awesome icons for visual elements

### Adding Features
- **New filters**: Extend the filtering system
- **Export functionality**: Add CSV/JSON export
- **Statistics**: Add more detailed analytics
- **Themes**: Implement dark/light mode

### Integration
- **Database**: Replace JSON with SQLite/PostgreSQL
- **Authentication**: Add OAuth or custom registration
- **API**: Create REST API endpoints

## 🔒 Security Notes

### For Production Deployment:

1. **Change secret key**:
   ```python
   app.secret_key = os.environ.get('SECRET_KEY', 'your-secure-key')
   ```

2. **Update credentials**:
   - Use environment variables
   - Consider implementing user registration
   - Add password hashing

3. **Enable HTTPS**:
   - Most hosting platforms provide SSL
   - Force HTTPS redirects

## ⚠️ Important Notes

### Data Persistence
- **Local Development**: Data persists in `problems_data.json`
- **Cloud Deployment**: Most free hosting platforms reset files on restart
- **Solution**: Consider using cloud databases (PostgreSQL, MongoDB) for production

### Performance
- **Current**: Optimized for ~100 problems
- **Scaling**: For larger datasets, consider pagination
- **Database**: Switch to SQL database for better performance

## 🐛 Troubleshooting

### Common Issues

1. **CSV not found**:
   - Ensure `all.csv` is in the project root
   - Check file permissions

2. **Port already in use**:
   - Change port in `app.py`: `port=8000`
   - Kill existing process: `pkill -f python`

3. **Login not working**:
   - Check credentials match exactly
   - Clear browser cookies/cache

4. **Data not saving**:
   - Check write permissions in project directory
   - Look for error messages in terminal

### Getting Help
- Check the Flask app logs in terminal
- Verify all files are in correct locations
- Ensure virtual environment is activated

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest new features  
- Submit pull requests
- Improve documentation

## 📜 License

This project is open source and available under the MIT License.

---

## 🎯 Ready to Start?

1. **Local Development**: Follow the installation steps above
2. **Deploy to Web**: Check out [`DEPLOYMENT.md`](DEPLOYMENT.md)
3. **Customize**: Modify the code to fit your needs
4. **Track Progress**: Start solving those LeetCode problems!

Happy coding! 🚀
