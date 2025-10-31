from flask import Flask, render_template, request
from recommendation import recommend_cars

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    budget_min = request.form.get('budget_min')
    budget_max = request.form.get('budget_max')
    body = request.form.get('body')
    fuel = request.form.get('fuel')
    transmission = request.form.get('transmission')
    seats = request.form.get('seats')

    results = recommend_cars(
        budget_min=float(budget_min) if budget_min else None,
        budget_max=float(budget_max) if budget_max else None,
        body=body,
        fuel=fuel,
        transmission=transmission,
        seats=int(seats) if seats else None
    )

    cars = results.to_dict(orient='records')
    return render_template('results.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)
