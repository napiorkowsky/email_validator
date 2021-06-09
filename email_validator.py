from pyisemail import is_email

with open('adresy.txt','r') as f:
    for line in f:
        address=line.rstrip()
        detailed_result_with_dns = is_email(address, check_dns=True, diagnose=True)
        print(address, ";", detailed_result_with_dns, sep="")
