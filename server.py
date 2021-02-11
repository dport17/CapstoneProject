#!/usr/bin/env python3
import os
import sys
from io import BytesIO
import json

from flask import jsonify, request, Flask
from flask_cors import CORS, cross_origin


############################################################################
############                    GLOBALS                         ############
############################################################################
CPORT = os.environ.get('CPORT', 18000)
if isinstance(CPORT, str):
    CPORT = int(CPORT)
app = Flask(__name__)
CORS(app)


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


############################################################################
############                 FLASK ENDPOINTS                    ############
############################################################################
@cross_origin()
@app.route('/receive_chat', methods=['POST'])
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


def main():
    """
    main( ) function exposed for pip whl build in setup/Make file.
    """
    app.run(debug=True, host='0.0.0.0', port=CPORT)


if __name__ == '__main__':
    main()
