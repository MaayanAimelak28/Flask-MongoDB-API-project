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
`git clone https://github.com/yourusername/yourrepo.git`
`cd yourrepo`

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

![צילום מסך 2024-11-07 133000](https://github.com/user-attachments/assets/36d56dd7-2de3-4c30-82f9-c7517bd59444)

![צילום מסך 2024-11-07 133012](https://github.com/user-attachments/assets/561fb785-56b0-43f1-a186-4ef77af1e1a9)

![צילום מסך 2024-11-07 133025](https://github.com/user-attachments/assets/cb5436e4-843e-47e1-86ed-600c3110f8e6)

![צילום מסך 2024-11-07 133139](https://github.com/user-attachments/assets/582a2f37-e83d-441c-8781-e337476e6318)

![צילום מסך 2024-11-07 133157](https://github.com/user-attachments/assets/6465f572-90b6-45f4-9f25-d70d06ce5ede)

![צילום מסך 2024-11-07 133217](https://github.com/user-attachments/assets/dd4a2f57-a02c-413a-affb-b8c703752b0c)

![צילום מסך 2024-11-07 133229](https://github.com/user-attachments/assets/45f81a37-4943-44b3-b3a7-3f6e5ca72e03)

![צילום מסך 2024-11-07 133240](https://github.com/user-attachments/assets/65bfe79f-d9ee-4ab4-b242-c3f587d13a5c)



##### 7.Stopping the Containers
To stop the running containers, use the following command:
docker-compose down
This will stop and remove the containers, but leave the images intact.

##### Troubleshooting
* Ensure that the MongoDB image is pulled correctly by running docker ps to check if the MongoDB container is running.
* If the containers fail to start, use docker-compose logs to inspect the logs for any errors.
