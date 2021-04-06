# CPS 491 - Capstone II
This file is automatically created by a script. Please delete this line and replace with the course and your team information.
## encoder.py
```python
from connexion.apps.flask_app import FlaskJSONEncoder
import six

from swagger_server.models.base_model_ import Model


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            dikt = {}
            for attr, _ in six.iteritems(o.swagger_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return FlaskJSONEncoder.default(self, o)

```
## controllers/default_controller.py
```python
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
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())

    user = body._user_name
    print(user)

    question = body._text
    print(question)
    answer ="Hello "+ user +", thank you for your question! Here's what I found:\n "

    response = getAnswer(question)
    print(response)
    
    answer = answer + response

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
    url = "https://cps-491-mattermost-chatbot.herokuapp.com/receive_chat"
    jsonBody = {"text" : str(text)}
    result = requests.post(url, json = jsonBody)

    responseData = result.json()
    return responseData['answer']

```
## controllers/authorization_controller.py
```python
from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


```
## controllers/__init__.py
```python

```
## test/__init__.py
```python
import logging

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app

```
## test/test_default_controller.py
```python
# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_receive_url_post(self):
        """Test case for receive_url_post

        creates a question.
        """
        body = Body()
        response = self.client.open(
            '/apis/puzderd1/MattermostChatbot/1.0.0/receive_url',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

```
## util.py
```python
import datetime

import six
import typing


def _deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in six.integer_types or klass in (float, str, bool):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == datetime.date:
        return deserialize_date(data)
    elif klass == datetime.datetime:
        return deserialize_datetime(data)
    elif type(klass) == typing.GenericMeta:
        if klass.__extra__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__extra__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    else:
        return deserialize_model(data, klass)


def _deserialize_primitive(data, klass):
    """Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = six.u(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """Return a original value.

    :return: object.
    """
    return value


def deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :type string: str
    :return: date.
    :rtype: date
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: model object.
    """
    instance = klass()

    if not instance.swagger_types:
        return data

    for attr, attr_type in six.iteritems(instance.swagger_types):
        if data is not None \
                and instance.attribute_map[attr] in data \
                and isinstance(data, (list, dict)):
            value = data[instance.attribute_map[attr]]
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]


def _deserialize_dict(data, boxed_type):
    """Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in six.iteritems(data)}

```
## __init__.py
```python

```
## models/inline_response400.py
```python
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse400(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, message: str=None):  # noqa: E501
        """InlineResponse400 - a model defined in Swagger

        :param message: The message of this InlineResponse400.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'message': str
        }

        self.attribute_map = {
            'message': 'message'
        }
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse400':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_400 of this InlineResponse400.  # noqa: E501
        :rtype: InlineResponse400
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this InlineResponse400.


        :return: The message of this InlineResponse400.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this InlineResponse400.


        :param message: The message of this InlineResponse400.
        :type message: str
        """

        self._message = message

```
## models/body.py
```python
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel_id: str=None, channel_name: str=None, team_domain: str=None, team_id: str=None, post_id: str=None, text: str=None, timestamp: int=None, token: str=None, trigger_word: str=None, user_id: str=None, user_name: str=None, file_ids: str=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param channel_id: The channel_id of this Body.  # noqa: E501
        :type channel_id: str
        :param channel_name: The channel_name of this Body.  # noqa: E501
        :type channel_name: str
        :param team_domain: The team_domain of this Body.  # noqa: E501
        :type team_domain: str
        :param team_id: The team_id of this Body.  # noqa: E501
        :type team_id: str
        :param post_id: The post_id of this Body.  # noqa: E501
        :type post_id: str
        :param text: The text of this Body.  # noqa: E501
        :type text: str
        :param timestamp: The timestamp of this Body.  # noqa: E501
        :type timestamp: int
        :param token: The token of this Body.  # noqa: E501
        :type token: str
        :param trigger_word: The trigger_word of this Body.  # noqa: E501
        :type trigger_word: str
        :param user_id: The user_id of this Body.  # noqa: E501
        :type user_id: str
        :param user_name: The user_name of this Body.  # noqa: E501
        :type user_name: str
        :param file_ids: The file_ids of this Body.  # noqa: E501
        :type file_ids: str
        """
        self.swagger_types = {
            'channel_id': str,
            'channel_name': str,
            'team_domain': str,
            'team_id': str,
            'post_id': str,
            'text': str,
            'timestamp': int,
            'token': str,
            'trigger_word': str,
            'user_id': str,
            'user_name': str,
            'file_ids': str
        }

        self.attribute_map = {
            'channel_id': 'channel_id',
            'channel_name': 'channel_name',
            'team_domain': 'team_domain',
            'team_id': 'team_id',
            'post_id': 'post_id',
            'text': 'text',
            'timestamp': 'timestamp',
            'token': 'token',
            'trigger_word': 'trigger_word',
            'user_id': 'user_id',
            'user_name': 'user_name',
            'file_ids': 'file_ids'
        }
        self._channel_id = channel_id
        self._channel_name = channel_name
        self._team_domain = team_domain
        self._team_id = team_id
        self._post_id = post_id
        self._text = text
        self._timestamp = timestamp
        self._token = token
        self._trigger_word = trigger_word
        self._user_id = user_id
        self._user_name = user_name
        self._file_ids = file_ids

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel_id(self) -> str:
        """Gets the channel_id of this Body.


        :return: The channel_id of this Body.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id: str):
        """Sets the channel_id of this Body.


        :param channel_id: The channel_id of this Body.
        :type channel_id: str
        """

        self._channel_id = channel_id

    @property
    def channel_name(self) -> str:
        """Gets the channel_name of this Body.


        :return: The channel_name of this Body.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name: str):
        """Sets the channel_name of this Body.


        :param channel_name: The channel_name of this Body.
        :type channel_name: str
        """

        self._channel_name = channel_name

    @property
    def team_domain(self) -> str:
        """Gets the team_domain of this Body.


        :return: The team_domain of this Body.
        :rtype: str
        """
        return self._team_domain

    @team_domain.setter
    def team_domain(self, team_domain: str):
        """Sets the team_domain of this Body.


        :param team_domain: The team_domain of this Body.
        :type team_domain: str
        """

        self._team_domain = team_domain

    @property
    def team_id(self) -> str:
        """Gets the team_id of this Body.


        :return: The team_id of this Body.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id: str):
        """Sets the team_id of this Body.


        :param team_id: The team_id of this Body.
        :type team_id: str
        """

        self._team_id = team_id

    @property
    def post_id(self) -> str:
        """Gets the post_id of this Body.


        :return: The post_id of this Body.
        :rtype: str
        """
        return self._post_id

    @post_id.setter
    def post_id(self, post_id: str):
        """Sets the post_id of this Body.


        :param post_id: The post_id of this Body.
        :type post_id: str
        """

        self._post_id = post_id

    @property
    def text(self) -> str:
        """Gets the text of this Body.


        :return: The text of this Body.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this Body.


        :param text: The text of this Body.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def timestamp(self) -> int:
        """Gets the timestamp of this Body.


        :return: The timestamp of this Body.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int):
        """Sets the timestamp of this Body.


        :param timestamp: The timestamp of this Body.
        :type timestamp: int
        """

        self._timestamp = timestamp

    @property
    def token(self) -> str:
        """Gets the token of this Body.


        :return: The token of this Body.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body.


        :param token: The token of this Body.
        :type token: str
        """

        self._token = token

    @property
    def trigger_word(self) -> str:
        """Gets the trigger_word of this Body.


        :return: The trigger_word of this Body.
        :rtype: str
        """
        return self._trigger_word

    @trigger_word.setter
    def trigger_word(self, trigger_word: str):
        """Sets the trigger_word of this Body.


        :param trigger_word: The trigger_word of this Body.
        :type trigger_word: str
        """

        self._trigger_word = trigger_word

    @property
    def user_id(self) -> str:
        """Gets the user_id of this Body.


        :return: The user_id of this Body.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this Body.


        :param user_id: The user_id of this Body.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def user_name(self) -> str:
        """Gets the user_name of this Body.


        :return: The user_name of this Body.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name: str):
        """Sets the user_name of this Body.


        :param user_name: The user_name of this Body.
        :type user_name: str
        """

        self._user_name = user_name

    @property
    def file_ids(self) -> str:
        """Gets the file_ids of this Body.


        :return: The file_ids of this Body.
        :rtype: str
        """
        return self._file_ids

    @file_ids.setter
    def file_ids(self, file_ids: str):
        """Sets the file_ids of this Body.


        :param file_ids: The file_ids of this Body.
        :type file_ids: str
        """

        self._file_ids = file_ids

```
## models/__init__.py
```python
# coding: utf-8

# flake8: noqa
from __future__ import absolute_import
# import models into model package
from swagger_server.models.body import Body
from swagger_server.models.inline_response400 import InlineResponse400

```
## models/base_model_.py
```python
import pprint

import six
import typing

from swagger_server import util

T = typing.TypeVar('T')


class Model(object):
    # swaggerTypes: The key is attribute name and the
    # value is attribute type.
    swagger_types = {}

    # attributeMap: The key is attribute name and the
    # value is json key in definition.
    attribute_map = {}

    @classmethod
    def from_dict(cls: typing.Type[T], dikt) -> T:
        """Returns the dict as a model"""
        return util.deserialize_model(dikt, cls)

    def to_dict(self):
        """Returns the model properties as a dict

        :rtype: dict
        """
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model

        :rtype: str
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

```
## __main__.py
```python
#!/usr/bin/env python3

import connexion

from swagger_server import encoder
import os
  
PORT = os.environ.get('PORT')

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'MattermostChatAPI'}, pythonic_params=True)
    app.run(debug=True, host='0.0.0.0', port=PORT)


if __name__ == '__main__':
    main()

```
