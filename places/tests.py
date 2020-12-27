from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestMainPage(StaticLiveServerTestCase):

    def test_start_ok(self):
        response = self.client.get(self.live_server_url)
        assert response.status_code == 200
