# from flask import Flask, request, jsonify, render_template
# import json
# from flask_pymongo import PyMongo
# app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/rajasthan'
# mongo = PyMongo(app)
# # Load existing data from the file
# try:
#     with open('data.json', 'r') as file:
#         stored_data_dict = json.load(file)
# except FileNotFoundError:
#     # If the file doesn't exist yet, initialize an empty dictionary
#     stored_data_dict = {}

# @app.route('/', methods=['GET'])
# def index():
#     return render_template('admin/adminPage.html')# Assuming your HTML file is named user.html

# #Admin form for user
# @app.route('/admin/cameraOwner', methods=['GET','POST'])
# def admin_cameraOwner():
#     return render_template('admin/user.html') 

# #Admin Login page for police
# @app.route('/admin/police')
# def admin_police():
#     return render_template('admin/policeAdmin.html')


# #police 
# @app.route('/police/home')
# def police_home():
#     return render_template('/police/home.html') 
# @app.route('/police/notification.html')
# def police_noti():
#     return render_template('index.html') 


# @app.route('/your-server-endpoint', methods=['POST'])
# def receive_data():
#     try:
#         # Get JSON data from the request
#         data = request.get_json()
#         collection = mongo.db.user_data
#         inserted_data = collection.insert_one(data)
#         # Generate a unique key (you may use a more robust method in production)
#         key = len(stored_data_dict) + 1

#         # Store the data in the dictionary with the generated key
#         stored_data_dict[key] = data

#         # Save the updated data to the file
#         with open('data.json', 'w') as file:
#             json.dump(stored_data_dict, file)

#         # Print the received data to the console
#         print('Received data:', data)

#         # Send a response back to the client
#         response = {'message': 'Data received and stored successfully','key': str(inserted_data.inserted_id)}
#         return jsonify(response), 200

#     except Exception as e:
#         # Handle any exceptions that may occur
#         print('Error:', str(e))
#         response = {'error': 'Failed to process the data'}
#         return jsonify(response), 500

# @app.route('/get-stored-data')
# def get_stored_data():
#     # Return the stored data as JSON
#     return jsonify(stored_data_dict)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)  # Set the port to 5000 or another available port


from flask import Flask, request, jsonify, render_template
from ast import literal_eval
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


client=MongoClient('mongodb+srv://dhananjaydogne:DD@cluster0.q565lol.mongodb.net/?retryWrites=true&w=majority')
db=client.get_database('rjpolice')

@app.route('/', methods=['GET'])
def index():
    return render_template('admin/adminPage.html')# Assuming your HTML file is named user.html

#Admin form for user
@app.route('/admin/cameraOwner', methods=['GET','POST'])
def admin_cameraOwner():
    if request.method == 'POST':
        user_input = request.data
        user_input=literal_eval(user_input.decode('utf-8'))
        name = user_input['name']
        email = user_input['email']
        contact=user_input['Contact']
        address=user_input['Address']
        Location=user_input['Location']
        resolution=user_input['resolution']
        radius=user_input['radius']
        powerning=user_input['powerning']
        # Add other form fields as needed

        # Store data in MongoDB database
            
        db.camowner.insert_one({'name':name, 'email':email, 'contact':contact,'address':address, 'Location':Location,'resolution':resolution,'radius':radius,'powerning':powerning})
        
        
        return jsonify({'message': 'Data received successfully'}), 200
    

#Admin Login page for police
@app.route('/admin/police')

def admin_police():
    return render_template('admin/policeAdmin.html')


#police 
@app.route('/police/home')
def police_home():
    return render_template('/police/home.html') 

@app.route('/police/notification')
def police_notifications():
    return render_template('/index.html')

@app.route('/get_cameraOwner', methods=['GET'])
def get_cameraOwner():
    records=db.camowner
   
    data=jsonify(list(records. find({}, {'_id': 0})))
    print(data)
    return data
    # return jsonify({"data": "data"})

@app.route('/your-server-endpoint', methods=['POST'])
def receive_data():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Generate a unique key (you may use a more robust method in production)
        key = len(stored_data_dict) + 1

        # Store the data in the dictionary with the generated key
        stored_data_dict[key] = data

        # Save the updated data to the file
        with open('data.json', 'w') as file:
            json.dump(stored_data_dict, file)

        # Print the received data to the console
        print('Received data:', data)

        # Send a response back to the client
        response = {'message': 'Data received and stored successfully', 'key': key}
        return jsonify(response), 200

    except Exception as e:
        # Handle any exceptions that may occur
        print('Error:', str(e))
        response = {'error': 'Failed to process the data'}
        return jsonify(response), 500

@app.route('/get-stored-data')
def get_stored_data():
    # Return the stored data as JSON
    return jsonify(stored_data_dict)

if __name__ == '__main__':
    app.run(debug=True, port=80)  # Set the port to 5000 or another available port