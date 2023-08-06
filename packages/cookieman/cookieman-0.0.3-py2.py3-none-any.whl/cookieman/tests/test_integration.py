
import unittest
import random
import string

import flask

import cookieman


class TestCookieMan(unittest.TestCase):
    module = cookieman

    def setUp(self):
        self.app = flask.Flask('myapp')
        self.app.session_interface = cookieman.CookieMan()
        self.app.secret_key = 'my_app_secret_key'

    def extract_cookies(self, client):
        return [
            c
            for c in client.cookie_jar
            if c.name.startswith(self.app.session_cookie_name)
            ]

    def test_session(self):
        @self.app.route('/write')
        def write():
            flask.session['value'] = 'something'
            return 'OK'

        @self.app.route('/read')
        def read():
            return flask.session.get('value', 'nothing')

        with self.app.test_client() as client:
            response = client.get('/read')
            self.assertEqual(response.data, b'nothing')

            response = client.get('/write')
            self.assertEqual(response.data, b'OK')

            response = client.get('/read')
            self.assertEqual(response.data, b'something')
            self.assertIn('Vary', response.headers)
            self.assertNotIn('Set-Cookie', response.headers)

            cookie, = self.extract_cookies(client)
            client.cookie_jar.clear()
            client.set_cookie(
                cookie.domain,
                cookie.name,
                value='buggy',
                expires=cookie.expires,
                path=cookie.path,
                domain=cookie.domain,
                secure=cookie.secure,
                )

            response = client.get('/read')
            self.assertEqual(response.data, b'nothing')

    def test_session_permanent(self):
        @self.app.route('/write')
        def write():
            flask.session['value'] = 'something'
            flask.session.permanent = True
            return 'OK'

        @self.app.route('/read')
        def read():
            return flask.session.get('value', 'nothing')

        @self.app.route('/noop')
        def noop():
            return 'OK'

        self.app.config['SESSION_REFRESH_EACH_REQUEST'] = True

        with self.app.test_client() as client:
            response = client.get('/write')
            self.assertEqual(response.data, b'OK')

            response = client.get('/read')
            self.assertEqual(response.data, b'something')
            self.assertIn('Vary', response.headers)
            self.assertIn('Set-Cookie', response.headers)

            response = client.get('/noop')
            self.assertEqual(response.data, b'OK')
            self.assertNotIn('Vary', response.headers)
            self.assertIn('Set-Cookie', response.headers)

            self.app.config['SESSION_REFRESH_EACH_REQUEST'] = False
            response = client.get('/noop')
            self.assertEqual(response.data, b'OK')
            self.assertNotIn('Vary', response.headers)
            self.assertNotIn('Set-Cookie', response.headers)

    def test_signature(self):
        @self.app.route('/write')
        def write():
            flask.session['value'] = 'something'
            return 'OK'

        @self.app.route('/read')
        def read():
            return flask.session.get('value', 'nothing')

        with self.app.test_client() as client:
            response = client.get('/write')
            self.assertEqual(response.data, b'OK')
            self.app.secret_key = 'other'
            response = client.get('/read')
            self.assertEqual(response.data, b'nothing')

    def test_secret_key(self):
        self.app.secret_key = None
        with self.app.test_request_context():
            with self.assertRaises(RuntimeError):
                flask.session['value'] = 'something'

    def test_removal(self):
        @self.app.route('/set')
        def set_cookie():
            flask.session['value'] = 'something'
            return 'OK'

        @self.app.route('/unset')
        def unset_cookie():
            del flask.session['value']
            return 'OK'

        with self.app.test_client() as client:
            response = client.get('/set')
            self.assertEqual(response.data, b'OK')
            cookies = self.extract_cookies(client)
            self.assertEqual(len(cookies), 1)

            response = client.get('/unset')
            self.assertEqual(response.data, b'OK')
            cookies = self.extract_cookies(client)
            self.assertEqual(len(cookies), 0)

    def test_shrink(self):
        calls = []

        @self.app.session_interface.register('a')
        def shrink_a(data, last):
            calls.append(len(data['a']))
            if len(data['a']) < 2:
                del data['a']
            else:
                data['a'] = data['a'][:-2]
            return data

        @self.app.route('/')
        def root():
            value = ''.join(
                random.choice(string.ascii_letters)
                for i in range(5000)
                )
            flask.session['a'] = flask.session.get('a', '') + value
            return 'OK'

        with self.app.test_client() as client:
            for i in range(5):
                response = client.get('/')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data, b'OK')

                cookies = self.extract_cookies(client)
                self.assertEqual(len(cookies), 1)
        self.assertGreater(len(calls), 1)
