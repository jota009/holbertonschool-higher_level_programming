#!/usr/bin/python3
"""
Module: task_04_flask

A simple RESTfule API using Flask.
Serves a welcome message, user info, and supports adding users.
"""
from flask import Flask, jsonify, request
app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return (
        jsonify({"message": "User added", "user": data}), 201
        )


if __name__ == "__main__":
    app.run()
