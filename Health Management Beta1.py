################### MINI PROJECT SOURCE CODE BATCH-13###################
print('''   Welcome To Health Management System 
            Enter Your Data And Yo Are Good TO Go ''')

# Getting input from User.
name = input("Enter your Name:\n")

print("Hello",name)

height=int(input("Enter Your Height in cms:\n"))
weight=int(input("Enter your Weight in Kgs\n"))

#Calculate Body Mass Index(BMI)

bmi=int(weight/(height**2)*10000) # returns value as kg/m^2

print("Your BMI is: ",bmi)

if(bmi<16):
    print(name,"you are severely Underweight ")

elif(bmi>=16 and bmi<18.5):
    print(name,"you are underweight")
elif(bmi>=18.5 and bmi<25):
    print(name,"You are Healthy, just Keep eating a healthy diet to maintain your BMI")
elif(bmi>=25 and bmi<30):
    print(name,"you are overweight")
elif(bmi>=30):
    print(name,"you are obese")

num={"Severly Underweight":"1","Underweght":"2","Overweight":"3","Obese":"4"}
print(num)
print("Would You like to have a healthy diet paln for you")
yourkey=int(input("Then enter the number as per you state mentioned above: \n"))

if(yourkey==1):
    print(''' You Should Add Ghee, Peanut butter, Panner, Curd Along with your daily
    meals Like Chapati Curyy, Rice and Dal, Rava Idly Sambahr and Milk
    ''')
elif(yourkey==2):
    print(''' You Should Add Ghee, Peanut butter, Panner, Curd Along with your daily
    meals Like Chapati Curyy, Rice and Dal, Rava Idly Sambahr and Milk and Dry Fruits
    ''')
elif(yourkey==3):
    print('''You need to take low calorie foods, decrease carbohydrate and fatty foods,
    avoid junk foods and have salad, fruits and juice instead. Also daily cardio
    is recomended.
    ''')
elif(yourkey==4):
    print('''You Should totally cut sugar from your diet and should have low carb high
    protien diet.Avoid refined foods as much as possible.
    Must add salad and fruits along with some nut and you can also have 
    luke warm water with lemon in the morning. You must do cardio and jogging empty 
    stomach if possibe for best results. 
    ''')

print('''Some Meal Options That Any one can Opt:
    
     1. Breakfast: Rava Idly Sambhar/ Brown Bread Sandwich/ Eggs / Paneer/ Chapati With 
        Green Vegetables.
     2. Lunch : Rice+Dal/ Curd Rice/ Chicken/Paneer/ Chickpeas/ Rajma etc.
     3. Evening Snacks: Fruits/ Sandwich/ Yogurt / Roasted Peanuts etc.
     4. Dinner: Chapati Curry/ Warm Milk/ Oats/ lite food etc.
     ''')

exercise=int(input('''Would you like some exercise recomendations,
 If yes Enter 1 or esle: 0\n'''))

if(exercise==1):
    print('''
    1. Skipping Rope, Jogging and Other Cardio empty stomach for 30 minutes would
    be great to lose fat fast and will get you to Good Shape.
    2. Doing Yoga in the morning will not only get you fit but also refreshes and
    relaxes your mind for a good start of the day.
    3. Good sleep of 6-8 Hours is recommended
    ''' )
elif(exercise==0):
    print("#######_____Thank You, See You Again_______#######")
