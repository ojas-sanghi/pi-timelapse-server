from datetime import datetime
# import pytz
from flask import Flask, request

app = Flask(__name__)

status = "No status yet"
time_received = datetime.now()

@app.route("/")
def hello():
    return "Hello, this is the server for the UHS Pi Timelapse Setup"

# http://127.0.0.1:5000/update-status?status=Python
@app.route('/update-status')
def update_status():
    global status, time_received
    
    status = request.args['status']

    # mst = pytz.timezone("America/Phoenix")
    time_received = datetime.now() #mst
    
    print("GOT! STATUS!")
    return ""

@app.route('/get-status')
def get_status():
    # timediff = datetime.now() - time_received
    # timediff_s = timediff.total_seconds()
    # minutes_diff  = divmod(timediff_s, 60)[0]
        #     <br>
        # Time since last: {}

    return '''
    <h1>
        Current status: {}
        <br>
        Time received: {}

    </h1>

    '''.format(status, time_received.strftime("%H:%M:%S %d %B %Y")) #, minutes_diff)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
