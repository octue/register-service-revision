import unittest
from unittest.mock import patch

import requests

from register_service_revision.entrypoint import register_service_revision


class TestEntrypoint(unittest.TestCase):
    def test_unsuccessful_registration_raises_error(self):
        """Test that an unsuccessful registration raises an error."""
        mock_response = requests.Response()
        mock_response.status_code = 400

        with patch("requests.post", return_value=mock_response) as mock_post:
            with self.assertRaises(requests.exceptions.HTTPError):
                register_service_revision(
                    namespace="my-org",
                    name="my-service",
                    revision_tag="0.1.0",
                    registry_endpoint="https://blah.com/services",
                )

        mock_post.assert_called_with("https://blah.com/services/my-org/my-service", json={"revision_tag": "0.1.0"})

    def test_successful_registration(self):
        """Test that a successful registration exits gracefully."""
        mock_response = requests.Response()
        mock_response.status_code = 201

        for registry_endpoint in ("https://blah.com/services", "https://blah.com/services/"):
            with self.subTest(registry_endpoint=registry_endpoint):
                with patch("requests.post", return_value=mock_response) as mock_post:
                    register_service_revision(
                        namespace="my-org",
                        name="my-service",
                        revision_tag="0.1.0",
                        registry_endpoint=registry_endpoint,
                    )

                mock_post.assert_called_with(
                    "https://blah.com/services/my-org/my-service",
                    json={"revision_tag": "0.1.0"},
                )

    def test_with_is_default_specified_as_true(self):
        """Test that setting `is_default` as `True` works."""
        mock_response = requests.Response()
        mock_response.status_code = 201

        for is_default in ("true", "True", "TRUE"):
            with self.subTest(is_default=is_default):
                with patch("requests.post", return_value=mock_response) as mock_post:
                    register_service_revision(
                        namespace="my-org",
                        name="my-service",
                        revision_tag="0.1.0",
                        registry_endpoint="https://blah.com/services",
                        is_default=is_default,
                    )

                mock_post.assert_called_with(
                    "https://blah.com/services/my-org/my-service",
                    json={"revision_tag": "0.1.0", "is_default": True},
                )

    def test_with_is_default_specified_as_false(self):
        """Test that setting `is_default` as `False` works."""
        mock_response = requests.Response()
        mock_response.status_code = 201

        for is_default in ("false", "False", "FALSE"):
            with self.subTest(is_default=is_default):
                with patch("requests.post", return_value=mock_response) as mock_post:
                    register_service_revision(
                        namespace="my-org",
                        name="my-service",
                        revision_tag="0.1.0",
                        registry_endpoint="https://blah.com/services",
                        is_default=is_default,
                    )

                mock_post.assert_called_with(
                    "https://blah.com/services/my-org/my-service",
                    json={"revision_tag": "0.1.0", "is_default": False},
                )
