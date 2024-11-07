from flask import Flask, request, json, Response
from pymongo import MongoClient
import logging as log

# Initialize the Flask application
app = Flask(__name__)

# MongoDB API Class
class MongoAPI:
    def __init__(self, data):
        """
               Initializes the MongoAPI instance with a MongoDB client, database, and collection.
               Parameters:
                   data (dict): A dictionary containing connection details, including the database and collection names.
               """
        # initialize the MongoDB client, connecting to the server
        self.client = MongoClient("mongodb://mymongo_1:27017/")

        # uncomment the line below if you want run locally
        #self.client = MongoClient("mongodb://localhost:27017/")

        # retrieve the database and collection names from the input data
        database = data['database']
        collection = data['collection']
        cursor = self.client[database] # connect to the specified database
        self.collection = cursor[collection] # access the specified collection
        self.data = data # store input data for later use

    def read(self):
        """
        Retrieves all documents from the specified MongoDB collection.
        Returns:
            list: A list of dictionaries, each representing a document from the collection with the '_id' field excluded.
        """
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output


    def write(self, data):
        """
        Inserts a new document into the MongoDB collection.
        Parameters:
            data (dict): A dictionary containing the document data to be inserted.
        Returns:
            dict: A dictionary with the status of the insertion and the ID of the newly inserted document.
        """
        log.info('Writing Data')
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self):
        """
        Updates an existing document in the MongoDB collection based on a filter.
        Returns:
            dict: A dictionary with the status of the update, indicating whether the update was successful or if no documents were modified.
        """
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        """
        Deletes a document from the MongoDB collection based on a filter.
        Parameters:
            data (dict): A dictionary containing the filter criteria for deletion.
        Returns:
            dict: A dictionary with the status of the deletion, indicating whether the document was deleted or not found.
        """
        filt = data['Filter']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

# Define the base route for health check
@app.route('/')
def base():
    """
    Health check route to ensure the server is running.
    Returns:
        Response: A JSON response with a "Status: UP" message.
    """
    return Response(response=json.dumps({"Status": "UP"}), status=200, mimetype='application/json')

# Route to handle GET requests for reading from MongoDB
@app.route('/mongodb', methods=['GET'])
def mongo_read():
    """
    Handles GET requests to read documents from the MongoDB collection.
    Returns:
        Response: A JSON response with the documents or an error if connection information is missing.
    """
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),status=400, mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.read()
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

# Route to handle POST requests for inserting a document
@app.route('/mongodb', methods=['POST'])
def mongo_write():
    """
    Handles POST requests to insert a document into the MongoDB collection.
    Returns:
        Response: A JSON response indicating the status of the insertion or an error if required data is missing.
    """
    data = request.json
    if data is None or data == {} or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}), status=400, mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.write(data)
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

# Route to handle PUT requests for updating a document
@app.route('/mongodb', methods=['PUT'])
def mongo_update():
    """
    Handles PUT requests to update a document in the MongoDB collection.
    Returns:
        Response: A JSON response indicating the status of the update or an error if required data is missing.
    """
    data = request.json
    if data is None or data == {} or 'DataToBeUpdated' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}), status=400, mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.update()
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

# Route to handle DELETE requests for deleting a document
@app.route('/mongodb', methods=['DELETE'])
def mongo_delete():
    """
    Handles DELETE requests to delete a document from the MongoDB collection.
    Returns:
        Response: A JSON response indicating the status of the deletion or an error if required data is missing.
    """
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}), status=400, mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.delete(data)
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
