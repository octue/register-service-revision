# octue/register-service-revision

A GitHub action that registers a revision of an Octue service in a service registry.

## Usage

To automatically register your service revision on e.g. pull request merge / package release, add the following to your
GitHub Actions workflow:

```yaml
steps:
  - uses: actions/checkout@v3

  - name: Get package version
    id: get-package-version
    run: echo "PACKAGE_VERSION=$(poetry version -s)" >> $GITHUB_OUTPUT
    # run: echo "PACKAGE_VERSION=$(python setup.py --version)" >> $GITHUB_OUTPUT  <- Use this instead if your package uses a `setup.py` file.

  - name: Register service revision
    uses: octue/register-service-revision@0.1.1
    with:
      service_namespace: my-org
      service_name: my-service
      service_revision_tag: ${{ steps.get-package-version.outputs.PACKAGE_VERSION }}
      service_registry_endpoint: https://example.com/services
```
