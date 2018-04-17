import unittest

from run_app import app


class FlaskHTMLPracticeTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_1_index(self):
        response = self.client.get('/index')
        assert response.status_code == 200
        # assert b'Hello Guido Van Rossum!' in str(response.data)

    def test_2_index_with_params(self):
        response = self.client.get('/index?user=test')
        assert response.status_code == 200
        # assert (response.data) == b'The sum of 100 and 200 is: 300'

    def test_3_get_form(self):
        response = self.client.get('/get-form')
        assert response.status_code == 200

    def test_4_get_form_post_not_allowed(self):
        response = self.client.post('/get-form')
        assert response.status_code == 405

    def test_5_post_form_redirect(self):
        response = self.client.post(
            '/post-form', data={'username': 'Guido van Rossum'})
        assert response.status_code == 302

    def test_6_get_login_form(self):
        response = self.client.get('/login-form')
        assert response.status_code == 200

    def test_7_post_login_form(self):
        response = self.client.post(
            '/login-form', data={'username': 'Guido van Rossum'})
        assert response.status_code == 302
