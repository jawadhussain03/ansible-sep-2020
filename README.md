# Install Ansible

## Switch as root user

su -
  
## Install Extra Packages for Enterprise Linux

yum install -y epel-release

## Install ansible

yum install -y ansible

## Install tree and git 

yum install -y tree git

## To see the list of Ansible modules supported by your version of Ansible

ansible-doc -l

## To see the number of Ansible modules supports, you may try below

ansible-doc -l | wc -l
