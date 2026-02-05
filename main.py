from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Python Calculator API is running"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    try:
        a = float(data.get("a"))
        b = float(data.get("b"))
        operator = data.get("operator")

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                return jsonify({"error": "Division by zero"}), 400
            result = a / b
        else:
            return jsonify({"error": "Invalid operator"}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": "Invalid input"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
