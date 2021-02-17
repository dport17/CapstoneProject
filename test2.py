from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if (request.method == 'POST'):
        sampleJson = request.get_json()
        return jsonify({'you sent': sampleJson})
        # curl -H "Content-Type: application/json" -X POST -d "{\"name\":\"brandon\",\"address\":\"home\"}" http://127.0.0.1:5000/hello
        # OR
        # curl -i -X POST -H "Content-Type: application/json" -d "{\"text\": \"Hello, this is some text\nThis is more text. :tada:\"}" http://127.0.0.1:5000/hello
    else:
        return "Hello World!"

@app.route('/multiply/<int:num>', methods=['GET'])
def multiplyBy10(num):
    return jsonify({'result': num * 10}) 
    # http://127.0.0.1:5000/multiply/10
        # { "result": 100 }

    # return (num * 10) 
        # TypeError: The view function did not return a valid response. 
        # The return type must be a string, dict, tuple, Response instance, 
        # or WSGI callable, but it was a int.
            # The result is a TypeError


if __name__ == '__main__':
    app.run(debug=True)
