# CloudFormation Template for AWS VPC and EFS

## Introduction

Today I decided to start by looking at CloudFormation templates in AWS which I've never used before. In the last few months I've had to create EKS Clusters several times and I am looking to save time by automating that as much as possible. AWS have some templates in their [doc](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html) which speeds things up but I also wanted to create templates for setting up EFS correctly. 

## Use Case

The reason I'm doing this is to make it faster and easier for me (and possibly colleagues) in the future to quickly provision the required AWS infrastructure for FME Server in EKS.

## Cloud Research

I started today by doing some lessons from the 'Intro to AWS CloudFormation' course from http://acloudguru.com/.
I found this page in the AWS doc which is the [CloudFormation Template Reference for EFS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html). I changed the AccessPointResource to match what FME Server requires. 

## ☁️ Cloud Outcome

I was successful in getting the EFS set up based on AWS' example. However, they create their own VPC and Subnets, so I wanted to merge it into one template with the VPC creation template in [Step 1](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html). Their VPC yaml file is available [here](https://s3.us-west-2.amazonaws.com/amazon-eks/cloudformation/2020-10-29/amazon-eks-vpc-private-subnets.yaml). I was successful, and added an extra input parameter (FileSystemName) and Outputs for File System Mount Point and File System ID as FME Server / Kubernetes will need these when setting up the storage class and persistent volume.

## Next Steps

Tomorrow I'd like to continue with the 'Intro to AWS CloudFormation' online learning and learn more about the intrinsic functions. I'd like to see if I can expand my template further and include creating the EKS Cluster!

## Social Proof

[Proof](https://twitter.com/mapgirll/status/1351765882440060935?s=21)

