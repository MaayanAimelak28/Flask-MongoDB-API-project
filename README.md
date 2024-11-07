# MongoDB Flask API
This project provides a simple Flask-based REST API that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB collection. The API allows users to interact with a database and manage documents in a collection.

The application is containerized using Docker and orchestrated with Docker Compose for easy setup and deployment.

## Prerequisites
Before running the application, ensure that the following tools are installed on your system:

##### Docker: To build and run containers.
##### Docker Compose: To manage multi-container Docker applications.

## Getting Started
Follow these steps to get the application running:

##### 1. Clone the Repository
Clone the repository to your local machine:
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

##### 2. Verify Docker Installation
Ensure that Docker is installed and running on your machine:
docker -v
You should see the version of Docker installed, e.g., Docker version 20.x.x.

##### 3. Pull MongoDB Image
Pull the MongoDB Docker image to set up the database container:
docker pull mongo
This command will download the latest MongoDB image from Docker Hub.

##### 4. Build the Docker Image for the Flask API
You need to build the Docker image for the Flask API. This will package the application into a container image.
docker-compose build
This command will build the images for the Flask API service defined in the docker-compose.yml file.

##### 5. Start the Containers
use Docker Compose to start both the MongoDB container and the Flask API container:
docker-compose up
This will run the application in the foreground. The API will be available on http://localhost:5001.

##### 6. Access the API
Once the containers are up and running, you can interact with the API through HTTP requests. The following endpoints are available:
* GET /mongodb: Retrieve all documents from the specified MongoDB collection.
* POST /mongodb: Insert a new document into the collection.
* PUT /mongodb: Update an existing document in the collection.
* DELETE /mongodb: Delete a document from the collection.
* 
You can test the API using tools like Postman.






![צילום מסך 2024-11-07 133240](https://github.com/user-attachments/assets/9c8ed6e6-e3c4-4af2-8926-ad47942800a6)
![צילום מסך 2024-11-07 133229](https://github.com/user-attachments/assets/9903ac0d-73b3-4b4b-8398-ba59115acbdb)
![צילום מסך 2024-11-07 133217](https://github.com/user-attachments/assets/3eb941c5-42ea-4190-970f-9e44158b9ec4)
![צילום מסך 2024-11-07 133157](https://github.com/user-attachments/assets/2d8c16f7-aad8-4c90-98d7-6ba70850c759)
![צילום מסך 2024-11-07 133139](https://github.com/user-attachments/assets/787a19ab-5afb-455a-951d-169a6c653439)
![צילום מסך 2024-11-07 133025](https://github.com/user-attachments/assets/510d158d-ec2d-40cd-9a92-98990759cb08)
![צילום מסך 2024-11-07 133012](https://github.com/user-attachments/assets/91b08e23-f0fc-4c33-8213-cab54aebf309)
![צילום מסך 2024-11-07 133000](https://github.com/user-attachments/assets/94d30d08-69b7-4289-a701-08f0144ba540)



##### 7.Stopping the Containers
To stop the running containers, use the following command:
docker-compose down
This will stop and remove the containers, but leave the images intact.

##### Troubleshooting
* Ensure that the MongoDB image is pulled correctly by running docker ps to check if the MongoDB container is running.
* If the containers fail to start, use docker-compose logs to inspect the logs for any errors.
