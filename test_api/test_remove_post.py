import pytest


class TestRemovePost:
    def test_successfully_removing_a_post(self, http_client):
        delete_post_resp = http_client.delete('/posts/1')

        assert delete_post_resp.status_code == 200

        get_post_resp = http_client.get('/posts/1')

        assert get_post_resp.status_code == 404

    def test_removing_non_existing_post_fails(self, http_client):
        remove_post_resp = http_client.delete('/posts/123231')

        assert remove_post_resp.status_code == 404
