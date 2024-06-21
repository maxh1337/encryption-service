from flask import request, jsonify
from models import users, methods, sessions, User, Session
from utils import vigenere_cipher, shift_cipher
import time

def configure_routes(app):

    @app.route('/users', methods=['POST'])
    def add_user():
        data = request.json
        if not data or 'login' not in data or 'secret' not in data:
            return jsonify({'message': 'Invalid input'}), 400
        if len(data['login']) < 3 or len(data['login']) > 10 or len(data['secret']) < 3 or len(data['secret']) > 10:
            return jsonify({'message': 'Invalid length for login or secret'}), 400
        user_id = len(users) + 1
        user = User(user_id, data['login'], data['secret'])
        users.append(user)
        return jsonify({'message': 'User added successfully'}), 201

    @app.route('/users', methods=['GET'])
    def get_users():
        return jsonify([{'user_id': user.user_id, 'login': user.login} for user in users]), 200

    @app.route('/methods', methods=['GET'])
    def get_methods():
        return jsonify(methods), 200

    @app.route('/encrypt', methods=['POST'])
    def encrypt():
        try:
            data = request.json
            if not data or 'user_id' not in data or 'method_id' not in data or 'data_in' not in data:
                return jsonify({'message': 'Invalid input'}), 400

            user_id = data['user_id']
            method_id = data['method_id']
            data_in = data['data_in']

            user = next((u for u in users if u.user_id == user_id), None)
            if not user:
                return jsonify({'message': 'User not found'}), 404

            method = next((m for m in methods if m['id'] == method_id), None)
            if not method:
                return jsonify({'message': 'Method not found'}), 404

            if len(data_in) > 10000:
                return jsonify({'message': 'Input data too long'}), 400

            if method['caption'] == 'Vigenere Cipher':
                if 'key' not in data['json_params']:
                    return jsonify({'message': 'Missing key for Vigenere Cipher'}), 400
                encrypted_data = vigenere_cipher(data_in, data['json_params']['key'])
            elif method['caption'] == 'Shift Cipher':
                encrypted_data = shift_cipher(data_in, method['json_params']['shift'])
            else:
                return jsonify({'message': 'Unsupported method'}), 400

            session = Session(
                id=len(sessions) + 1,
                user_id=user_id,
                method_id=method_id,
                data_in=data_in,
                data_out=encrypted_data,
                status='completed',
                created_at=time.time(),
                time_op=0  # Simplified for example purposes
            )
            sessions.append(session)

            return jsonify({'session_id': session.id, 'encrypted_data': encrypted_data}), 200

        except Exception as e:
            return jsonify({'message': 'An error occurred during encryption', 'error': str(e)}), 500

    @app.route('/sessions/<int:session_id>', methods=['GET'])
    def get_session(session_id):
        session = next((s for s in sessions if s.id == session_id), None)
        if not session:
            return jsonify({'message': 'Session not found'}), 404
        return jsonify({
            'id': session.id,
            'user_id': session.user_id,
            'method_id': session.method_id,
            'data_in': session.data_in,
            'data_out': session.data_out,
            'status': session.status,
            'created_at': session.created_at,
            'time_op': session.time_op
        }), 200

    @app.route('/sessions/<int:session_id>', methods=['DELETE'])
    def delete_session(session_id):
        try:
            data = request.json
            if not data or 'user_id' not in data or 'secret' not in data:
                return jsonify({'message': 'Invalid input'}), 400
            
            session = next((s for s in sessions if s.id == session_id), None)
            if not session:
                return jsonify({'message': 'Session not found'}), 404
            
            user = next((u for u in users if u.user_id == session.user_id and u.secret == data['secret']), None)
            if not user:
                return jsonify({'message': 'Unauthorized'}), 403
            
            sessions.remove(session)
            return jsonify({'message': 'Session deleted successfully'}), 200
        
        except Exception as e:
            return jsonify({'message': 'An error occurred while deleting session', 'error': str(e)}), 500
