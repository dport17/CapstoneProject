import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def users_user_id_get(user_id):  # noqa: E501
    """Returns a user by ID

     # noqa: E501

    :param user_id: The ID of the user to return
    :type user_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'
