from models.people import People
from flask import abort, request


def add_friendship(userId: int, friendId: int) -> dict:
    """
    Description: Make a friendship between userId and friendId
    @param userId: an integer, ID of the user who make the proposal
    @param friendId: an integer, ID of the user who is going to receive the proposal
    @return: a json response (dict) indicating the results of the operation
    """
    # request.get_json()
    if not isinstance(userId, int) or not isinstance(friendId, int) or userId == friendId:
        abort(
            400,
            {"message": "Bad Request"},
        )
    if userId not in [People[it]['userId'] for it in range(0, len(People))] or friendId not in [People[it]['userId'] for it in range(0, len(People))]:
        abort(
            406,
            {"message": "The userId or friendId is not present in the system."},
        )
    else:
        if friendId not in People[userId - 1]['Friends']:
            People[userId - 1]['Friends'].append(friendId)
            People[friendId - 1]['Friends'].append(userId)
            return {"message": f"{People[userId - 1]['fullName']} and {People[friendId - 1]['fullName']} are friends now."}
        else:
            abort(
                406,
                {"message": "They are friends already"},
            )


def add_follower(userId: int, followerId: int) -> dict:
    """
    Description: Make userId a follower of friendId
    @param userId: an integer, ID of the user to be followed
    @param followerId: an integer, ID of the follower
    @return: a json response (dict) indicating the results of the operation
    """
    # request.get_json()
    if not isinstance(userId, int) or not isinstance(followerId, int):
        abort(
            400,
            {"message": "Bad Request"},
        )
    if userId not in [People[it]['userId'] for it in range(0, len(People))] or followerId not in [People[it]['userId'] for it in range(0, len(People))]:
        abort(
            406,
            {"message": "The userId or followerId is not present in the system."},
        )
    else:
        if userId not in People[followerId - 1]['Following']:
            People[followerId - 1]['Following'].append(userId)
            return {"message": f"{People[followerId - 1]['fullName']} is following {People[userId - 1]['fullName']}"}
        else:
            abort(
                406,
                {"message": f"{People[followerId - 1]['fullName']} is already following {People[userId - 1]['fullName']}"},
            )
