from flask import Flask, request, jsonify

app = Flask(__name__)

def UDRI_API(text):
    """UDRI API function that returns an answer to a mattermost user query.
    This example simply returns the question asked plus a random answer.

    Args:
        text (str): the text sent from the /receive_chat endpoint

    Returns:
        dict:
        {
            'query': str # original query sent in,
            'answer': str # answer to the query
        }
    """
    from essential_generators import DocumentGenerator

    gen = DocumentGenerator()
    response = {}
    response['query'] = text
    response['answer'] = gen.sentence()
    return response

@app.route('/receive_chat', methods=['GET', 'POST'])
def receive_chat():
    """
    The endpoint for the UDRI server to receive chat messages, encoded as JSON.
    Expected input:
    {
        'text': 'Some text here'
    }
    """
    print(request)
    text = request.json['text']

    response = UDRI_API(text)
    return jsonify(response)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
