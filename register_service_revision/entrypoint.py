import logging
import sys

import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def register_service_revision(namespace, name, revision_tag, registry_endpoint, is_default=None):
    """Register a service revision in the given registry.

    :param str namespace: the service namespace
    :param str name: the service name
    :param str revision_tag: the service revision tag
    :param str registry_endpoint: the URL of the service registry's service registration endpoint
    :param str|None is_default: whether the service revision should be set as the default for its service - should be either the string "true" or "false"
    :return None:
    """
    logger.info(
        "Attempting to register service revision '%s/%s:%s' with registry %r.",
        namespace,
        name,
        revision_tag,
        registry_endpoint,
    )

    body = {"revision_tag": revision_tag}

    if is_default:
        if is_default.lower() == "true":
            is_default = True
        elif is_default.lower() == "false":
            is_default = False

        body["is_default"] = is_default

    response = requests.post(f"{registry_endpoint.strip('/')}/{namespace}/{name}", json=body)
    response.raise_for_status()


if __name__ == "__main__":
    namespace, name, revision_tag, registry_endpoint, is_default = sys.argv[1:6]
    register_service_revision(namespace, name, revision_tag, registry_endpoint, is_default)
