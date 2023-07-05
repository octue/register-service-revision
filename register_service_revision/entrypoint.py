import sys

import requests


def register_service_revision(namespace, name, revision_tag, registry_endpoint):
    """Register a service revision in the given registry.

    :param str namespace: the service namespace
    :param str name: the service name
    :param str revision_tag: the service revision tag
    :param str registry_endpoint: the URL of the service registry's service registration endpoint
    :return None:
    """
    response = requests.post(
        registry_endpoint,
        json={
            "namespace": namespace,
            "name": name,
            "revision_tag": revision_tag,
        },
    )

    response.raise_for_status()


if __name__ == "__main__":
    namespace, name, revision_tag, registry_endpoint = sys.argv[1:5]
    register_service_revision(namespace, name, revision_tag, registry_endpoint)
