class TestAddPost:
    def _assert_response_json_payload(self, response_payload: dict):
        assert response_payload['title'] == 'foo'
        assert response_payload['body'] == 'bar'
        assert response_payload['userId'] == '1'

    def test_post_successfully_added(self, http_client):
        post_creation_resp = http_client.post(
            '/posts',
            payload={
                'title': 'foo',
                'body': 'bar',
                'userId': 1,
            }
        )

        assert post_creation_resp.status_code == 201

        resp_body = post_creation_resp.json()
        self._assert_response_json_payload(resp_body)

        get_post_resp = http_client.get(f'/posts/{resp_body["id"]}')

        assert get_post_resp.status_code == 200

        resp_body = get_post_resp.json()
        self._assert_response_json_payload(resp_body)
