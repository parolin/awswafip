# UpdateIPs_AWS_WAF
Insert or Delete a list of IPv4 addresses in the AWS WAF.

It makes use of python3 and boto3

It is available in pypitest (the test environment for pip). To install it via pypitest you can follow the steps below. If python3 and boto3 already installed you can skip to step 4.

1. Install python3 (if already installed you can skip this step)
sudo yum install python36 -y

2. Upgrade pip for python3 (if already upgrade or in a stable version, you can skip this step)
python3 -m pip install --upgrade pip;

3. Upgrade the boto3 for python3 (this step is need only when using pypitest, as the test environment does not have the latest boto3 version. As soon as it is moved to pip it will not be necessary)
python3 -m pip install --upgrade boto3;

4. Install the awswafip (if all
python3 -m pip install -i https://testpypi.python.org/pypi awswafip;

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
