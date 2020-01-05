from .utils import verify_json_payload_for_post_object


class TestAddPost:
    def test_post_successfully_added(self, http_client, post_object):
        post_creation_resp = http_client.post('/posts', payload=post_object)

        assert post_creation_resp.status_code == 201

        resp_body = post_creation_resp.json()

        verify_json_payload_for_post_object(resp_body)

        id_of_created_post = resp_body['id']
        get_post_resp = http_client.get(f'/posts/{id_of_created_post}')

        assert get_post_resp.status_code == 200

        resp_body = get_post_resp.json()

        verify_json_payload_for_post_object(resp_body)

    def test_adding_post_with_GET_http_verb_fails(self, http_client, post_object):
        post_creation_resp = http_client.get('/posts', payload=post_object)

        assert post_creation_resp.status_code != 201

    def test_adding_post_with_PUT_http_verb_fails(self, http_client, post_object):
        post_creation_resp = http_client.put('/posts', payload=post_object)

        assert post_creation_resp.status_code in list(range(400, 500))

    def test_adding_post_with_malformatted_json_payload_fails(self, http_client):
        post_creation_resp = http_client.post('/posts', payload={'body': 'bar', 'userId': 1,})

        assert post_creation_resp.status_code in list(range(400, 500))
