import requests
from flask import Flask, render_template, request

app = Flask(__name__)

queries = (
    {
        'q': 'Name',
        'd': "What's your name ?"
    },
    {
        'q': 'Email Address',
        'd': "What's your email Address ?"
    },
    {
        'q': 'Phone',
        'd': "What's your phone number ?"
    },
    {
        'q': 'Position',
        'd': "What's your position ?"
    },
    {
        'q': 'Years',
        'd': "What's your experience (in years) ?"
    },
    {
        'q': 'Referrer',
        'd': "Name your current organisation ?"
    },
    {
        'q': 'Degree',
        'd': "What's your Educational Qualification ?"
    },
    {
        'q': 'Status',
        'd': "What's your experience (in years) ?"
    },
    {
        'q': 'Resume',
        'd': 'Provide url for resume'
    },
    {
        'q': 'Ping',
        'd': 'OK'
    },
)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        url = request.form.get("url", None)
        if url:
            result = dict()
            for query in queries:
                response = requests.get(url, params=query)
                key = query.get('q')
                value = response.text if response.text else "No Response"
                result[key] = value
            return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
