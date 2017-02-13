# Automating docker app deployments using ansible

Deploying microservice in containers and linking them together to communicate with each other.

In this demo, one front end webserver and one backend database is used.

The webserver displays the Welcome message and number of hits on the page.

Hits are stored in Redis database container.


Step 1: Deploy container microservice using Ansible Playbook by following command:

$ ansible-playbook -u root -k deploy_container.yml

Step 2: Check your docker host and verify if containers are launched:

$ docker ps

Your app should be launched at address http://$DOCKER_HOST_IP:5000
Check port the load balancer container at http://$DOCKER_HOST_IP:5001

Step 3: Update the app

Copy the new app/code to docker host and build the app again. 
This build takes less time since it used the previous image template

$ ansible-playbook -u root -k re_deploy_container.yml

Check http://$DOCKER_HOST_IP:5000 for new version of the app. 
Notice the hits. The app didn't go offline during the update.
