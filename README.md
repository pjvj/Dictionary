# Dictionary
The goal of the program is allow a user to enter a word as input, and using a stored dictionary , return the meaning of the word.

## Requirements
A python installed system
The libraries used are:
* json   ...for converting text file to json and storing in a dictionary
* nltk   ...for some lowercase conversions
* tkinter...for simple working GUI in python

## Function findword()
It is calculating the nears and probable suggestions based on edit distance=1 by performing 4 major transformations like transposing, substituting, removing, adding characters.
It also maintains the frequency of the words that are feeded(selected from the suggested list) by the user.
This frequency will be used to determine the future suggestions so that the higher frequency words will be suggested. Hence, frequency is used for self learning and analysis by the algorithm

## Function delsearch()
It will be used to delete the existed suggestions and display the result of the selected word from the suggestions.

## Function search()
It determines if the word exits in the dictionary. If it does, it display the results. Else, It calls findword() function to generate suggestions based upon the frequency and extant words of dictionary.
The words returned from the findword function are dislayed as buttons which can be clicked to obtain results further by calling the delsearch() function.

