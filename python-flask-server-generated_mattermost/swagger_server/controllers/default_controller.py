import connexion
import six
import requests

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server import util
from flask import jsonify
import hashlib

MATTERMOST_HASHED_TOKEN = "c8a6dd3cbd5a94d7356d3cffad8a7f97f1d31b18d0590e7ad965bf87"

def receive_url_post(body):  # noqa: E501

    # These print statements are what is shown in Mattermost
    print("The receive_url_post has received the body.")
    print("\n")
    print(body)
    
    """
    creates a question.
     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())

    # "body._user_name" refers to the json body's "user_name" variable
    user = body._user_name
    print(user)

    # "body._text" refers to the json body's "_text" variable
    question = body._text
    print(question)
    answer ="Hello "+ user +", thank you for your question! Here's what I found:\n "
    token = body._token

    authorized = False
    token = str.encode(token)
    if hashlib.sha224(token).hexdigest() == MATTERMOST_HASHED_TOKEN:
        print("Authorization granted.")
        authorized = True

   
    if authorized:
        user = body._user_name

        question = body._text
        print(question)
        answer ="Hello "+ user +", thank you for your question! Here's what I found:\n "

        response = getAnswer(question)
        print(response)
        
        answer = answer + response

        jsonBody = {"text": answer} #, "response_type": "comment"}

        # ------ This url represents the incoming webhook on Mattermost ------
        url = 'https://udricapstone.cloud.mattermost.com/hooks/wnojm45ppbb7ie8tzfhx8841nw'

        # ------------- Change the dotted section for future use -------------

        result = requests.post(url, json = jsonBody)

        print(result.text)

        return "Everything successful, reply sent"

      # noqa: E501
    else:
        return "ACCESS DENIED WEE OOO WEE OOO"
    

def getAnswer(text):
    # call the UDRI API and grab the response from the JSON body returned

    # --------------- This url represents Alex's mock API. ---------------
    url = "https://cps-491-mattermost-chatbot.herokuapp.com/receive_chat"

    # ------------- Change the dotted section for future use -------------

    jsonBody = {"text" : str(text)}
    result = requests.post(url, json = jsonBody)

    # return that response
    responseData = result.json()
    return responseData['answer']
