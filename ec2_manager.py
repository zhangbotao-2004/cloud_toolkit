import sys
import boto3
from moto import mock_aws
import time

def create_instance(ec2):
    print("正在创建 EC2 实例...")
    instance = ec2.run_instances(
        ImageId='ami-12345678',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    instance_id = instance['Instances'][0]['InstanceId']
    print(f"✅ 实例创建成功，ID: {instance_id}")
    return instance_id

def list_instances(ec2):
    response = ec2.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            print(f"ID: {i['InstanceId']}, 状态: {i['State']['Name']}")

def stop_instance(ec2, instance_id):
    print(f"正在停止实例 {instance_id}...")
    ec2.stop_instances(InstanceIds=[instance_id])
    time.sleep(1)
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    print(f"📌 停止后状态: {state}")

def start_instance(ec2, instance_id):
    print(f"正在启动实例 {instance_id}...")
    ec2.start_instances(InstanceIds=[instance_id])
    time.sleep(1)
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    print(f"📌 启动后状态: {state}")

@mock_aws
def run_mock():
    ec2 = boto3.client('ec2', region_name='ap-southeast-2')
    
    print("\n" + "=" * 40)
    print("开始 EC2 实例管理模拟")
    print("=" * 40)
    
    instance_id = create_instance(ec2)
    
    print("\n📋 当前所有实例：")
    list_instances(ec2)
    
    stop_instance(ec2, instance_id)
    start_instance(ec2, instance_id)
    
    print("\n" + "=" * 40)
    print("✅ 模拟完成！")
    print("=" * 40)

def show_help():
    print("用法: python3 ec2_manager.py [选项]")
    print("  mock    - 模拟完整流程（创建→列表→停止→启动）")
    print("  help    - 显示帮助信息")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)
    
    action = sys.argv[1]
    if action == "mock":
        run_mock()
    else:
        show_help()