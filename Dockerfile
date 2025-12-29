#######################################
# Base image and common dependencies  #
#######################################
FROM ubuntu:24.04
ARG PYTHON_VERSION=3.14

# Install common packages and add deadsnakes PPA for multiple Python versions
RUN apt-get update && \
    apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/*

# add user for building and running
RUN adduser omni

# copy files into the image
COPY . /pyomnidata
RUN chown omni:omni -R /pyomnidata

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python${PYTHON_VERSION} \
        python${PYTHON_VERSION}-venv \
        python${PYTHON_VERSION}-dev && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN chown omni: -R /app
USER omni
# Create a virtual environment, upgrade pip and install your package (editable mode)
RUN cd /app && python${PYTHON_VERSION} -m venv venv && \
    ./venv/bin/pip install --upgrade pip && \
    ./venv/bin/pip install setuptools wheel
CMD ["tail", "-f", "/dev/null"]
