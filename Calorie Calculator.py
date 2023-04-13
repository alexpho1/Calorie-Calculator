gender = input("Are you male or female?(M/F) ")
weight = eval(input("What is your weight or goal weight in pounds? "))
activityLevel = input("Describe your activity level? (Low, Light, Moderate, Extreme) ")
activityLevel = activityLevel.strip()
multiplier = 0
if gender == 'M':
    if activityLevel == 'Low':
        multiplier = 14
    elif activityLevel == 'Light':
        multiplier = 15
    elif activityLevel == 'Moderate':
        multiplier = 16
    elif activityLevel == 'Extreme':
        multiplier = 17
    else:
        print('Invalid Response')
elif gender == 'F':
    if activityLevel == 'Low':
        multiplier = 13
    elif activityLevel == 'Light':
        multiplier = 14
    elif activityLevel == 'Moderate':
        multiplier = 15
    elif activityLevel == 'Extreme':
        multiplier = 16
    else:
        print('Invalid Response')

calories = weight * multiplier
print('Based on your responses your caloric intake should be around', calories, 'calories.')