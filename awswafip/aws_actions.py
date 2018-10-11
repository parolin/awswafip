import math
import time
import boto3

API_CALL_NUM_RETRIES = 3

global client

client = boto3.client('waf', region_name="us-east-1")


def define_client(waf_type, region):
    global client
    client = boto3.client(waf_type, region_name=region)


def create_ipset(new_ipset):
    change_token = get_change_token()
    for retries in range(API_CALL_NUM_RETRIES):
        try:
            print("Creating the IPSet {0}".format(new_ipset))
            response = client.create_ip_set(
                Name=new_ipset,
                ChangeToken=change_token
            )
            return response['IPSet']['IPSetId']
        except Exception as e:
            print(e)
            exp_backoff = math.pow(2, retries)
            print("Retrying in {0} seconds ".format(exp_backoff))
            time.sleep(exp_backoff)


def update_ipset(list_ip, action, ipset_id):
    updates_tobe = []
    for x in list_ip:
        temp_dict = {
            'Action': action,
            'IPSetDescriptor': {
                'Type': 'IPV4',
                'Value': x
            }
        }
        updates_tobe.append(temp_dict)
    change_token = get_change_token()

    for retries in range(API_CALL_NUM_RETRIES):
        try:
            print("Updating IP Address Condition...")
            response_update = client.update_ip_set(
                IPSetId=ipset_id,
                ChangeToken=change_token,
                Updates=updates_tobe
            )
            return response_update
        except Exception as e:
            print(e)
            exp_backoff = math.pow(2, retries)
            print("Retrying in {0} seconds ".format(exp_backoff))
            time.sleep(exp_backoff)
    else:
        print("Failed all attempts to update the IPSet List")
        exit(0)


def get_ipset_id(ipset):
    list_all_ipsets = client.list_ip_sets(
        Limit=99
    )
    ipset_created = False

    print("Getting IPSet ID for the IPSet {0}".format(ipset))

    for ipsets in list_all_ipsets['IPSets']:
        if ipsets['Name'] == ipset:
            response_ip_set_id = ipsets['IPSetId']
            ipset_created = True

    if ipset_created == True:
        print('IPSet found')
        return response_ip_set_id
    else:
        print('IPSet Name {0} informed does not exist'.format(ipset))
        exit(0)


def get_change_token():
    response_token = client.get_change_token()
    return response_token['ChangeToken']
