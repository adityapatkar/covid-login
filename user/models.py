from flask import Flask, jsonify, request, redirect
import uuid
from passlib.hash import pbkdf2_sha256
import pymongo

class User:

    def signup(self):
        client = pymongo.MongoClient("mongodb+srv://flaskapp:myflaskapp@miniproject.dagcc.mongodb.net/flaskapp?retryWrites=true&w=majority")
        db = client.flaskapp


        #create the user object
        user = {
            "_id" : uuid.uuid4().hex,
            "name" : request.form.get("name"),
            "email" : request.form.get("email"),
            "password" : request.form.get("password")
        }

        #encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if db.users.find_one({"email" : user['email']}):
            return jsonify({"error" : "E-mail adress already in use. "}), 400

        #add to database
        if db.users.insert_one(user):
            return user, 200

        return jsonify({"error" : "signup failed"}), 400

    def login(self):
        client = pymongo.MongoClient("mongodb+srv://flaskapp:myflaskapp@miniproject.dagcc.mongodb.net/flaskapp?retryWrites=true&w=majority")
        db = client.flaskapp

        luser = {
            "email" : request.form.get("email"),
            "password" : request.form.get("password")
        }

        #create the user object
        user_e = db.users.find_one({
            "email" : luser['email']
        })

        if user_e and pbkdf2_sha256.verify(luser['password'], user_e['password']):
            return {"message": "Success"}, 201

        return jsonify({"error" : "login failed"}), 401
        