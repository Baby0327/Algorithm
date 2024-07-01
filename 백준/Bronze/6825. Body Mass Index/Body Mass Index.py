w = float(input())
h = float(input())
result = w / (h**2)
if result > 25:
    print("Overweight")
elif result >= 18.5:
    print("Normal weight")
else:
    print("Underweight")