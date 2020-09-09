# Copy default nginx conf file from ubuntu to Ansible Controller Machine

    scp root@192.168.112.131:/etc/nginx/sites-available/default .
    
# To execute the playbook

    ansible-playbook -i hosts install-nginx-playbook.yml
