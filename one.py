import urllib
from flask import Flask, request


#app = Flask(__name__)
app = Flask(__name__.split('?')[0])


@app.after_request
def after(response):
    if request.method == "GET":
        response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/weeby/magic", methods=['GET'])
def hello_world():
    # Happy hacking :)
	temp = request.args.get('spell');
	return temp.replace('plugh','1').replace('thud','2').replace('graply','3').replace('1','graply').replace('3','thud').replace('2','plugh');



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
