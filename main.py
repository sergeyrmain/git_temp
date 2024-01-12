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
    #fix

    result = num1 - num2
    return jsonify({"result": result})


@app.route('/divide', methods=['GET'])
def divide():
    num1 = request.args.get('num1', default=1, type=int)
    num2 = request.args.get('num2', default=1, type=int)
    if num2 == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    result = num1 / num2
    return jsonify({"result": result})


@app.route('/multiply', methods=['GET'])
def multiply():
    num1 = request.args.get('num1', default=0, type=int)
    num2 = request.args.get('num2', default=0, type=int)
    result = num1 * num2
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
