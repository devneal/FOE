## Setup

### Docker
If you already have docker installed running the following will build a foe image and 
put you into an interactive session with `$PWD/..` mounted (like a shared dir) at /home/user/foe:
```
sh docker_run.sh
```


### setup.sh (experimental)
If you are using a VM or want to install directly to an Ubuntu host,
running the following should install all the dependencies:
```
source setup.sh # (Use at your own risk :D)
```
