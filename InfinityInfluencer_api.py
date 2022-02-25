from flask import Flask, request
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest
import sqlite3
from model import Model

#Initialize Flask
app = Flask(__name__)
api = Api(app)

#Initialize database and connect 
conn = sqlite3.connect(':memory:', check_same_thread=False)
curr = conn.cursor()

#Create model object and set table names and columns
session_model = Model(conn, curr)
table_name = 'vocab_words'
columns = [('word', 'VARCHAR (255)', 'PRIMARY KEY')]

#Create table and insert initial values
session_model.create_table(table_name, columns)
session_model.insert(['#ad','#sponsored', 'advertisement'], table_name)


class Vocab(Resource):
    #Sends a GET and returns all vocab words currently in database
    def get(self):
        try:
            vocab_words = session_model.select(columns[0][0], table_name)
            return {'vocab':vocab_words}, 200

        except:
            raise BadRequest('An error occurred while getting vocab words')
    
    #Sends a POST to add a new vocab word to the database and returns all words. Duplicate words cannot be added
    def post(self):
        try:
            request_data = request.get_json(force=True)
            words = request_data['vocab']

            duplicates = session_model.insert(words, table_name)
            current_words = session_model.select(columns[0][0], table_name)

            if duplicates:
                return {'vocab':current_words, 'message':'A duplicate word has not been added'}, 200
            return {'vocab':current_words}, 200

        except:
            raise BadRequest('An error occured while adding new words')


class Prediction(Resource):
    #Sends a POST to see if post_text is sponsored or non-sponsored. Checks the vocab words in the database and returns a prediction
    def post(self):
        try:
            request_data = request.get_json(force=True)

            data = request_data['post_text'].split()
            current_words = session_model.select(columns[0][0], table_name)

            for word in data:
                if word in current_words:
                    return {'prediction':'sponsored'}, 200
            return {'prediction':'non-sponsored'}, 200

        except:
            raise BadRequest('An error occured while trying to make a prediction')


#Define routes
api.add_resource(Vocab, '/api/vocab')
api.add_resource(Prediction, '/api/prediction')


if __name__ == '__main__':
    app.run(debug=False, port=5000) 