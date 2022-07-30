from flask import Flask, render_template, request # import what we need to use from the flask library
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

app = Flask(__name__) # invoke the Flask clask

@app.route('/')
def index():
    now_utc = datetime.now()
    #now_aest = now_aest = now_utc.replace(tzinfo=ZoneInfo('UTC')).astimezone(tz=ZoneInfo('Australia/Sydney'))
    ## debug
    now_aest = datetime.strptime("2022-08-02", '%Y-%m-%d')
    if now_aest.strftime("%m-%d") == "08-02":
        print("yes")
        return render_template('./yes.html')

    else:
        #print(now.strftime("%m-%d"))
        print("no")
        return render_template('./no.html')



if __name__ == '__main__':
    app.run(debug=True) # Start the server listening for requests