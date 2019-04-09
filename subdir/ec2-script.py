import   boto3
session=boto3.Session(profile_name='Thinkpad',region_name='us-east-1')
ec2=session.resource('ec2')
for i in ec2.instances.all():
    print("There is a an i nstance {0}".format(i))