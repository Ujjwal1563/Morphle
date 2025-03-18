from flask import Flask, render_template
import subprocess
import datetime
import pytz
import getpass

app = Flask(__name__)
@app.route('/')
def htop():
    print("htop route accessed")  # Add this line to verify if the route is being hit
    name = "Ujjwal Sharma"  # Replace with your actual name
    username = getpass.getuser()
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.datetime.now(ist)
    top_output = subprocess.check_output(['top', '-bn1']).decode('utf-8')  # -bn1 for non-interactive batch mode, 1 iteration

    return render_template('htop.html', name=name, username=username, time=now_ist, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
