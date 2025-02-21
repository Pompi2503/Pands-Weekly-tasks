# this program reads string and strips spaces, coverts letter to lower case 
# o/p len of original and normalised string
# Author Deepika Gusain
# Promot user for input and store in var rawString
rawString = input("Enter a String:")
# strip any trailing and lagging spaces and convert to lower case, and store in normalisedString
normalisedString = rawString.strip().lower()
# Captured len of original string
lenghtOfrawString = len(rawString)
# displays length of normalisedString String
lenghtOfnormalisedString = len(normalisedString)
# Print normalised string with corrected space and in lower case
print("The string normalised is: {}".format(normalisedString))
# print lenght of original string reduced to normalisedString
print("{} is reduced to {}".format(lenghtOfrawString,lenghtOfnormalisedString))
