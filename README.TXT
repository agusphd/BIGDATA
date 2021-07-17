1. OS:
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.2 LTS
Release:	20.04
Codename:	focal

2. Install Pycharm
sudo snap install pycharm-community --classic
pycharm-community

3. Python 3+

4. pip install -r requirements.txt

5. MongoDB

5.1. Install Mongo ubuntu  > sh mongoinstallubuntu.sh
~$ cat mongoinstallubuntu.sh

#!/bin/sh
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-org-shell hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections

5.2. ~$ sudo service mongod start



5.3. Install MongoDB Compass
https://www.mongodb.com/try/download/compass?tck=docs_compass


5.4. ~$mongo  > show dbs > use dbs > show collections


6. MPI: Ubuntu
~$ sudo apt-get install libopenmpi-dev python-dev python3-dev
~$ wget https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-3.0.0.tar.gz
~$ tar -zxf mpi4py-3.0.0.tar.gz
~$ cd mpi4py-3.0.0/
~$ sudo python3 setup.py build
~$ sudo python3 setup.py install
~$ mpiexec -n 5 python helloworld.py

cat helloworld.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
print(size,rank)

7. Link to Data:
https://drive.google.com/drive/u/1/folders/1I6fkdq3HUAHVVJX5jZ_9cwsuN6yD-Uiu
