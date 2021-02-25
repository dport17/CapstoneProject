import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server import util


def receive_url_post(body):  # noqa: E501
    """creates a question.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
