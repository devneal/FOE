FROM ubuntu:latest


RUN apt-get update && apt-get -y install \
   build-essential \
   gdb \
   gdbserver \
   gdb-multiarch \
   git \
   emacs \
   libcapstone3 \
   libc6-dbg \
   libffi-dev \
   libssl-dev \
   locales \
   ltrace \
   man-db \
   netcat \
   net-tools \
   openssh-server \
   python2.7 \
   python-pip \
   python-dev \
   rubygems \
   socat \
   strace \
   sudo \
   tmux \
   unp \
   vim-nox \
   wget \
   valgrind \
   zip

# 32-bit
RUN dpkg --add-architecture i386 && apt-get update && apt-get -y install \
   libc6:i386 \
   libc6-dbg:i386 \
   libexpat1:i386 \
   libffi6:i386 \
   libfontconfig1:i386 \
   libfreetype6:i386 \
   libgcc1:i386 \
   libglib2.0-0:i386 \
   libice6:i386 \
   libpcre3:i386 \
   libpng12-0:i386 \
   libsm6:i386 \
   libstdc++6:i386 \
   libuuid1:i386 \
   libx11-6:i386 \
   libxau6:i386 \
   libxcb1:i386 \
   libxdmcp6:i386 \
   libxext6:i386 \
   libxrender1:i386 \
   zlib1g:i386 \
   libx11-xcb1:i386 \
   libdbus-1-3:i386 \
   libxi6:i386 \
   libsm6:i386 \
   libcurl3:i386

# user account
RUN useradd -m user
RUN usermod -s /bin/bash user
ENV SHELL /bin/bash
ENV HOME /home/user
RUN echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN echo 'Defaults env_keep = "http_proxy https_proxy ftp_proxy DISPLAY XAUTHORITY"' >> /etc/sudoers
USER user

RUN pip install --upgrade pip
RUN pip install --user --upgrade \
   ipdb \
   ipython \
   virtualenv \
   virtualenvwrapper

RUN echo "source /home/user/.local/bin/virtualenvwrapper.sh" >> ~/.bashrc

RUN mkdir /home/user/tools
WORKDIR /home/user/tools

# pwntools
RUN pip install --user --upgrade pwntools

# checksec
RUN mkdir /home/user/tools/checksec
WORKDIR /home/user/tools/checksec
RUN wget http://www.trapkit.de/tools/checksec.sh
RUN echo "export PATH=$PATH:/home/user/tools/checksec" >> ~/.bashrc

# pwndbg
WORKDIR /home/user/tools
RUN git clone https://github.com/pwndbg/pwndbg
WORKDIR /home/user/tools/pwndbg
RUN ./setup.sh
# Set the locale
RUN sudo locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN sudo gem install one_gadget

WORKDIR /home/user/
ENV EDITOR vim
RUN echo "export PATH=$PATH:/home/user/.local/bin" >> ~/.bashrc

CMD bash
