# Kaitlyn Harold and Annie Dumont
# Course: CS151, Dr. Simari
# Date: 1/28/2021
# Lab Number: 1
# Program Inputs: number of mL
# Program Outputs: number of teaspoons and tablespoons

#ask user to input the number of ml
milliliters = input("Please enter the number of milliliters:")
milliliters = float(milliliters)
print(milliliters)
teaspoons = milliliters / 5
print("The number of teaspoons is", teaspoons)
tablespoons = teaspoons / 3
print("The number of tablespoons is", tablespoons)

