from flask import Flask, render_template, abort,request
from database import load_db
app = Flask(__name__)

# Jobs database (for now, just a list)
jobs = load_db()

@app.route("/")
def home():
    return render_template("home.html", jobs=jobs)

@app.route("/job/<int:job_id>", methods=["GET", "POST"])
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
