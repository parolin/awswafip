# UpdateIPs_AWS_WAF
Insert or Delete a list of IPv4 addresses in the AWS WAF.

It makes use of python3 and boto3

It is available in through pip. To install it via pip you can follow the steps below. If python3 and boto3 already installed you can skip to step 3.

1. Install python3 (if already installed you can skip this step)
sudo yum install python36 -y

2. Upgrade pip for python3 (if already upgrade or in a stable version, you can skip this step). It can be done via pip3
pip3 install --upgrade pip3

or loading it via python
python3 -m pip install --upgrade pip;

3. Install the awswafip 
pip3 install awswafip

or 

python3 -m pip install awswafip;


Also, if you want, you can clone and run it from the clone directory:
git clone https://github.com/parolin/awswafip.git; cd awswafip

pip install -e .

After installing

To run just type: awswafip

It will ask you the following information:
If the IPSet already exist or if you want to create a new one.
The name of IPSet. If it is a new IPSet, it will automatically create a new IPSet for you
The location of the file that contain the IPs
If you want to insert or delete the IPs from the IPSet

At the moment, it only works with IPv4. IPv6 version is in progress.

The file with IPs, need to have one IP per line, as in the example below:

10.10.10.10/32

192.168.10.0/24

192.168.1.128/25

172.16.0.0/16
