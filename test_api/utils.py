def verify_json_payload_for_post_object(payload: dict):
    assert payload['title'] == 'foo'
    assert payload['body'] == 'bar'
    assert payload['userId'] == '1'
