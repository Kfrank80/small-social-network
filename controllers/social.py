from models.people import People
from models.post import Posts
from flask import abort


def user_wall(userId: int) -> list[dict]:
    """
    Description: Request to see userId wall, which contains all posts
                 that are visible to him, sorted by latest to earliest
                 (from the creation time descending)
    @param userId: the ID of the user requesting to see his wall
    @return: a json response list[dict] which is a list of all posts visible
             for userId
    """
    resultado = []
    if userId in [People[it]['userId'] for it in range(0, len(People))]:
        for post_id in People[userId - 1]['Posts']:
            resultado.append(Posts[post_id - 1])
        for friend_id in People[userId - 1]['Friends']:
            for friend_post_id in People[friend_id - 1]['Posts']:
                resultado.append(Posts[friend_post_id - 1])
        for follow_id in People[userId - 1]['Following']:
            for follow_post_id in People[follow_id - 1]['Posts']:
                if Posts[follow_post_id - 1]['visibility'] == 'public':
                    resultado.append(Posts[follow_post_id - 1])
        resultado.sort(key=lambda x: x['postedOn'], reverse=True)
        return resultado
    else:
        abort(
            400,
            {"message": f"Users with ID: {userId} not found in the system."},
        )


def add_like(userId: int, postId: int) -> dict:
    """
    Description: the userId liked postId
    @param userId: the ID of the user who like the post
    @param postId: the ID of the post
    @return: a json response (dict) indicating the results of the operation
    """
    if userId not in [People[it]["userId"] for it in range(0, len(People))] or postId not in [Posts[it]["postId"] for it
                                                                                              in range(0, len(Posts))]:
        abort(
            406,
            {"message": "The userId or postId is not present in the system."},
        )
    else:
        if userId not in Posts[postId - 1]['likes']:
            Posts[postId - 1]['likes'].append(userId)
            return {"message": f"{People[userId - 1]['fullName']} liked post with ID: {postId}"}
        else:
            abort(
                400,
                {"message": f"{People[userId - 1]['fullName']} already liked post with ID: {postId}"},
            )


def dislike(userId: int, postId: int) -> dict:
    """
        Description: the userId disliked postId
        @param userId: the ID of the user who dislike the post
        @param postId: the ID of the post
        @return: a json response (dict) indicating the results of the operation
    """
    if userId not in [People[it]["userId"] for it in range(0, len(People))] or postId not in [Posts[it]["postId"] for it
                                                                                              in range(0, len(Posts))]:
        abort(
            406,
            {"message": "The userId or postId is not present in the system."},
        )
    else:
        if userId in Posts[postId - 1]['likes']:
            Posts[postId - 1]['likes'].pop(Posts[postId - 1]['likes'].index(userId))
            return {"message": f"{People[userId - 1]['fullName']} disliked post with ID: {postId}"}
        else:
            abort(
                406,
                {"message": f"{People[userId - 1]['fullName']} is not liked post with ID: {postId}"},
            )
