from flask import Flask, render_template, session, request, redirect
from NFT.test import get_value
app = Flask(__name__)

app.secret_key = b'e3ba6fc7ec44173d32d96d251bc692db7182a5b36ea233f045c64c8ae270cdb2'


@app.route("/")
def hello_world():
    print(session)
    if session.get('account'):
        balance = get_value(session['account'])
        return render_template('main.html', balance=balance)
    else:
        return render_template('main.html')

@app.route("/set-cookie", methods=['POST'])
def get_cookie():
    account = request.get_json()['account']
    session['account'] = account
    return {
        "Value":'Account bien enregistrer dans la session Flask'
    }


@app.route("/delete-cookie", methods=['POST'])
def delete_cookie():
    del session['account']
    return {
        "Value":'Account bien supprimer de la session Flask'
    }

    