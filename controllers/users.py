from flask import abort
from models.people import People
from flask import request


def create(userRequest: dict) -> dict:
    """
    Description: Create a new user in the system
    @param userRequest: a dict with exactly one key: "fullName"
    @return: a json response (dict) indicating the results of the operation
    """
    try:
        request.get_json()
        full_name_new_user = userRequest['fullName']
    except KeyError:
        abort(
            400,
            {"message": "Bad Request"},
        )
    if full_name_new_user not in [People[it]["fullName"] for it in range(0, len(People))]:
        People.append({"userId": len(People)+1,
                       "fullName": full_name_new_user,
                       "Posts": [],
                       "Friends": [],
                       "Following": []})
        return {"userId": len(People)}
    else:
        abort(
            406,
            {"message": f"Person with name: {full_name_new_user} already exists"},
        )
