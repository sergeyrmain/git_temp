from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add', methods=['GET'])
def add():
    num1 = request.args.get('num1', default=0, type=int)
    num2 = request.args.get('num2', default=0, type=int)

    result = num1 + num2
    return jsonify({"result": result})


@app.route('/subtract', methods=['GET'])
def subtract():
    num1 = request.args.get('num1', default=0, type=int)
    num2 = request.args.get('num2', default=0, type=int)

    result = num1 - num2
    return jsonify({"result": result})
# comment 

if __name__ == '__main__':
    app.run(debug=True)
