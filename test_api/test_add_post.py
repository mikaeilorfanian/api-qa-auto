class TestAddPost:
    def _assert_response_json_payload(self, response_payload: dict):
        assert response_payload['title'] == 'foo'
        assert response_payload['body'] == 'bar'
        assert response_payload['userId'] == '1'

    def test_post_successfully_added(self, http_client):
        post_creation_resp = http_client.post('/posts', payload={'title': 'foo', 'body': 'bar', 'userId': 1,})

        assert post_creation_resp.status_code == 201

        resp_body = post_creation_resp.json()
        self._assert_response_json_payload(resp_body)

        id_of_created_post = resp_body['id']
        get_post_resp = http_client.get(f'/posts/{id_of_created_post}')

        assert get_post_resp.status_code == 200

        resp_body = get_post_resp.json()
        self._assert_response_json_payload(resp_body)

    def test_adding_post_with_GET_http_verb_fails(self, http_client):
        post_creation_resp = http_client.get('/posts', payload={'title': 'foo', 'body': 'bar', 'userId': 2,})

        assert post_creation_resp.status_code != 201

    def test_adding_post_with_PUT_http_verb_fails(self, http_client):
        post_creation_resp = http_client.put('/posts', payload={'title': 'foo', 'body': 'bar', 'userId': 2,})

        assert post_creation_resp.status_code != 201

    def test_adding_post_with_malformatted_json_payload_fails(self, http_client):
        post_creation_resp = http_client.post('/posts', payload={'body': 'bar', 'userId': 1,})

        assert post_creation_resp.status_code != 201
