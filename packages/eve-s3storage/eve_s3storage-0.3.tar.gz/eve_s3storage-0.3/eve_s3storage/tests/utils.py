import sys
import eve
import json
import unittest
from bson import ObjectId
from flask import g
from flask.testing import FlaskClient
from flask.wrappers import Response
from pymongo import MongoClient
from eve_s3storage.s3_storage import S3MediaStorage


class TestClient(FlaskClient):
    """Custom test client with additional request/response checks.
    Auth header will be added if token is provided.
    Data is sent as json if nothing else is specified.
    Responses can be checked against an expected status code.
    """

    def open(self, *args, **kwargs):
        """Modified request.
        Adds token and headers and asserts status code.
        """
        # We are definetly going to add some headers
        if 'headers' not in kwargs:
            kwargs['headers'] = {}

        # Add token
        token = kwargs.pop('token', None)

        if token:
            kwargs['headers'].update({
                # We support a auth header of the form "Token <thetoken>"
                'Authorization': 'Token ' + token
            })

        # Add content-type: json header if nothing else is provided
        if (not("content-type" in kwargs['headers']) and
                ("data" in kwargs)):
            # Parse data
            kwargs['data'] = json.dumps(kwargs['data'])
            # Set header
            kwargs['content_type'] = "application/json"

        # get the actual response and assert status
        expected_code = kwargs.pop('status_code', None)

        response = super().open(*args, **kwargs)

        status_code = response.status_code

        if (expected_code is not None and expected_code != status_code):
            raise AssertionError(
                "Expected a status code of %i, but got %i instead\n"
                "Response:\n%s\n%s\n%s" % (expected_code, status_code,
                                           response, response.data,
                                           response.status))
        elif ((expected_code == 422) and
              ('exception' in response.json.get('_issues', {}))):
            # The validator swallows exceptions and turns them into 'exception'
            # validation errors. Ensure that tests do not miss this by raising
            # them properly.
            error = response.json['_issues']['exception']
            raise AssertionError("Expected a validation error but the "
                                 "validator raised an exception: %s" % error)

        return response


class TestResponse(Response):
    """Custom response to ease JSON handling."""

    @property
    def json(self):
        """Return data in JSON."""
        return json.loads(self.data.decode())


class TestBase(unittest.TestCase):
    """Base test class for tests against the full WSGI stack without authentication
    Inspired by eve standard testing class.
    """

    # Test Config overwrites
    test_config = {
        'MONGO_HOST': 'localhost',
        'MONGO_PORT': 27099,
        'MONGO_DBNAME': 'test_db',
        'MONGO_USERNAME': 'test_user',
        'MONGO_PASSWORD': 'test_pw',
        'S3_HOST': 'localhost:9000',
        'S3_ACCESS_KEY': 'minio_access',
        'S3_SECRET_KEY': 'minio_secret',
        'S3_BUCKET': 'testbucket',
        'S3_SECURE_CONNECTION': False,
        'DOMAIN': {},
        'TESTING': True,
        'DEBUG': True,   # This makes eve's error messages more helpful
    }

    def setUp(self, **extra_config):
        """Set up the testing client and database connection.
        self.api will be a flask TestClient to make requests
        self.db will be a MongoDB database
        """
        super().setUp()

        # In 3.2, assertItemsEqual was replaced by assertCountEqual
        # Make assertItemsEqual work in tests for py3 as well
        if sys.version_info >= (3, 2):
            self.assertItemsEqual = self.assertCountEqual

        # create eve app and test client
        config = {}
        config.update(self.test_config)
        config.update(extra_config)
        self.app = eve.Eve(settings=config, media=S3MediaStorage)
        self.app.response_class = TestResponse
        # self.app.test_client_class = TestClient
        self.test_client = self.app.test_client()

        def authenticate_root(resource):
            g.resource_admin = True

        self.app.after_auth += authenticate_root

        # Create a separate mongo connection and db reference for tests
        self.connection = MongoClient(host=self.test_config['MONGO_HOST'],
                                      port=self.test_config['MONGO_PORT'])
        self.db = self.connection[self.test_config['MONGO_DBNAME']]
        self.db.authenticate(name=self.test_config['MONGO_USERNAME'],
                             password=self.test_config['MONGO_PASSWORD'],
                             source=self.test_config['MONGO_DBNAME'])

    def tearDown(self):
        """Tear down after testing."""
        # delete testing database
        self.connection.drop_database(self.test_config['MONGO_DBNAME'])
        # close database connection
        self.connection.close()

    def patch(self, url, data, headers=None):
        if headers is None:
            headers = []
        headers.append(("Content-Type", "application/json"))
        r = self.test_client.patch(url, data=json.dumps(data), headers=headers)
        return self.parse_response(r)

    def parse_response(self, r):
        try:
            v = json.loads(r.get_data())
        except json.JSONDecodeError:
            v = None
        return v, r.status_code
