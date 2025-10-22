FROM python:3.12

# Avoid interactive prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# ENV USERNAME=canuebun
# ARG USERNAME
ENV USERNAME=user
ENV HOME=/logs/work/${USERNAME}

RUN apt-get update && \
    apt-get install software-properties-common -y

RUN add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update && \
    apt-get install -y sudo

RUN useradd -ms /bin/bash ${USERNAME} && \
    usermod -aG sudo ${USERNAME}

# Set working directory in container
WORKDIR ${HOME}

# Copy entire repo into container
COPY . .
RUN chown -R ${USERNAME}:${USERNAME} ${HOME}

# COPY tools/infra/data/.bashrc ${HOME}/

COPY tools/infra/data/.bashrc /tmp/my-bashrc
RUN mv /tmp/my-bashrc ${HOME}/.bashrc

########################################################
# STANDARD PACKAGES
# Install system and Python dependencies
RUN apt-get install -y \
    build-essential \
    git \
    curl \
    unzip \
    zip \
    vim \
    ca-certificates \
    gnupg \
    python3.12 \
    python3.12-dev \
    python3.12-venv \
    libffi-dev \
    less \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    bash-completion \
    libcurl4-openssl-dev \
    clang \
    gcc \
    pre-commit \
    sqlite3 \
    libsqliteodbc \
    lcov \
    && rm -rf /var/lib/apt/lists/*
########################################################

# Non standard packs
############################
# SQL Server tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools18 unixodbc-dev
############################
# Bazel
RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor -o /usr/share/keyrings/bazel-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" > /etc/apt/sources.list.d/bazel.list && \
    apt-get update && \
    apt-get install -y bazel
########################################################


RUN python3.12 -m pip install --upgrade pip setuptools wheel cython && \
    python3.12 -m pip install -r requirements.txt && \
    pre-commit install

USER ${USERNAME}

CMD ["/bin/bash"]
