FROM python:3.12-slim

# install dependencies
COPY ci/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt 

# copy codebase
COPY src /src
WORKDIR /src

EXPOSE 8000

ENTRYPOINT [ "python3", "api_app.py" ]