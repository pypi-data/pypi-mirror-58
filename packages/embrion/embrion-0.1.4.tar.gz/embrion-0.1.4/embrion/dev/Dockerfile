
FROM ubuntu:latest
# ARG ENV_NAME=embrion
# RUN conda create --name ${ENV_NAME}

LABEL maintainer="Izel Levy <izel93@gmail.com>"

RUN apt-get update
RUN apt-get install -y wget git tmux
RUN apt-get install -y vim

# -- ZSH --
RUN apt-get install -y zsh
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN sed -i -E 's/ZSH_THEME="(.*?)"/ZSH_THEME="agnoster"/' ~/.zshrc
# Required for zsh fonts to work properly.
RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8

# -- MINICONDA --
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-4.6.14-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.zshrc && \
    rm -r /opt/conda/pkgs/

ENV PATH="/opt/conda/bin:$PATH"

# -- VS CODE --
ARG BUILD_VERSION=1.1119-vsc1.33.1
ARG BUILD_OS=linux-x64

RUN wget https://github.com/cdr/code-server/releases/download/${BUILD_VERSION}/code-server${BUILD_VERSION}-${BUILD_OS}.tar.gz -O ~/code-server-build.tar.gz && \
    mkdir ~/code-server-build && \
    tar xf ~/code-server-build.tar.gz -C ~/code-server-build && \
    mv ~/code-server-build/code-server${BUILD_VERSION}-${BUILD_OS}/code-server ~ && \
    rm -r ~/code-server-build && \
    rm ~/code-server-build.tar.gz

RUN apt-get update && apt-get install -y \
	openssl \
	net-tools \
    curl

# -- SSH-SERVER --

# Change password root
RUN echo "root:embrion"|chpasswd

RUN apt-get -y install openssh-server
RUN mkdir -p /var/run/sshd

# Authorize SSH connection with root account
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config


COPY . /embrion

# Change the shell from now on use zsh.
SHELL ["zsh", "-c"]

# SERVER CONFIGURATION
ARG CONTAINER_ALREADY_STARTED="CONTAINER_ALREADY_STARTED_PLACEHOLDER"

RUN touch /tmp/${CONTAINER_ALREADY_STARTED}

RUN echo "-- Installing embrion development environment --"
RUN conda env create -f /embrion/dev/environment.yml
RUN echo "-- Done: Installing embrion development environment --"

RUN echo "-- Installing jupyterlab extensions --"
RUN . /opt/conda/etc/profile.d/conda.sh && \
conda activate $(cat /embrion/dev/environment.yml | grep -oP '^name:\s*\K(\S+)(?=\s*$)') && \
jupyter labextension install "@lckr/jupyterlab_variableinspector" && \
jupyter labextension install "@jupyterlab/debugger" && \
conda deactivate
RUN echo "-- Done: Installing jupyterlab extensions --"

RUN echo "-- Removing password for jupyter login --"
RUN mkdir ~/.jupyter
RUN touch ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "-- Done: Removing password jupyter login --"

RUN touch /tmp/environment.yml

# /SERVER CONFIGURATION

WORKDIR /app


EXPOSE 22
EXPOSE 8888
EXPOSE 8443


#ENTRYPOINT ["/embrion/dev/startup.sh"]

# docker build --tag embrion:0.1 --build-arg ENV_NAME=embrion .
# docker build --tag embrion:0.1 .
