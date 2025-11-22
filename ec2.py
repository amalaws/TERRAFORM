import boto3

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

    print("EC2 Launched Successfully!")
    print("Instance created with ID:", response[0].id)


def terminate_ec2():
    print("\nTerminating EC2 instance...")
    instance_id = input("Enter Instance ID to TERMINATE: ")

    ec2.instances.filter(InstanceIds=[instance_id]).terminate()

    print("EC2 TERMINATED:", instance_id)


def menu():
    while True:
        print("\n=========== AWS EC2 Automation ===========")
        print("1. Launch EC2")
        print("2. Terminate EC2")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            launch_ec2()
        elif choice == "2":
            terminate_ec2()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
