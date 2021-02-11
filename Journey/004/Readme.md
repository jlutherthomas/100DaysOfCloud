# Learning Azure Resource Manager Templates


## Introduction

As a distributed deployment of FME Server is available on the [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/safesoftwareinc.fme-server-distributed-deployment?tab=Overview) I wanted to learn how to create and modify ARM templates so that I can adapt them to my needs. I can then reap the benefits of IaC (Infrastructure as Code) the next time I need to test this deployment.

## Use Case

For this scenario I wanted to test using a private load balancer. The marketplace deployment by default comes with a public load balancer, and I wasn't having any luck changing it through Azure Portal so I thought modifying the ARM template would be easiest.

## Cloud Research

My learning was done using the [A Cloud Guru - Introduction to Microsoft Azure Resource Manager](https://acloudguru.com/course/introduction-to-azure-resource-manager).

Then, I downloaded the template that you get on the last page when you launch FME Server from the Marketplace and started working!

## Things I did

### Changed the frontendIPConfigurations

The original template is referring to the public IP address (which I actually didn't remove from my template) so I had to change that configuration to use a static, private IP address.

### Change the loadBalancerBackendAddressPools 

In the original template it has 2 Backend Address Pools because one is public and one is private which is allowed by Azure. When I tried it complained that you can't have 2 private so I removed the engine load balancer and kept the core load balancer.  


## ☁️ Cloud Outcome

It worked, although for several days I thought that it hadn't worked. With Azure, internal/private load balancers don't work if the host ends up trying to connect to itself. So I would RDP into the VM, try to access the FME Server web ui and it wouldn't work. Then I gave up for a few days (after trying multiple things). I decided to try the [Azure Quickstart](https://docs.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-internal-portal?tabs=option-1-create-internal-load-balancer-standard) to do this without FME and then realized my missing element - a test VM in order to access the web through the load balancer. What's really embarrassing about this whole thing is that I knew about this load balancer behaviour, and it was exactly what I was trying to reproduce, and then test other solutions.

I did learn a few things from this exercise though, one of them being how to set up and use a Bastion Host in Azure so that I can RDP into my private VMs.

## Next Steps

There are a lot of next steps for this project, and two directions to take it in.
- Tidy up the template I modified to remove everything I don't need (like the public IP) and add in the things I do need (bastion host, new subnet, test VM)
- Abandon using a load balancer altogether and modify the template to use Application Gateway instead. This will mean I don't need a test VM, but I would still need the bastion host.
- Once I've swapped out to use Application Gateway, I could either make two templates, or a fancy one template, that gives the option of a private FME Server distributed deployment, or a public one.
- I'm also not sure that the private IP of the load balancer (or App Gateway if I use that) is getting passed to FME Server to be used in the service urls. This is something I'd have to test and work on.

## Social Proof

✍️ Show that you shared your process on Twitter or LinkedIn

[link](link)
