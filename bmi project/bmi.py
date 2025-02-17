"""
This program calculates the Body Mass Index (BMI) of a person based on their weight and height.
The BMI is a measure of body fat based on a person's weight in relation to their height.
The formula to calculate BMI is weight (kg) / height (m) ** 2.
The program will prompt the user to enter their name, age, weight and height.
It will then calculate and display the BMI of the user and give exercise and diet recommendations based on BMI results.
"""

def get_user_details():
    """Get user details including name, weight, and height."""
    print("Hello there!")
    print("Welcome to the BMI calculator.")
    print("Please enter your details to calculate your BMI.")
    name = input("Enter your name: ")
    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0:
                break  # Exit the loop if age is valid
            else:
                print("Invalid input. Age cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")

    while True:
        sex = input("What is your gender? [male/female]: ").lower()
        if sex in ["male", "female"]:
            break  # Exit the loop if sex is valid
        else:
            print("Invalid input. Please enter either 'male' or 'female'.")

    print(f"Hello, {name}!")
    while True:
        units = input("Would you like to enter your details in metric or imperial units? ").lower()

        try:
            if units == "metric":
                height = float(input("Enter your height in meters: "))
                weight = float(input("Enter your weight in kilograms: "))
                break
            elif units == "imperial":
                height_inches = float(input("Enter your height in inches: "))
                weight_pounds = float(input("Enter your weight in pounds: "))
                # Convert imperial to metric
                height = height_inches * 0.0254
                weight = weight_pounds * 0.453592
                break
            else:
                print("Invalid input. Please enter either 'metric' or 'imperial'.")
        except ValueError:
            print("Please enter valid numbers for height and weight.")

    return name, weight, height, age, sex

# Sample BMI percentiles for children (simplified)
BMI_PERCENTILES = {
    "underweight": (0, 5),
    "healthy": (5, 85),
    "overweight": (85, 95),
    "obese": (95, 100),
}

def get_bmi_percentile(bmi, age):
    if age < 5:
        return "BMI calculation not available for children under 5", None
    if age < 18:
        for category, (start, end) in BMI_PERCENTILES.items():
            if start <= bmi <= end:  # Corrected the condition here
                # Calculate a simple percentile based on the range
                percentile = (bmi - start) / (end - start) * 100
                return category, percentile
        return None, None # if BMI does not fall into any category
    return None, None


def calculate_bmi(weight, height): 
    bmi = weight / (height ** 2)
    print("Calculating BMI...")
    print("Your BMI is: {0:.2f}".format(bmi))
    return bmi


def print_results(bmi, name, age, sex): # added name
    if age < 5:
        print("BMI calculation not available for children under 5")
        return
    if age < 18:
        category, percentile = get_bmi_percentile(bmi, age)
        if category == "BMI calculation not available for children under 5":
            print("BMI calculation not available for children under 5")
        elif category is not None and percentile is not None:
            if percentile is not None:
                print("Your BMI percentile is: {0:.1f}%".format(percentile))
            print("Your BMI category is: {0}".format(category))
        return

    else:
        if sex == "female":
            if bmi < 18.5:
                print("You are underweight. 😓 Women generally need more body fat for health.")
            elif 18.5 <= bmi < 25:
                print("{0}, you have normal weight.👌😁".format(name))
            elif 25 <= bmi < 30:
                print("You are overweight. Consider a balanced diet and exercise. 😫")
            else:
                print("{0}, you are highly overweight. Consult a doctor for guidance.🤦‍♀️".format(name))
        else:
            if bmi < 18.5:
                print("You are underweight. 😓 Consider increasing protein intake.")
            elif 18.5 <= bmi < 25:
                print("{0}, you have normal weight.👌😁".format(name))
            elif 25 <= bmi < 30:
                print("You are overweight. Consider strength training and diet 😫")
            else:
                print("{0}, you are highly overweight. Consult a doctor for guidance.🤦‍♂️".format(name))

def give_health_tips(bmi, age):
    if age < 5:
        return "BMI and health tips are not available for children under 5."

    if age < 18:
        return "For children, maintaining a balanced diet and regular physical activity is essential. Talk to a pediatrician for proper guidance."

    if bmi < 18.5:
        return "🔹 Eat more calorie-dense foods like nuts, avocados, and whole grains.\n🔹 Strength training can help build muscle mass."
    elif 18.5 <= bmi < 25:
        return "🔹 Maintain a balanced diet and regular exercise.\n🔹 Keep up with hydration and sleep well!"
    elif 25 <= bmi < 30:
        return "🔹 Reduce sugar intake and focus on lean proteins.\n🔹 Try daily cardio like jogging or cycling."
    else:
        return "🔹 Consult a nutritionist for a healthy diet plan.\n🔹 Start with low-impact exercises like swimming or walking."


def main():
    name, weight, height, age, sex = get_user_details()
    bmi = calculate_bmi(weight, height) 
    print_results(bmi, name, age, sex) # added name

    print(give_health_tips(bmi, age))

if __name__ == "__main__":
    main()
