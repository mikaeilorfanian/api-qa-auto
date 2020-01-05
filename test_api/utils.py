def verify_json_payload_for_post_object(payload: dict):
    assert payload['title'] == 'foo'
    assert payload['body'] == 'bar'
    assert payload['userId'] == '1'


def verify_json_payload_for_comment_object(payload: dict):
    assert payload['postId'] is not None
    assert payload['id'] is not None
    assert payload['email'] is not None
    assert payload['body'] is not None
