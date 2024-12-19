# BMI Calculator

def calculate_bmi(weight, height):
    """Calculate BMI using the formula: BMI = weight (kg) / height (m)^2"""
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."


def interpret_bmi(bmi):
    """Interpret the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        bmi = calculate_bmi(weight, height)

        if isinstance(bmi, str):
            print(bmi)
        else:
            print(f"Your BMI is: {bmi}")
            print(f"Category: {interpret_bmi(bmi)}")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")


if __name__ == "__main__":
    main()

