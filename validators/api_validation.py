def validate_post_json(post_json):
    """
    Validates whether we have the correct json data
    :return: True if we have the correct json data, False otherwise
    """
    if not post_json:
        return {'message': "Wrong data"}, 400
