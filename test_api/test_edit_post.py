from .utils import verify_json_payload_for_post_object


class TestEditPost:
    def test_successfully_edited_post_using_http_PUT_verb(self, http_client, post_object):
        post_edit_resp = http_client.put('/posts/1', post_object)

        assert post_edit_resp.status_code == 200
        verify_json_payload_for_post_object(post_edit_resp.json())

    def test_successfully_edited_post_using_http_PATCH_verb(self, http_client):
        post_edit_resp = http_client.patch('/posts/1', {'title': 'not_foo'})

        assert post_edit_resp.status_code == 200
        assert post_edit_resp.json()['title'] == 'not_foo'

    def test_editing_post_object_with_wrong_http_verb_fails(self, http_client, post_object):
        post_edit_resp = http_client.post('/posts/1', post_object)

        assert post_edit_resp.status_code in range(400, 500)

    def test_editing_post_object_with_malformed_json_payload_fails(self, http_client):
        post_edit_resp = http_client.put('/posts/1', {'random_attr': 'title'})
        assert post_edit_resp.status_code in list(range(400, 500))
