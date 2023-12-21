from models.people import People
from flask import abort
from datetime import datetime
from models.post import Posts
from flask import request

TimeStamp = datetime.now()


def add_post(postRequest: dict) -> dict:
    """
    Description: Add a new post to the social network
    @param postRequest: a dict of the form:
                      {
                      'userId': "..."
                      'text': "..."
                      'visibility': "..."  --> "public" or "private"
                      }
    @return: a json response (dict) indicating the results of the operation
    """
    try:
        request.get_json()
        post_text = postRequest["text"]
        userId = postRequest["userId"]
        visibility = postRequest["visibility"]
        if visibility != "public" and visibility != "private":
            raise ValueError
    except KeyError:
        abort(
            400,
            {"message": "Bad Request"},
        )

    if userId in [People[it]["userId"] for it in range(0, len(People))]:
        Posts.append({"postId": len(Posts) + 1,
                      "text": post_text,
                      "postedOn": f'{TimeStamp}',
                      "visibility": postRequest["visibility"],
                      "likes": [],
                      "fullName": People[userId - 1]["fullName"]})
        People[userId - 1]['Posts'].append(len(Posts))
        return {'postId': len(Posts)}
    else:
        abort(
            406,
            {"message": "The userId is not present in the system."},
        )
