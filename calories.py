def main():

    # Ask for the number of fat grams.(user input)
    fat = int(input('Enter the number of fat grams consumed in a day: '))
    fat_calories(fat)

    # Ask for the number of carb grams.(user input)
    calories = int(input('Enter the number of carbohydrate grams consumed in a day: '))
    carb_calories(calories)

def fat_calories(fat):
    
    #  Calculate calories_from_fat = fat *9
    calories_from_fat = fat * 9
    print ('The calories from fat are', calories_from_fat)

def carb_calories(carbs):
     
    #  Calculate calories_from_carbs = carbs * 4
    calories_from_carbs = carbs * 4
    print ('The calories from carbohydrates are', calories_from_carbs)

#  main function is called