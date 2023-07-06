FROM python:3.10.7-slim

# Install via `.zip` file to avoid having to add `git` to image.
RUN pip install https://github.com/octue/register-service-revision/archive/0.1.0.zip

COPY register_service_revision/entrypoint.py /entrypoint.py

RUN chmod +x entrypoint.py

ENTRYPOINT ["python", "/entrypoint.py"]
