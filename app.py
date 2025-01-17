from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import requests

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    payment = Payment(user_id=data['user_id'], amount=data['amount'], product_id=data['product_id'])
    db.session.add(payment)
    db.session.commit()

    # Call the update_model API
    try:
        response = requests.post('http://api-layer-ai:5004/api/update_model', json={
            'user_id': payment.user_id,
            'product_id': payment.product_id,
            'amount': payment.amount
        })
        response_data = response.json()
        update_status = response_data.get('message', 'Update failed')
    except requests.exceptions.RequestException as e:
        update_status = f'Update failed: {str(e)}'

    return jsonify({'message': 'Payment created', 'payment': {
        'id': payment.id,
        'user_id': payment.user_id,
        'amount': payment.amount,
        'product_id': payment.product_id,
        'timestamp': payment.timestamp.isoformat()
    }}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5003)
