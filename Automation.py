import boto3

# EC2 resource
ec2 = boto3.resource("ec2", region_name="us-east-1")

def launch_ec2():
    print("\nLaunching EC2 instance...")

    response = ec2.create_instances(
        ImageId="ami-0fa3fe0fa7920f68e",
        MinCount=1,
        MaxCount=1,
        InstanceType="t3.micro",
        KeyName="public",
    )

    instance_id = response[0].id
    print("EC2 Launched Successfully!")
    print("Instance ID:", instance_id)


def stop_ec2():
    instance_id = input("\nEnter Instance ID to STOP: ")
    print(f"Stopping instance {instance_id}...")
    ec2.instances.filter(InstanceIds=[instance_id]).stop()
    print("Instance Stopped!")


def start_ec2():
    instance_id = input("\nEnter Instance ID to START: ")
    print(f"Starting instance {instance_id}...")
    ec2.instances.filter(InstanceIds=[instance_id]).start()
    print("Instance Started!")


def terminate_ec2():
    instance_id = input("\nEnter Instance ID to TERMINATE: ")
    print(f"Terminating instance {instance_id}...")
    ec2.instances.filter(InstanceIds=[instance_id]).terminate()
    print("Instance TERMINATED!")


def menu():
    while True:
        print("\n=========== AWS EC2 Automation Menu ===========")
        print("1. Launch EC2")
        print("2. Stop EC2")
        print("3. Start EC2")
        print("4. Terminate EC2")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            launch_ec2()
        elif choice == "2":
            stop_ec2()
        elif choice == "3":
            start_ec2()
        elif choice == "4":
            terminate_ec2()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again!")


if __name__ == "__main__":
    menu()
