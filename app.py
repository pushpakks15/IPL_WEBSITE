#consuming apis
from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route('/')
def home():
    response=requests.get('http://127.0.0.1:5000/api/teams')
    teams=response.json()['teams']
    return render_template('home.html',teams=teams)

@app.route('/teamvsteam')
def team_vs_team():
    team1=request.args.get('team1')
    team2=request.args.get('team2')
    response=requests.get(f'http://127.0.0.1:5000/api/teamvsteam?team1={team1}&team2={team2}').json()
    return render_template('result.html',result=response)




app.run(debug=True,port=4000)
