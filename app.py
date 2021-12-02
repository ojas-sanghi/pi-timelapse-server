from flask import Flask, request

app = Flask(__name__)

# TODO: figure out get requests in java, get this setup on heroku

@app.route("/")
def hello():
    return "Hello, this is the server for the UHS Pi Timelapse Setup"

# http://127.0.0.1:5000/update-status?status=Python
@app.route('/update-status')
def update_status():
    status = request.args['status']

    return '''<h1>Current status: {}</h1>'''.format(status)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)