"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from flask import Flask, jsonify, request
from datastructures import Family



app = Flask(__name__)
jackson_family = Family('Jackson')

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({'error': 'Member not found'}), 404

@app.route('/member', methods=['POST'])
def add_member():
    data = request.json
    if data:
        jackson_family.add_member(data)
        return jsonify({'status': 'Member added'}), 200
    return jsonify({'error': 'Invalid data provided'}), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify({'done': True}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
