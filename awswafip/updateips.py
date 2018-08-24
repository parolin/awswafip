from aws_actions import *
from file_actions import *
from __init__ import *
global client

def get_parameters():
    regions_dict = {1: 'us-east-1',
                    2 : 'us-east-2',
                    3 : 'us-west-2',
                    4 : 'us-west-1',
                    5 : 'eu-west-1',
                    6 : 'eu-central-1',
                    7 : 'ap-northeast-1',
                    8 : 'ap-southeast-2'
                    }
    try:
        param_new_ipset = input('Is it a new IpSet? (Y/N)\n').upper()
        if param_new_ipset == 'Y':
            param_ipset = input('Enter the IPSet name to be created:\n')
        elif param_new_ipset == 'N':
            param_ipset = input('Enter the name of the IPSet you want to update:\n')
        else:
            raise ValueError

        param_global_regional = int(input('Is the IPSet for WAF (with CloudFront) or WAF Regional (with ALB)?\n'
                                '(1) WAF\n'
                                '(2) WAF Regional\n'
                                ))
        if param_global_regional == 1:
            param_region = 'us-east-1'
        elif param_global_regional == 2:
            param_region = int(input('Please select the region for your WAF Regional: \n'
                                    '(1) Northern Virginia / us-east-1 \n'
                                    '(2) Ohio / us-east-2 \n'
                                    '(3) Oregon / us-west-2 \n'
                                    '(4) Northern California / us-west-1 \n'
                                    '(5) Ireland / eu-west-1 \n'
                                    '(6) Frankfurt / eu-central-1 \n'
                                    '(7) Tokyo / ap-northeast-1 \n'
                                    '(8) Sydney / ap-southeast-2 \n'
                                    ))
            if 1 <= param_region <= 8:
                param_region = regions_dict[param_region]
            else:
                raise ValueError

        else:
            raise ValueError

        param_action = int(input('What is the action desired? \n(1) Insert\n(2) Delete\n'))
        if param_action == 1:
            param_action = 'INSERT'
        elif param_action == 2:
            param_action = 'DELETE'
        else:
            raise ValueError

        param_file = input('Enter the file location containing the list of IPs: \n')

    except ValueError as e:
        print('Please enter a correct Value!')
        exit(0)

    return param_new_ipset, param_ipset, param_global_regional, param_region, param_action, param_file


def check_limits(list_ips, action):
    if action == "INSERT":
        if len(list_ips) > 10000:
            print("The amount of IPs to be added in the IPSet is above the AWS Limit (10,000 IPs per IPSet)")
            print("Please check the link for details https://docs.aws.amazon.com/waf/latest/developerguide/limits.html")
            exit(0)
    status_limits = True
    return status_limits


def format_response(raw_response):
    print("Request ID: {0}".format(raw_response['ResponseMetadata']['RequestId']))
    print("HTTP Response Code: {0}".format(raw_response['ResponseMetadata']['HTTPStatusCode']))
    if raw_response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Request Successful - IP Address Condition update successfully")
    else:
        print("Response Code not expected (expected 200)- check your IP Address condition for confirmation")
    print("Change Token: {0}".format(raw_response['ChangeToken']))


if __name__ == "__main__":
    new_ipset, ipset, global_regional, region, action, file = get_parameters()

    if global_regional == 2:
        define_client('waf-regional', region)

    if new_ipset == "Y":
        ipset_id = create_ipset(ipset)
    elif new_ipset == "N":
        ipset_id = get_ipset_id(ipset)

    list_ips = get_ips_from_file(file)

    check_limits = check_limits(list_ips, action)

    if check_limits:
        response_update = update_ipset(list_ips, action, ipset_id)
        format_response(response_update)

##############################
##############################
##############################


#need to test if the return response is not breaking the exceptio and retry
#add pip install

#done
#need to validate response and show if successful or not
#region validator
#check limits = check if waf supported in this region (not need, only specific regions informed)
# Northern Virginia = us-east-1
# Ohio = us-east-2
# Oregon = us-west-2
# Northern California = us-west-1
# Ireland = eu-west-1
# Frankfurt = eu-central-1
# Tokyo = ap-northeast-1
# Sydney = ap-southeast-2
