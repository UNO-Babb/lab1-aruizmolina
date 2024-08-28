#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Give me a noun ")
  noun2 = input("Give me another noun ")
  adj1 = input("Give me and adjective ")
  verb1 = input("Give me a verb in the past tense ")
  verb2 = input("Give me another verb in the past tense ")
  adverb1 = input("Give me an adverb ")
  #Print the story with the user supplied words.
  print("Once there was a great", noun1, "the great", noun1, "had a very big problem, his", noun2, "was very unhelpful")
  print("The", noun1, verb1, "to the store to see if he could find a brand new", noun2)
  print("The", noun1, "arrived to the store and found a", adj1, noun2, "surely this new", noun2, "is an improvement")
  print("The", noun1, adverb1, verb2, "back to his home and lived happily ever after")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
