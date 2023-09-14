from flask import Flask,render_template,jsonify,request
from flask_cors import CORS
import requests
from src.connections import connect
from src.auth import authorization
submission_url="https://leetcode.com/playground/api/runcode"
result_url="https://www.leetcode.com/submissions/detail/{}/check/"
app=Flask(__name__)
CORS(app)
@app.route('/',methods=['GET',"POST"])
def home():
    if request.method=="POST":
        content=request.get_json()
        # print(content)
        response=requests.post(submission_url,content.get('data')).json()
        interpret_id=response['interpret_id']
        response2=requests.get(result_url.format(interpret_id)).json()
        print(response2)
        n=0
        while response2.get("state")!="SUCCESS":
            response2=requests.get(result_url.format(interpret_id)).json()
            if n==4:
                break
            n=n+1
            # print(response2)
        return jsonify(response2)
    return render_template("./index.html")

@app.route("/s",methods=['GET','POST'])
def index():
    if request.method=='POST':
        content=request.get_json()
        print(content)
        email=content['data']['email']
        password=content['data']['password']
        auth=authorization()
        response=auth.login(email,password)
        return jsonify(response)
    return "hello"
if __name__=="__main__":
    app.run()
