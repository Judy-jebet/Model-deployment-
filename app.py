from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    product = request.form['product']
    branch = request.form['branch']
    city = request.form['city']
    payment = request.form['payment']

    # Here you can implement your prediction logic based on selected values
    # For demonstration purposes, let's assume we predict based on product line and city only
    gender_preference = predict_gender_preference(product, branch, city, payment)
    prediction_result = 'Male preferences predicted.' if gender_preference == 'male' else 'Female preferences predicted.'

    return jsonify({'prediction': prediction_result})

# Dummy prediction function, replace with actual prediction logic
def predict_gender_preference(product, branch, city, payment):
    # Dummy logic based on product line and city
    if product == 'Electronic Accessories' and city == 'Yangon':
        return 'male'
    elif product == 'Fashion Accessories' and city == 'Naypyitaw':
        return 'female'
    else:
        # Default prediction
        return 'female'

if __name__ == '__main__':
    app.run(debug=True)
