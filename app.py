import requests, json
from flask import Flask, request, Response, render_template

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return render_template("index.html")

@app.route('/api/getQ',methods=['GET','POST'])
def api():
    if request.method=="GET":
        return "This API doesn't have a GET Request's Response..."
    # read post inputs
    if request.headers['Content-Type'] == 'application/json':
        text = request.json["text"]
        shouldSummarize = int(request.json["summarize"])
    else:
        return "header doesn't have application/json as Content-Type"
    

    if shouldSummarize == 1:
        text = summarize(text)
    return text
    # call question model

    # return a json response
    # {"questions":["q1","q2","q3"]}

@app.route('/api/getQArray',methods=['GET','POST'])
def apiArray():
    if request.method=="GET":
        return "This API doesn't have a GET Request's Response..."
    # read post inputs
    text = []
    shouldSummarize = []
    if request.headers['Content-Type'] == 'application/json':

        for i in range(0,len(request.json)):
            
            shouldSummarize.append(int(request.json[i]["summarize"]))
            if shouldSummarize[i] == 1:
                text.append(summarize(request.json[i]["text"]))
            else:
                text.append(request.json[i]["text"])
    else:
        return "header doesn't have application/json as Content-Type"
        
    # call question model

    # return a json response
    # {"questions":["q1","q2","q3"]}




def summarize(text):
    url = "https://api.deepai.org/api/summarization"

    payload = str(text)
    payload = payload.replace("'","")
    # headers = {
    #     'api-key': "395e6583-036c-43c0-a2db-92c8e129294e",
    #     }

    # response = requests.request("POST", url, data=payload, headers=headers)
    r = requests.post(
    url,
    data={
        'text': payload,
    },
    headers={'api-key': '395e6583-036c-43c0-a2db-92c8e129294e'}
    )
    # print(r.json())
    # print(response.text)
    if "err" in r.json():
        print(r.json()["err"])
        return r.json()["err"]
    return r.json()["output"]

# @app.route('/quiz/<article_name>/', methods = ['GET'])
# def get_quiz(article_name):

#     _resp = []

#     a = Article(article_name)

#     for question in a.quiz.get_ten_random():
#         _resp.append((question.text, question.gaps))

#     data_send = json.dumps({
#         'sentences': _resp,
#         'propers': a.quiz.get_random_propers(),
#         # 'locations': a.quiz.get_random_locations(),
#     })
#     resp = Response(data_send, status=200, mimetype='application/json')
#     #      Response("ERROR", status=500, mimetype='application/json')

#     resp.headers['Access-Control-Allow-Origin'] = "*"
#     return resp


if __name__ == '__main__':
    app.run()
