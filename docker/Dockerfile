FROM vyahello/cli-snakegame-base:0.1.0
LABEL version=0.1.0 \
      metadata="The main image for smnakegame cli application" \
      maintainer="Volodymyr Yahello <vyahello@gmail.com>"
ARG VERSION
ENV CODE_DIR="/app" \
    IMAGE_VERSION=${VERSION}
WORKDIR ${CODE_DIR}
COPY snake snake
COPY requirements.txt docker/snake-entry.sh ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt
ENTRYPOINT ["python", "-m", "snake"]
