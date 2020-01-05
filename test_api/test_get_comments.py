from .utils import verify_json_payload_for_comment_object


class TestGetComments:
    def test_successfully_getting_comment_for_post_number_13(self, http_client):
        get_comments_resp = http_client.get('/posts/13/comments')

        assert get_comments_resp.status_code == 200

        comments_payload = get_comments_resp.json()

        assert len(comments_payload) == 5

    def test_each_comment_for_specific_post_object_contain_required_attributes(self, http_client):
        comment_objects = http_client.get('/posts/13/comments').json()

        for comment in comment_objects:
            verify_json_payload_for_comment_object(comment)

    def test_fetched_comment_object_contains_required_attributes(self, http_client):
        comment_objects = http_client.get('/posts/13/comments').json()
        get_comment_resp = http_client.get(f'/comments/{comment_objects[0]["id"]}')

        assert get_comment_resp.status_code == 200

        comment_object = get_comment_resp.json()

        verify_json_payload_for_comment_object(comment_object)

    def test_getting_comments_for_non_existing_post_fails(self, http_client):
        get_comments_for_post_resp = http_client.get('/posts/1234234/comments')

        assert get_comments_for_post_resp.status_code == 404

    def test_getting_non_existing_comment_fails(self, http_client):
        get_comment_resp = http_client.get('/comments/123123123')

        assert get_comment_resp.status_code == 404
