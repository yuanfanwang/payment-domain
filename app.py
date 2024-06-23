from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
# CORS(app)

"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
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
    return jsonify({'message': 'Payment created', 'payment': {
        'id': payment.id,
        'user_id': payment.user_id,
        'amount': payment.amount,
        'product_id': payment.product_id,
        'timestamp': payment.timestamp.isoformat()
    }}), 201
"""

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5003)
