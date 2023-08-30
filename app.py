from flask import Flask,render_template,jsonify,request,make_response
from flask_cors import cross_origin,CORS
import requests
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
        # print(response2)
        return jsonify(response2)
    return render_template("./index.html")

if __name__=="__main__":
    app.run()