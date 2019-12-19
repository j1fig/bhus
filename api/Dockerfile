FROM python:3.7-slim-stretch
# Here we trade a bigger image for better build times.
# Building from Alpine would yield a smaller image size, yet longer build times.

WORKDIR /src
COPY requirements.txt ./
RUN apt-get update && apt-get install -y build-essential
RUN pip install --no-cache-dir -r requirements.txt
COPY entrypoint.sh /src/
RUN chmod +x /src/entrypoint.sh
# We keep the copying of your code as far through the dockerfile as possible, to allow for speedier builds when we're just making code changes.
COPY . .

ENTRYPOINT ["/src/entrypoint.sh"]
CMD ["run"]
EXPOSE 8000
