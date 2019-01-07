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
        'd': "Are you currently employed ?"
    },
    {
        'q': 'Resume',
        'd': 'Provide url for resume'
    },

    {
        'q': 'Puzzle',
        'd': "ABCD\nA=->-\nB-=<-\nC<---\nD>---"
    }
)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        url = request.form.get("url", None)
        if url:
            query = {
                'q': 'Ping',
                'd': 'Ping should recieve OK response to move forward'
            }
            ping = requests.get(url, params=query)
            ping = ping.text if ping.text else "No Response"

            if ping == "OK":
                result = dict()
                for query in queries:
                    response = requests.get(url, params=query)
                    question = query.get('q')
                    description = query.get('d')
                    answer = response.text if response.text else "No Response"
                    result[question] = (description, answer)
            else:
                result = None
            return render_template("result.html", result=result, response=ping)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
