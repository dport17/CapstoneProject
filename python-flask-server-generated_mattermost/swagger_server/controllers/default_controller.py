import connexion
import six
import requests

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server import util
from flask import jsonify


def receive_url_post(body):  # noqa: E501
    print("The receive_url_post has received the body.")
    print("\n")
    print(body)
    """creates a question.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    # if connexion.request.is_json:
    #     body = Body.from_dict(connexion.request.get_json())

    user = body['user_name']
    print(user)

    question = body['text']
    print(question)
    answer ="Hello "+str(user)+", thank you for your question! Here's what I found:\n "

    result = getAnswer(question)
    result.json()
    print(result)
    answer = answer + result.answer

    jsonBody = {"text": answer}#, "response_type": "comment"}

    url = 'https://udricapstone.cloud.mattermost.com/hooks/wnojm45ppbb7ie8tzfhx8841nw'

    result = requests.post(url, json = jsonBody)

    print(result.text)

      # noqa: E501
    return 'This is the body I received: '+str(body)

def getAnswer(text):
    #call the UDRI API
    #grab the response from the JSON body returned
    #return that response
    url = "http://127.0.0.1:18000/receive_chat"
    jsonBody = {"text" : str(text)}
    result = requests.post(url, json = jsonBody)

    return result
