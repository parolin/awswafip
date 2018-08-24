# AWS WAF IP
Insert or Delete a list of IPv4 addresses in the AWS WAF.

It makes use of python3 and boto3, so before you continue, you need to have both installed in your system.

For Amazon Linux you may use the following commands to install python3 and boto3.

sudo yum install python36

sudo python3 -m pip install boto3

After the installation, you can just run the command
To run just type: python3 updateIPs.py

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
