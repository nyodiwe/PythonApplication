
print("Welcome to the Body Mass Index (BMI) Calculator")
#######################################
#####################################
####################################
w = float(input("Enter your Weight in KG : "))
h = float (input("Enter your Height in Metre : "))
h2 = h**2
bmi = w/h2
bmi_approx = int(bmi)
print("Your BMI is : " , bmi_approx)
