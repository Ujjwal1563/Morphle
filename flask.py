from flask import Flask, render_template
import subprocess
import datetime
import pytz
import os

app = Flask(_name_)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual name
    username = os.getlogin()
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.datetime.now(ist)
    top_output = subprocess.check_output(['top', '-bn1']).decode('utf-8')  # -bn1 for non-interactive batch mode, 1 iteration

    return render_template('htop.html', name=name, username=username, time=now_ist, top_output=top_output)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)