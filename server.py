from flask import Flask, render_template, request
import budget


app = Flask(__name__)
email_code = budget.get_email_code()
@app.route('/')

def home_page():

    return render_template("home.html")




@app.route('/verification', methods=['POST', 'GET'])
def send_2fa_code():
    if request.method == 'POST':
        data = request.form.to_dict()


    verification_code = budget.send_email_code()
    
    return render_template('2factor.html')
