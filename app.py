from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "My Calculator"

@app.route('/calc', methods=['GET','POST'])
def calc():
    if request.method == "GET":
        num1 = int(request.args.get('value1'))
        num2 = int(request.args.get('value2'))
        ch = request.args.get('operation')
    elif request.method == "POST":
        reqJson = request.get_json(force=False)
        num1 = int(reqJson['value1'])
        num2 = int(reqJson['value2'])
        ch = str(reqJson['operation'])

    if ch == ' ':
            ans = num1 + num2
    elif ch == '-':
        ans = num1 - num2
    elif ch == '*':
        ans = num1 * num2
    else:
        ans = 'Other then + - *'
    return jsonify({"Result": str(ans)})


if __name__ == '__main__':
    app.run(debug=True, port=9090)