# demo-python-falcon-statsd
Deploy a Falcon application that uses statsd to store business metrics

## Configuration

You will need the following environment variables:

```
CC_PYTHON_MODULE=server:api
ENABLE_METRICS=true
PORT=8080
PYTHON_BACKEND=gunicorn
```
