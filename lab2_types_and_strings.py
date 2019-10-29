#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        # print only first and last of the sentence
        print("\nFirst Letter:" + message[0])
        print("Last Letter: " + message[-1])


        # use slice notation
        print("\nusing slice notation")
        print("First 3 letters: " + message[0:3])
        print("Last 3 letters: " + message[-3:])
        print("Up to 4th index: " + message[:4])
        print("Second index onwards: " + message[2:])
        print("Displaying whole noun: " + message[:])

        # escaping a character
        print("\nHe said \"that\'s fantastic\"!")


        # find all a's in the input word and count how many there are
        print("First position of a:")
        print(message.find(str('a')))
        print("Occurrences of a:")
        print(message.count(str('a')))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        print(message.replace('a', '-'))


        # printing only characters at even index positions
        for i in range(0, len(message), 2):
            print(message[i])


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        original_sentence = []
        original_sentence = message.split()
        print(original_sentence)

        # append a new element to the list and print
        user_input = input("Add word to the sentence: ")
        original_sentence.append(user_input)
        print(original_sentence)


        # remove from the list in 3 ways


        # check if the word cake is in your input list


        # reverse the items in the list and print


        # reverse the list with the slicing trick


        # print the list 3 times by using multiplication



tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()