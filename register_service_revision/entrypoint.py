import logging
import sys

import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def register_service_revision(namespace, name, revision_tag, registry_endpoint):
    """Register a service revision in the given registry.

    :param str namespace: the service namespace
    :param str name: the service name
    :param str revision_tag: the service revision tag
    :param str registry_endpoint: the URL of the service registry's service registration endpoint
    :return None:
    """
    logger.info(
        "Attempting to register service revision '%s/%s:%s' with registry %r.",
        namespace,
        name,
        revision_tag,
        registry_endpoint,
    )

    response = requests.post(f"{registry_endpoint.strip('/')}/{namespace}/{name}", json={"revision_tag": revision_tag})
    response.raise_for_status()


if __name__ == "__main__":
    namespace, name, revision_tag, registry_endpoint = sys.argv[1:5]
    register_service_revision(namespace, name, revision_tag, registry_endpoint)
