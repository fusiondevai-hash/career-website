from flask import Flask, render_template

app = Flask(__name__)

# Configure Flask to allow all hosts for Replit proxy
app.config['SERVER_NAME'] = None

@app.route('/')
def home():
    """Home page showing career opportunities"""
    jobs = [
        {
            'id': 1,
            'title': 'Software Engineer',
            'department': 'Engineering',
            'location': 'San Francisco, CA',
            'type': 'Full-time',
            'description': 'Join our engineering team to build innovative software solutions.'
        },
        {
            'id': 2,
            'title': 'Product Manager',
            'department': 'Product',
            'location': 'New York, NY',
            'type': 'Full-time',
            'description': 'Lead product strategy and drive feature development.'
        },
        {
            'id': 3,
            'title': 'UX Designer',
            'department': 'Design',
            'location': 'Remote',
            'type': 'Full-time',
            'description': 'Design beautiful and intuitive user experiences.'
        }
    ]
    
    return render_template('index.html', jobs=jobs)

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    """Job detail page"""
    # In a real app, this would fetch from a database
    job = {
        'id': job_id,
        'title': 'Software Engineer',
        'department': 'Engineering',
        'location': 'San Francisco, CA',
        'type': 'Full-time',
        'description': 'Join our engineering team to build innovative software solutions.',
        'requirements': [
            'Bachelor\'s degree in Computer Science or related field',
            '3+ years of experience in software development',
            'Proficiency in Python, JavaScript, or similar languages',
            'Experience with web frameworks and databases'
        ]
    }
    
    return render_template('job_detail.html', job=job)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    # Bind to 0.0.0.0:5000 for Replit environment
    app.run(host='0.0.0.0', port=5000, debug=True)