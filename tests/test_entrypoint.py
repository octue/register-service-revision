import unittest
from unittest.mock import patch

import requests

from register_service_revision.entrypoint import register_service_revision


class TestEntrypoint(unittest.TestCase):
    def test_unsuccessful_registration_raises_error(self):
        """Test that an unsuccessful registration raises an error."""
        mock_response = requests.Response()
        mock_response.status_code = 400

        with patch("requests.post", return_value=mock_response):
            with self.assertRaises(requests.exceptions.HTTPError):
                register_service_revision(
                    namespace="my-org",
                    name="my-service",
                    revision_tag="0.1.0",
                    registry_endpoint="https://blah.com/services",
                )

    def test_successful_registration(self):
        """Test that a successful registration exits gracefully."""
        mock_response = requests.Response()
        mock_response.status_code = 201

        with patch("requests.post", return_value=mock_response):
            register_service_revision(
                namespace="my-org",
                name="my-service",
                revision_tag="0.1.0",
                registry_endpoint="https://blah.com/services",
            )
