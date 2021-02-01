# Kaitlyn Harold and Annie Dumont
# Course: CS151, Dr. Simari
# Date: 1/28/2021
# Lab Number: 1
# Program Inputs: user inputs manually number of mL
# Program Outputs: program computes number of teaspoons and tablespoons

# Output purpose:
print('This program is to convert the number of teaspoons and tablespoons given the number of ml (milliliters)')

# ask user to input the number of ml (milliliters)
milliliters = input("Please enter the number of milliliters:")
milliliters = float(milliliters)
print(milliliters)

# compute number of teaspoons
teaspoons = milliliters / 5

# output the number of teaspoons
print("The number of teaspoons is", teaspoons)

# compute the number of tablespoons
tablespoons = teaspoons / 3

# output the number of tablespoons
print("The number of tablespoons is", tablespoons)

