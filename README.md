# AWS WAF IP
Insert or Delete a list of IPv4 addresses in the AWS WAF.

## Introduction
It makes use of python3 and boto3.

Python 2.x is not supported as the EOL (End of Life) was already confirmed: https://www.python.org/dev/peps/pep-0373/

It take a file containing the IP addresses, and add it in an IPSet Condition in AWS WAF. The IPs need to be listed in CIDR notation and one per line.

At the moment it works in a wizard format, asking questions about your WAF and the file location that contains the IP.

## System Pre-Requisites

1. Have python3 installed
`sudo yum install python36 -y`

2. Have pip3 updated
`pip3 install --upgrade pip3`


## Installation 

`pip3 install awswafip`

### From source

`git clone https://github.com/parolin/awswafip.git; cd awswafip`

`pip install -e .`

## Running awswafip

To run just type: awswafip

It will ask you the following information:
* If the IPSet already exist or if you want to create a new one.
* The name of IPSet. If it is a new IPSet, it will automatically create a new IPSet for you
* The location of the file that contain the IPs
* If you want to insert or delete the IPs from the IPSet


## Limitations and New features
* At the moment, it only works with IPv4. IPv6 version is in progress.

* The file with IPs, need to have one IP per line, as in the example below:

   10.10.10.10/32  
   192.168.10.0/24  
   192.168.1.128/25  
   172.16.0.0/16  
   
  * CSV format is in progress
