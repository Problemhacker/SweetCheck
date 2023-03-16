# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Define your food database here
# food_database = {
#     "apple": {"calories": 95, "sugar_per_serving": 19},
#     "banana": {"calories": 105, "sugar_per_serving": 14},
#     "grapes": {"calories": 67, "sugar_per_serving": 15},
#     "orange": {"calories": 62, "sugar_per_serving": 12},
#     "mango": {"calories": 99, "sugar_per_serving": 23},
#     "pineapple": {"calories": 50, "sugar_per_serving": 10},
#     "carrot": {"calories": 41, "sugar_per_serving": 5},
#     "broccoli": {"calories": 34, "sugar_per_serving": 2},
#     "cauliflower": {"calories": 25, "sugar_per_serving": 2},
#     "spinach": {"calories": 23, "sugar_per_serving": 1},
# }

# # Set the target sugar level here (in grams)
# target_sugar_level = 120

# @app.route('/')
# def index():
#     return render_template('index.html', food_database=food_database)

# @app.route('/', methods=['POST'])
# def calculate_sugar():
#     food_items = request.form.getlist('food_item')
#     quantities = request.form.getlist('quantity')
#     current_sugar_level = float(request.form['current_sugar_level'])

#     total_sugar = 0

#     for i in range(len(food_items)):
#         food_item = food_items[i].lower()
#         if food_item in food_database:
#             sugar_per_serving = food_database[food_item]['sugar_per_serving']
#             quantity = float(quantities[i])
#             total_sugar += (sugar_per_serving * quantity) / 100

#     # Calculate the current sugar level
#     current_sugar_level += total_sugar

#     if current_sugar_level >= 70 and current_sugar_level <= 125:
#        level_status = "Good"
#     else:
#        level_status = "Bad"

#     return render_template('index.html', current_sugar_level=current_sugar_level, level_status=level_status, food_database=food_database)


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

# Define your food database here
food_database = {
    "apple": {"calories": 95, "sugar_per_serving": 19},
    "banana": {"calories": 105, "sugar_per_serving": 14},
    "grapes": {"calories": 67, "sugar_per_serving": 15},
    "orange": {"calories": 62, "sugar_per_serving": 12},
    "mango": {"calories": 99, "sugar_per_serving": 23},
    "pineapple": {"calories": 50, "sugar_per_serving": 10},
    "carrot": {"calories": 41, "sugar_per_serving": 5},
    "broccoli": {"calories": 34, "sugar_per_serving": 2},
    "cauliflower": {"calories": 25, "sugar_per_serving": 2},
    "spinach": {"calories": 23, "sugar_per_serving": 1},
}

# Set the target sugar level here (in grams)
target_sugar_level = 120

# Define the reduction rate of sugar per minute of workout
sugar_reduction_rate = 0.25

@app.route('/')
def index():
    return render_template('index.html', food_database=food_database)

@app.route('/', methods=['POST'])
def calculate_sugar():
    current_sugar_level = float(request.form['current_sugar_level'])
    workout_time = float(request.form['workout_time'])
    total_sugar = 0

    # Loop through all form fields that start with 'food_item_'
    for field in request.form:
        if field.startswith('food_item_'):
            food_item = request.form[field].lower()
            if food_item in food_database:
                sugar_per_serving = food_database[food_item]['sugar_per_serving']
                quantity = float(request.form['quantity_' + field[10:]])
                total_sugar += (sugar_per_serving * quantity) / 100

    # Calculate the current sugar level
    current_sugar_level += total_sugar
    current_sugar_level -= (workout_time * sugar_reduction_rate)

    if current_sugar_level >= 70 and current_sugar_level <= 125:
        level_status = "Good"
    else:
        level_status = "Bad"

    return render_template('index.html', current_sugar_level=current_sugar_level, level_status=level_status, food_database=food_database)


if __name__ == '__main__':
    app.run(debug=True)
