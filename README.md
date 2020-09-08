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

## Enable root user ssh on CentOS and Ubuntu

### Install SSH Server on Ubuntu

From Ansible machine's terminal

    ssh ansible@192.168.112.131

Once you have logged in as 'ansible' user, you may then switch to root user as shown below

    su -

You may now paste the Ansible root user's public key into the /root/.ssh/authorized_keys

### How to enable root user ssh?

As root user, you may edit the file /etc/ssh/sshd_config

Look for PermitRootLogin prohibit-password, replace the prohibit-password with yes as shown below

    PermitRootLogin  yes
    
You may now edit /etc/ssh/sshd file and look for pattern "session required pam_loginuid.so" and replace with "session optional pam_loginuid.so"
