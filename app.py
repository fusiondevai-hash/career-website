from flask import Flask, render_template, abort,request

app = Flask(__name__)

# Jobs database (for now, just a list)
jobs = [
    {
        "id": "backend",
        "title": "Software Engineer (Backend)",
        "location": "Bengaluru · Hybrid",
        "responsibilities": [
            "Design, build, and maintain backend systems",
            "Optimize database queries for scalability",
            "Collaborate with frontend engineers and product managers"
        ],
        "requirements": [
            "3+ years of backend development experience",
            "Strong Python/Flask or Node.js skills",
            "Experience with SQL/NoSQL databases"
        ],
        "salary": "₹15-20 LPA"
    },
    {
        "id": "frontend",
        "title": "Frontend Engineer (React)",
        "location": "Remote (India)",
        "responsibilities": [
            "Build responsive UI with React",
            "Ensure cross-browser compatibility",
            "Collaborate with designers and backend developers"
        ],
        "requirements": [
            "2+ years of React development experience",
            "Good knowledge of JavaScript, HTML, CSS",
            "Experience with REST APIs"
        ],
        "salary": "₹12-18 LPA"
    },
    {
        "id": "datasci",
        "title": "Data Scientist",
        "location": "Mumbai · On-site",
        "responsibilities": [
            "Build ML models for business insights",
            "Perform data cleaning and preprocessing",
            "Work with cross-functional teams"
        ],
        "requirements": [
            "Strong Python skills (Pandas, NumPy, Scikit-learn)",
            "Experience with SQL",
            "Background in statistics/machine learning"
        ],
        "salary": "₹18-25 LPA"
    }
]

@app.route("/")
def home():
    return render_template("home.html", jobs=jobs)

@app.route("/job/<job_id>", methods=["GET", "POST"])
def job_detail(job_id):
    # Find job by id
    job = next((job for job in jobs if job["id"] ==             job_id), None)
    if not job:
        abort(404)
    if request.method == "POST":
        name= request.form.get("name")
        return render_template("success.html", job=job, name=name)
    return render_template("job_detail.html", job=job)

print(__name__)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
