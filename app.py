from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import csv
import json
import os
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')  # Change this in production!

# Configuration
CSV_FILE = 'all.csv'
PERSISTENCE_FILE = 'problems_data.json'

# Default credentials (change these for production)
DEFAULT_CREDENTIALS = {
    'admin': os.environ.get('ADMIN_PASSWORD', 'password123'),
    'user': os.environ.get('USER_PASSWORD', 'leetcode2025'),
    'student': os.environ.get('STUDENT_PASSWORD', 'study123')
}

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def load_csv_data():
    """Load problems from CSV file"""
    problems = []
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                problems.append({
                    'id': int(row['ID']),
                    'url': row['URL'],
                    'title': row['Title'],
                    'difficulty': row['Difficulty'],
                    'acceptance': row['Acceptance %'],
                    'frequency': row['Frequency %']
                })
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found!")
    return problems

def load_persistence_data():
    """Load saved comments and status from JSON file"""
    if os.path.exists(PERSISTENCE_FILE):
        try:
            with open(PERSISTENCE_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    return {}

def save_persistence_data(data):
    """Save comments and status to JSON file"""
    try:
        with open(PERSISTENCE_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving data: {e}")

def merge_data(problems, persistence_data):
    """Merge CSV data with persisted comments and status"""
    for problem in problems:
        problem_id = str(problem['id'])
        if problem_id in persistence_data:
            problem['comment'] = persistence_data[problem_id].get('comment', '')
            problem['status'] = persistence_data[problem_id].get('status', False)
            problem['last_updated'] = persistence_data[problem_id].get('last_updated', '')
        else:
            problem['comment'] = ''
            problem['status'] = False
            problem['last_updated'] = ''
    return problems

def get_stats(problems):
    """Calculate completion statistics"""
    total = len(problems)
    completed = sum(1 for p in problems if p.get('status', False))
    remaining = total - completed
    completion_rate = (completed / total * 100) if total > 0 else 0
    
    return {
        'total': total,
        'completed': completed,
        'remaining': remaining,
        'completion_rate': round(completion_rate, 1)
    }

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in DEFAULT_CREDENTIALS and DEFAULT_CREDENTIALS[username] == password:
            session['logged_in'] = True
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    """Main page showing all problems"""
    problems = load_csv_data()
    persistence_data = load_persistence_data()
    problems = merge_data(problems, persistence_data)
    stats = get_stats(problems)
    
    # Sort by difficulty and then by ID
    difficulty_order = {'Easy': 1, 'Medium': 2, 'Hard': 3}
    problems.sort(key=lambda x: (difficulty_order.get(x['difficulty'], 4), x['id']))
    
    return render_template('index.html', problems=problems, stats=stats)

@app.route('/update_status', methods=['POST'])
@login_required
def update_status():
    """Update problem status (done/undone)"""
    data = request.get_json()
    problem_id = str(data.get('problem_id'))
    status = data.get('status', False)
    
    persistence_data = load_persistence_data()
    
    if problem_id not in persistence_data:
        persistence_data[problem_id] = {}
    
    persistence_data[problem_id]['status'] = status
    persistence_data[problem_id]['last_updated'] = datetime.now().isoformat()
    
    save_persistence_data(persistence_data)
    
    return jsonify({'success': True})

@app.route('/update_comment', methods=['POST'])
@login_required
def update_comment():
    """Update problem comment"""
    data = request.get_json()
    problem_id = str(data.get('problem_id'))
    comment = data.get('comment', '')
    
    persistence_data = load_persistence_data()
    
    if problem_id not in persistence_data:
        persistence_data[problem_id] = {}
    
    persistence_data[problem_id]['comment'] = comment
    persistence_data[problem_id]['last_updated'] = datetime.now().isoformat()
    
    save_persistence_data(persistence_data)
    
    return jsonify({'success': True})

@app.route('/filter')
@login_required
def filter_problems():
    """Filter problems by status or difficulty"""
    filter_type = request.args.get('filter', 'all')
    difficulty = request.args.get('difficulty', 'all')
    
    problems = load_csv_data()
    persistence_data = load_persistence_data()
    problems = merge_data(problems, persistence_data)
    
    # Apply filters
    if filter_type == 'completed':
        problems = [p for p in problems if p.get('status', False)]
    elif filter_type == 'pending':
        problems = [p for p in problems if not p.get('status', False)]
    
    if difficulty != 'all':
        problems = [p for p in problems if p['difficulty'].lower() == difficulty.lower()]
    
    stats = get_stats(load_csv_data())  # Get overall stats
    
    # Sort by difficulty and then by ID
    difficulty_order = {'Easy': 1, 'Medium': 2, 'Hard': 3}
    problems.sort(key=lambda x: (difficulty_order.get(x['difficulty'], 4), x['id']))
    
    return render_template('index.html', problems=problems, stats=stats, 
                         current_filter=filter_type, current_difficulty=difficulty)

@app.route('/reset')
@login_required
def reset_data():
    """Reset all data (clear all comments and status)"""
    if os.path.exists(PERSISTENCE_FILE):
        os.remove(PERSISTENCE_FILE)
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
