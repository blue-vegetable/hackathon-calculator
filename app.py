import math
from flask import Flask ,render_template,request
from flask_cors import CORS


app = Flask(__name__)
CORS(app,  resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template("./index.html")

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    temp = request.form.get('process').replace('$','+').replace('mod','%')
    print(temp)
    try:
        ans = eval(temp)
    except:
        ans ="算式存在错误"
    return str(ans)


if __name__ == '__main__':
    app.run()
