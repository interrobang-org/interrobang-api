import requests, json
from flask import Flask, request, Response, render_template
from bs4 import BeautifulSoup
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import random
import mechanicalsoup
app = Flask(__name__)

# Instantiates a client
client = language.LanguageServiceClient()

# @app.route('/', methods=['GET'])
# def index():
#     return render_template("index.html")

@app.route('/api/getQ',methods=['GET','POST'])
def api():
    if request.method=="GET":
        return "This API doesn't have a GET Request's Response..."
    # read post inputs
    if request.headers['Content-Type'] == 'application/json':
        url = request.json["url"]
        text = getTextFromUrl(url)
        shouldSummarize = int(request.json["summarize"])
    else:
        return "header doesn't have application/json as Content-Type"
    

    if shouldSummarize == 1:
        text = summarize(text)
    # return text
    # call question model
    # senti = getSentiment(text)
    questions = getEntityAnalysis(text)
    q = {}
    for i,x in enumerate(questions):
        if x not in q:
            q[x]=i
    q_final = []
    for k in q:
        q_final.append(k)
    ret = {
        "questions":q_final,
        "error":False
    }
    if questions == []:
        ret["error"]=True
    
    return json.dumps(ret)
    # return a json response
    # {"questions":["q1","q2","q3"]}
# def getSentiment(text):
#     document = types.Document(
#         content=text,
#         language='en',
#         type=enums.Document.Type.PLAIN_TEXT)
#     sentiment = client.analyze_sentiment(document=document).document_sentiment    
#     sentiment='{}, {}'.format(sentiment.score, sentiment.magnitude)
#     return sentiment

def getEntityAnalysis(text):
    print(text)
    category_type_count = {"1":0, "2":0, "3":0, "4":0}
    document = types.Document(
        content=text,
        language='en',
        type=enums.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(
        document=document,
        encoding_type='UTF8',
    )
    ret = []
    print(response)
    for entity in response.entities:
        if (entity.type < 1 or entity.type > 4) or (category_type_count[str(entity.type)] > 3):
            continue

        category_type_count[str(entity.type)] += 1
        temp = {}
        temp["name"] = entity.name
        temp["type"] = entity.type
        temp["salience"] = entity.salience
        ret.append(temp)
    template_questions = {"1":["What did OBJECT do today?","What is OBJECT up to, now?"],"2":["What is the OBJECT end up doing?","What are OBJECT's lateset ventures?"],"4":["Did you hear what happened at OBJECT?"]}
    questions = []
    for  x in ret:
        if x["type"]!=3:
            # print("********************",x["type"])
            i = random.randint(0,len(template_questions[str(x["type"])])-1)
            # print("len(template_questions[str(x['type'])]) = ", len(template_questions[str(x["type"])]))
            # print("i = " ,i)
            # print(template_questions["1"][0])
            template_questions[str(x["type"])][i]=template_questions[str(x["type"])][i].replace("OBJECT",x["name"])
            # print("questions = ", questions)
            # print("template_questions = ", template_questions)
            # print("str(x['type'])",str(x["type"]))
            # print("i=",i)
            questions.append(template_questions[str(x["type"])][i])
    return questions


def getTextFromUrl(url):
    # html = requests.get(url).content
    # soup = BeautifulSoup(html)

    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    html = str(browser.get_current_page())
    # print(type(html))
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    # print(text)
    return text

# @app.route('/api/getQArray',methods=['GET','POST'])
# def apiArray():
#     if request.method=="GET":
#         return "This API doesn't have a GET Request's Response..."
#     # read post inputs
#     urls = []
#     text = []
#     # shouldSummarize = [] #unnecessary variable
#     if request.headers['Content-Type'] == 'application/json':

#         for i in range(0,len(request.json)):
            
#             # shouldSummarize.append(int(request.json[i]["summarize"]))
#             if int(request.json[i]["summarize"]) == 1:
#                 urls.append(request.json[i]["text"])
#                 text.append(getTextFromUrl(urls[i]))
#                 text[i] = summarize(text[i])
#             else:
#                 urls.append(request.json[i]["text"])
#                 text.append(getTextFromUrl(urls[i]))
#     else:
#         return "header doesn't have application/json as Content-Type"
        
#     # call question model

#     # return a json response
#     # {"questions":["q1","q2","q3"]}




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
