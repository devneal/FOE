sudo apt-get update && sudo apt-get -y install \
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
sudo dpkg --add-architecture i386 && sudo apt-get update && sudo apt-get -y install \
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


pip install --upgrade pip
pip install --user --upgrade \
   ipdb \
   ipython \
   virtualenv \

mkdir tools
pushd tools

# pwntools
pip install --user --upgrade pwntools

# checksec
mkdir checksec
pushd checksec
wget http://www.trapkit.de/tools/checksec.sh
popd # tools

# pwndbg
git clone https://github.com/pwndbg/pwndbg
pushd pwndbg
sudo ./setup.sh
# Set the locale
sudo locale-gen en_US.UTF-8
popd # tools

# one_gadget
sudo gem install one_gadget

popd
. env.sh
