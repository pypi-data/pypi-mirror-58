# What is CodeReef client

CodeReef client allows you to communicate with [CodeReef portal](https://codereef.ai/portal) 
from your machine to manage, build, run and benchmark AI workflows.

# Installation

## Prerequisites

CodeReef requires minimal dependencies (Python 2.7+ or 3.x, PIP and Git) 
and should be able to run on Linux, MacOS, Windows.
We are developing clients for Android and iOS too.

We plan to create a self-containing and self-installing package in the future.
In the mean time, you can install pre-requisites as described [here](https://github.com/ctuning/ck#installation).

When ready, you should also install virtualenv as follows:
```
 python -m pip install virtualenv (--user)
    or
 python3 -m pip install virtualenv (--user)
```

Note that you can run CodeReef client from Virtual Machines.
We tested CodeReef with Windows Subsystem Linux 
(enable it in "Windows Features" and install Ubuntu 18.04 from Apps store) 
and Docker (```docker run -p 4444:4444 -it {Docker Image} "/bin/bash"```).


```
 git clone https://github.com/code-reef/client

 python -m setup.py install
   or
 python3 -m setup.py install

```

Note that CK should be automatically installed too unless you already have it installed.

You can now install several CK repositories required by the CodeReef client:

```
 ck pull repo --url=https://github.com/code-reef/ck-codereef-client
 ck pull repo:ck-env
```

You can now test that cr works:
```
 cr
```

## Setting up your user credentials to communicate with CodeReef.ai

```
 cr setup --username={Your CodeReef.ai portal username} \
          --api_key={Your CodeReef.ai API key}
```

## Preparing specific python version for virtual env

We often need different python versions for virtual environments
(unless a user version must be used which is also possible
but may make shared workflows fail).

Our current demos are tested with Python 3.6.3.
If you don't have python 3.6, you should install one.
You will need it later with you initialize CodeReef solution

### On Windows:

Download installer of the correct version from https://www.python.org/downloads :

```
wget https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe
```

Install to a specific directory {PYTHON_PATH}.
You will need it later with you initialize CodeReef solution.

### On Linux:

Note that you may want to rebuild a specific version (it's relatively fast: 5..10 minutes).

However, you must check that you have ssl and zlib packages. You can install them on Ubuntu as follows:

```
 sudo apt install libssl-dev zlib1g-dev
```

or compile it from [sources](https://www.openssl.org/source/): 

```
 mkdir python
 cd python

 wget https://www.openssl.org/source/openssl-1.0.2t.tar.gz

 gzip -d openssl-1.0.2t.tar.gz
 tar xvf openssl-1.0.2t.tar

 cd openssl-1.0.2t
 ./config --prefix=$PWD/.. shared

 make -j4
 make install

 cd ..

 wget https://www.zlib.net/zlib-1.2.11.tar.gz
 gzip -d zlib-1.2.11.tar.gz
 tar xvf zlib-1.2.11.tar

 cd zlib-1.2.11
 ./configure --prefix=$PWD/..

 make
 make install

```

Download source codes of the correct Python version from https://www.python.org/downloads .

```
 wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
 
 gzip -d Python-3.6.9.tgz
 tar xvf Python-3.6.9.tar

 cd Python-3.6.9

 export LDFLAGS="-L$PWD/../lib/"
 export LD_LIBRARY_PATH="$PWD/../lib/"
 export CPPFLAGS="-I$PWD/../include/ -I$PWD/../include/openssl/"
 
 ./configure --prefix=$PWD/.. --enable-optimizations 

 make -j4
 make install
```

 Remember path to the new python: $PWD/bin/python3.6

### On MacOS:

To be tested: maybe it's possible to install specific version such as python3.6 via brew.

Otherwise install openssl and recompile as above:
```
 brew install openssl
```










# Using different types of machines to run workflows

## Running CUDA-based object detection from the laptop

* https://dev.codereef.ai/portal/c/cr-solution/demo-obj-detection-kitti-0009-tf-cuda-win/?refresh_rate=100
* https://dev.codereef.ai/portal/c/cr-solution/demo-obj-detection-kitti-0009-tf-cuda-win/?refresh_rate=100&jpeg=yes

## Running CodeReef solutions on external hosts

You can not use non-SSL client on remote host. 

However, you can create a secure virtual host using Apache2
and redirect traffic to CodeReef client.

Add port 4444 to /etc/apache2/ports.conf:

```
<IfModule ssl_module>
        Listen 443
        Listen 4444
</IfModule>

<IfModule mod_gnutls.c>
        Listen 443
        Listen 4444
</IfModule>

```

Add new VirtualHost to your default-ssl.conf:

```
        </VirtualHost>

        <VirtualHost _default_:4444>
                ServerAdmin admin@cknowledge.org

                ServerName codereef.io
                ServerAlias www.codereef.io

                ProxyPreserveHost On
                ProxyRequests Off
                ProxyPass / http://{YOUR INTERNAL IP}:4445
                ProxyPassReverse / http://{YOUR INTERNAL IP}:4445

```


Install dependencies and restart apache2:
```
sudo a2enmod proxy && sudo a2enmod proxy_http && sudo service apache2 restart
```

Run CodeReef client on port 4445:
```
cr start -h 0.0.0.0 -p 4445
```
Now you should be able to access CodeReef client via https://{YOU APACHE2 host}:4444

You can then test how it works at https://dev.codereef.ai/portal/c/cr-solution/demo-obj-detection-kitti-0009-tf-cpu-linux-azure/?jpeg=yes&jpeg_quality=40&refresh_rate=400
