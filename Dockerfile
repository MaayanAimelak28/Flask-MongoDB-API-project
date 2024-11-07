# Step 1: Select the base image
FROM python

# Step 2: Set up the working directory for the app
WORKDIR /app

# Step 3: Copy the dependencies file to the container
COPY /requirements.txt /app

# Step 4: Install Python dependencies
RUN pip3 install -r requirements.txt

# Step 5: Copy the main application file to the working directory in the container
COPY ["api_mongo_flask.py", "/app"]

# Step 6: Expose the port that the Flask app will use
EXPOSE 5001

# Step 7: Set the default entrypoint to run Python
ENTRYPOINT [ "python3" ]

# Step 8: Specify the default command to run the application
# CMD will be replaced if another command is provided during runtime
CMD ["api_mongo_flask.py"]