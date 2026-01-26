from flask import Flask

#creates your app
app = Flask(__name__)

#defines a route — a URL path your app responds to (/ is the homepage).
@app.route('/')
def hello():
    return "Hello, World!"

#starts a local server and gives you auto-reload feedback.
if __name__ == '__main__':
    app.run(debug=True)



 