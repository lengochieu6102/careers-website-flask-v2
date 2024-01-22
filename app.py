from flask import Flask
from flask import render_template, jsonify

app = Flask(__name__)

jobs = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs = jobs)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
