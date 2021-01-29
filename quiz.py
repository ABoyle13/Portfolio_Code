# allows the 'datetime' library to be used in this script
import datetime
# allows the 'numpy' library to be used in this script and referred to as 'np'
import numpy as np
# allows the 'tabulate' module of the 'tabulate' library to be used in this script
from tabulate import tabulate

# defines a class called 'Quiz'
class Quiz:

    # this is the constructor, it defines variables that can be used in all
    # functions of the class
    def __init__(self, name):
        # assigned the value of the variable 'name' that has been passed into
        # the class to the variable 'self.name'
        self.name = name
        # creates a variable that will keep track of the player's score and has
        # been assigned the starting value of 0
        self.score = 0
        # creates an array that will be used to store the text that will be
        # pulled out of the 'quiz' text file
        self.text = []
        # creates an array that will store the questions of the quiz
        self.questions = []
        # creates an array that will store the possible answers of the quiz
        self.answers = []
        # creates an array that will store the position of the correct answer
        # to each question in the quiz
        self.results = []
        # creates an array that will store the user's answers to the quiz
        self.user_results = []
        # creates an array that will store the results of if the user's
        # answer's are correct
        self.marks = []
        # creates an array that will store the text that will be pulled out
        # of the 'user_results' text file
        self.lead = []


    # defines a function called 'open_file'
    def open_file(self, quiz):

        ''' opens requested file '''
        
        # starts a try-except statement that will check to see if the file
        # you want to open, exists or not
        try:
            # checks to see if the data stored in variable 'quiz' equals 1
            if quiz == 1:
                # opens file 'quiz.txt' in read-plus mode and assigns the data
                # contained within the file to the variable 'file'
                file = open("quiz.txt", "r+")
            # checks to see if the data stored in variable 'quiz' equals 2
            elif quiz == 2:
                # opens file 'quiz2.txt' in read-plus mode and assigns the data
                # contained within the file to the variable 'file'
                file = open("quiz2.txt", "r+")
            # uses the built-in function 'readlines' to read the file line by
            # line and assign that data to the variable 'text'
            text = file.readlines()

            ''' puts file data into a 2D list '''

            # the for loop iterates through the data stored in 'text' line by line
            for line in text:
                # adds the line just read to the list 'self.text'
                self.text.append(line)

            ''' splits questions, answers and results into separate lists '''

            # this for loop iterates through the loop for a set amount of times,
            # this being the length of the list 'self.text'
            for i in range(len(self.text)):
                # assigns the data in the index position 'i' to the variable 'phrase'
                phrase = self.text[i]
                # splits the data in phrase up into chunks, separated by commas, and
                # assigned to the variable 'new'
                new = phrase.split(',')
                # assigns the first item in the list 'new' to the variable 'q'
                q = new[0]
                # assigns the 2nd to 5th items in the list 'new' to the variable 'a'
                a = new[1:5]
                # assigns the 6th item in the list 'new' to the variable 'r'
                r = new[5]
                # adds the value assigned to the variable 'q' to the
                # 'self.questions' list
                self.questions.append(q)
                # adds the values assigned to the variable 'a' to the
                # 'self.answers' list
                self.answers.append(a)
                # adds the first character of the value assigned to the variable
                # 'r' to the 'self.results' list
                self.results.append(r[:1])

        # this catches the error of the file trying to be opened not existing
        except FileNotFoundError:
            # tells the user that the file does not exist
            print("File does not exist")
            
    # defines a function called 'run_quiz'
    def run_quiz(self):

        ''' print questions '''
        
        # checks to see if the 'self.questions' list is empty, meaning that
        # a file has not been found
        if len(self.questions) == 0:
            # takes the program out of the subroutine and back to the return address
            pass
        # if the 'self.questions' list is not empty, the following code is executed
        else:
            # creates a counter variable and sets the value to 0
            count = 0
            # this for loop iterates through each item in the 'self.questions' list
            for question in self.questions:
                # displays the item from the 'self.questions' list to the user
                print("Question", count+1, ") ", question)
                print()

                ''' print answers '''

                # this for loop iterates for the number of times that is equal
                # to the length of the item in 'self.answers'
                for i in range(len(self.answers[count])):
                    # displays the answers for that question to the user
                    print(i+1, ") ", self.answers[count][i])
                print()

                # takes a user input of their answer to the question
                answer = input("Enter your answer: ")

                # adds the user's answer to the 'self.user_results' list
                self.user_results.append(answer)
                # increments the counter variable by 1
                count += 1
                print("\n")


    # defines a function called 'check1' that checks the user's results to quiz 1
    def check1(self):

        # checks to see if the 'self.user_results' list is empty, meaning that
        # a file has not been found
        if len(self.user_results) == 0:
            # takes the user out of this subroutine and the program will continue
            pass
        # if the 'self.user_results' list is not empty, the following code will
        # be executed
        else:
            ''' making leading and trailing spaces disappear '''

            # creates a variable called 'loop' and assigns the value 0 to it
            loop = 0
            # this while loop will continue as long as the loop variable
            # does not hold the value 2
            while loop != 2:
                # creates a counter variable and sets it to 0
                count = 0
                # this for loop iterates through each item in the
                # 'self.user_results' list
                for i in self.user_results:
                    # checks to see if the first character of the string is blank
                    if i[:1] == " ":
                        # reassigns the variable with the blank space removed
                        i = i[1:]
                    # checks to see if the last character of the string is blank
                    elif i[-1:] == " ":
                        # reassigns the variable with the blank space removed
                        i = i [:-1]

                    ''' making answers start with capital letter '''

                    # reassigns the variable with the first character being
                    # changed to a capital letter
                    i = i[:1].upper() + i[1:]
                    # reassigns the specified item in the 'self.user_results'
                    # list with the modified variable
                    self.user_results[count] = i
                    # increments the counter variable by 1
                    count += 1
                # increments the 'loop' variable by 1
                loop += 1

            ''' making answer that is a name, have capitals on both names '''

            #assigns the answer to the 4th question to the variable 'name_answer'
            name_answer = self.user_results[3]
            # splits the string into a list containing the names
            name_answer = name_answer.split()
            # checks to see if the name entered consists of anything other
            # than 2 names
            if len(name_answer) != 2:
                # tells the user that the answer should be made of 2 names
                print("Question 4 - answer should consist of 2 names")
                print()
            # if the name is made of 2 names, the following code is run
            else:
                # takes the second item in the list and changes the first
                # character to a capital letter, before reassigning it in the list
                name_answer[1] = name_answer[1][:1].upper() + name_answer[1][1:]
                # reassigns the 4th item in the 'self.user_results' list with the
                # modified items in the 'name_answer' joined together into a string
                self.user_results[3] = " ".join(name_answer)

            '''checks to see if the answer is one of the answer choices '''

            # creates a counter variable and sets it to 0 
            num = 0
            # this for loop iterates through each item stored in the
            # 'self.user_results' list
            for i in self.user_results:
                # checks to see if the answer is in the 'self.answers' list
                if i in self.answers[num]:
                    # allows the program to proceed
                    pass
                # if the answer is not in the 'self.answers' list, the following
                # code is executed
                else:
                    # tells the user that the answer they entered for a
                    # specified question is invalid
                    print("Question", num+1, "- Invalid answer")
                    print()
                # increments the value of the counter varible by 1
                num += 1

            ''' checking to see if the answer is correct '''

            # creates a counter variable and assigns it the value 0
            count = 0
            # this for loop increments through each item stored in the
            # 'self.user_results' list
            for i in self.user_results:
                # takes the item stored in the 'self.results' list at a certain
                # index position and assigns it to the variable 'position'
                # after converting it into an integer
                position = int(self.results[count])
                # checks to see if the value stored in the 'self.answers' list
                # for a specific question, at the index position of 'position'
                # minus 1, is the same as the users answer
                if i == self.answers[count][position-1]:
                    # assigns the Boolean value of True to the variable 'result' 
                    result = True
                    # adds the value stored in variable 'result' to the
                    # 'self.marks' list
                    self.marks.append(result)
                # if the values are not the same, the following code is run
                else:
                    # assigns the Boolean value of False to the variable 'result'
                    result = False
                # increments the value of 'count' by 1
                count += 1
                # tells the user whether their answer is correct or not
                print(count, ") ", result)

    # defines a function called 'check2' that checks the user's results to quiz 2
    def check2(self):
        # checks to see if the 'self.user_results' list is empty, meaning that
        # a file has not been found
        if len(self.user_results) == 0:
            # takes the user out of this subroutine and the program will continue
            pass
        # if the 'self.user_results' list is not empty, the following code will
        # be executed
        else:
            ''' making leading and trailing spaces disappear '''

            # creates a variable called 'loop' and assigns the value 0 to it
            loop = 0
            # this while loop will continue as long as the loop variable
            # does not hold the value 2
            while loop != 2:
                # creates a counter variable and sets it to 0
                count = 0
                # this for loop iterates through each item in the
                # 'self.user_results' list
                for i in self.user_results:
                    # checks to see if the first character of the string is blank
                    if i[:1] == " ":
                        # reassigns the variable with the blank space removed
                        i = i[1:]
                    # checks to see if the last character of the string is blank
                    elif i[-1:] == " ":
                        # reassigns the variable with the blank space removed
                        i = i [:-1]

                    ''' making answers start with capital letter '''

                    # reassigns the variable with the first character being
                    # changed to a capital letter
                    i = i[:1].upper() + i[1:]
                    # reassigns the specified item in the 'self.user_results'
                    # list with the modified variable
                    self.user_results[count] = i
                    # increments the counter variable by 1
                    count += 1
                # increments the 'loop' variable by 1
                loop += 1
            ''' making answer that is a name, have capitals on both names '''

            #assigns the answer to the 4th question to the variable 'name_answer'
            name_answer = self.user_results[3]
            # splits the string into a list containing the names
            name_answer = name_answer.split()
            # checks to see if the name entered consists of anything other
            # than 2 names
            if len(name_answer) != 2:
                # tells the user that the answer should be made of 2 names
                print("Question 4 - answer should consist of 2 names")
                print()
            # if the name is made of 2 names, the following code is run
            else:
                # takes the second item in the list and changes the first
                # character to a capital letter, before reassigning it in the list
                name_answer[1] = name_answer[1][:1].upper() + name_answer[1][1:]
                # reassigns the 4th item in the 'self.user_results' list with the
                # modified items in the 'name_answer' joined together into a string
                self.user_results[3] = " ".join(name_answer)

            '''checks to see if the answer is one of the answer choices '''

            # creates a counter variable and sets it to 0 
            num = 0
            # this for loop iterates through each item stored in the
            # 'self.user_results' list
            for i in self.user_results:
                # checks to see if the answer is in the 'self.answers' list
                if i in self.answers[num]:
                    # allows the program to proceed
                    pass
                # if the answer is not in the 'self.answers' list, the following
                # code is executed
                else:
                    # tells the user that the answer they entered for a
                    # specified question is invalid
                    print("Question", num+1, "- Invalid answer")
                    print()
                # increments the value of the counter varible by 1
                num += 1

            ''' checking to see if the answer is correct '''

            # creates a counter variable and assigns it the value 0
            count = 0
            # this for loop increments through each item stored in the
            # 'self.user_results' list
            for i in self.user_results:
                # takes the item stored in the 'self.results' list at a certain
                # index position and assigns it to the variable 'position'
                # after converting it into an integer
                position = int(self.results[count])
                # checks to see if the value stored in the 'self.answers' list
                # for a specific question, at the index position of 'position'
                # minus 1, is the same as the users answer
                if i == self.answers[count][position-1]:
                    # assigns the Boolean value of True to the variable 'result' 
                    result = True
                    # adds the value stored in variable 'result' to the
                    # 'self.marks' list
                    self.marks.append(result)
                # if the values are not the same, the following code is run
                else:
                    # assigns the Boolean value of False to the variable 'result'
                    result = False
                # increments the value of 'count' by 1
                count += 1
                # tells the user whether their answer is correct or not
                if result is True:
                    print(count, ") Correct")
                else:
                    print(count, ") Incorrect")
                
    # defines a function called 'mark'
    def mark(self):
        # checks to see if the 'self.marks' list is empty, meaning that
        # a file has not been found
        if len(self.marks) == 0:
            # takes the program out of this subroutine
            pass
        # if the 'self.marks' list is not empty, the following code is run
        else:
            # this for loop iterates through each item in the 'self.marks' list
            for item in self.marks:
                # checks to see if the value is equal to the Boolean value True
                if True:
                    # increments the variable 'self.score' by 1
                    self.score += 1
            print()
            # displays the score out of 10 to the user
            print(str(self.score) + "/10")

    # defines a function called 'user_file'
    def user_file(self, quiz):
        # checks to see if the 'self.marks' list is empty, meaning that
        # a file has not been found
        if len(self.marks) == 0:
            # takes the program out of this subroutine
            pass
        # if the 'self.marks' list is not empty, the following code is run
        else:
            # checks to see if the quiz being played is number 1
            if quiz == 1:
                # attempts to open the file 'user_results1.txt', creates the
                # file if it does not exist, and opens in append mode
                # if it does already exist
                file = open("user_results1.txt", "a+")
            # checks to see if the quiz being played is number 2
            elif quiz == 2:
                file = open("user_results2.txt", "a+")
            # writes the information stored in the variable 'self.name' to the file   
            file.write(self.name + " ")
            # writes the information stored in 'self.score' to the file, as a string
            file.write(str(self.score) + " ")
            # assigns the information gathered by the function 'datetime' to
            # the variable called 'time'
            time = str(datetime.datetime.now())
            # writes the information stored in 'time' to the file
            file.write(time)
            # writes a new line to the file
            file.write("\n")
            print()
            # displays to the user that the information has been saved
            print("Information saved successfully")

    # defines a function called 'leaderboard1' that displays the results
    # of all the players who completed quiz number 1
    def leaderboard_1(self):
        # opens the file called 'user_results1' in read mode and assigns
        # the data to the variable 'l'
        l = open("user_results1.txt", "r")
        # uses 'readlines' function to go through each individual line in the
        # file and assign the data to variable 'text'
        text = l.readlines()
        # this for loop iterates through the lines of text in variable 'text'
        for item in text:
            # this for loop interates through each integer until it reaches
            # the value that is length - 1
            item = item.split()
            # adds the 'item' list to the 'self.lead' list
            self.lead.append(item)

        ''' bubble sort '''

        # assigns the length of the 'self.lead' list to the variable 'length'
        length = len(self.lead)
        # creates a while loop that will continue until length is equal to 1
        while length != 1:
            # this for loop interates through each integer until it reaches
            # the value that is length - 1
            for count in range(length-1):
                # checks to see if the score in one player entry is smaller
                # than the score of the adjacent player entry
                if int(self.lead[count][1]) < int(self.lead[count + 1][1]):
                    # assigns the bigger value to the variable 'temp'
                    temp = self.lead[count + 1]
                    # assigns the smaller value to the previously bigger
                    # value's position in the list
                    self.lead[count + 1] = self.lead[count]
                    # assigns the value stored in 'temp' to the previously
                    # smaller value's position
                    self.lead[count] = temp
            # decrements the value of length by 1
            length -= 1

        ''' formatting date and time '''

        # this for loop iterates through eacch item in the 'self.lead' list
        for item in self.lead:
            # uses string splitting to take just the day/month part of the date
            date =  item[2][8:] + "/" + item[2][5:7]
            # reassigns this formatted date to the correct position in the list
            item[2] = date
            # uses string splitting to take part of the time to be displayed
            time = item[3][:5]
            # reassigns this formatted time to the correct position in the list
            item[3] = time

        # prints out which leaderboard is going to be displayed
        print("Leaderboard for Quiz 1")

        # uses the numpy module to create an array that is compatible
        # with the numpy functions
        m = np.array(self.lead)
        # creates the headers for the leaderboard
        headers = ["Name", "Score", "Date", "Time"]
        # creates the leaderboard table using the 'tabulate' function
        table = tabulate(m, headers, tablefmt="fancy_grid")
        # displays the leaderboard to the user
        print(table)

    # defines a function called 'leaderboard_2' that displays the results
    # of all the players who completed quiz number 2
    def leaderboard_2(self):
        # opens the file called 'user_results1' in read mode and assigns
        # the data to the variable 'l'
        l = open("user_results2.txt", "r")
        # uses 'readlines' function to go through each individual line in the
        # file and assign the data to variable 'text'
        text = l.readlines()
        # this for loop iterates through the lines of text in variable 'text'
        for item in text:
            # uses the 'split' function to have each word or phrase separated
            # by a space, held as a separate item in a list
            item = item.split()
            # adds the 'item' list to the 'self.lead' list
            self.lead.append(item)

        ''' bubble sort '''

        # assigns the length of the 'self.lead' list to the variable 'length'
        length = len(self.lead)
        # creates a while loop that will continue until length is equal to 1
        while length != 1:
            # this for loop interates through each integer until it reaches
            # the value that is length - 1
            for count in range(length-1):
                # checks to see if the score in one player entry is smaller
                # than the score of the adjacent player entry
                if int(self.lead[count][1]) < int(self.lead[count + 1][1]):
                    # assigns the bigger value to the variable 'temp'
                    temp = self.lead[count + 1]
                    # assigns the smaller value to the previously bigger
                    # value's position in the list
                    self.lead[count + 1] = self.lead[count]
                    # assigns the value stored in 'temp' to the previously
                    # smaller value's position
                    self.lead[count] = temp
            # decrements the value of length by 1
            length -= 1

        ''' formatting date and time '''

        # this for loop iterates through eacch item in the 'self.lead' list
        for item in self.lead:
            # uses string splitting to take just the day/month part of the date
            date =  item[2][8:] + "/" + item[2][5:7]
            # reassigns this formatted date to the correct position in the list
            item[2] = date
            # uses string splitting to take part of the time to be displayed
            time = item[3][:5]
            # reassigns this formatted time to the correct position in the list
            item[3] = time

        # prints out which leaderboard is going to be displayed
        print("Leaderboard for Quiz 2")

        # uses the numpy module to create an array that is compatible
        # with the numpy functions
        m = np.array(self.lead)
        # creates the headers for the leaderboard
        headers = ["Name", "Score", "Date", "Time"]
        # creates the leaderboard table using the 'tabulate' function
        table = tabulate(m, headers, tablefmt="fancy_grid")
        # displays the leaderboard to the user
        print(table)
    

# defines a function called 'main'
def main():
    # displays a welcome message to the user
    print("Welcome to the Quiz Game!")
    # creates an infinite loop that will only be broken by a 'break'
    while True:
        print()
        # takes an input of the user's name and assigns it to variable 'name'
        name = input("Please enter your name: ")
        print("\n")
        # displays the options available to the user
        print("1 - play the game")
        print("2 - view the leaderboard")
        print("3 - quit the game")
        # attempts to take an integer value for the following input
        try:
            # takes an input of the user's choice and assigns it to variable 'choice'
            choice = int(input("> "))
            print()
            # creates an instance of the class 'Quiz', called 'q'
            q = Quiz(name)
            # checks to see if the user's choice is equal to 1
            if choice == 1:
                # attempts to take an integer value for the following input
                try:
                    # takes an input of the choice of quiz and assigns it to the
                    # variable called 'quiz'
                    quiz = int(input("Would you like to play quiz 1 or 2: "))
                    print()
                    # checks to see which quiz the user is playing
                    if quiz == 1:
                        # calls the 'open_file' method in the 'Quiz' class, passing
                        # in the value of the 'quiz' variable
                        q.open_file(quiz)
                        # calls the 'run_quiz'method in the 'Quiz' class
                        q.run_quiz()
                        # calls the 'check1' method in the 'Quiz' class, to
                        # check the answers for quiz 1
                        q.check1()
                    # checks to see which quiz the user is playing
                    elif quiz == 2:
                        # calls the 'open_file' method in the 'Quiz' class, passing
                        # in the value of the 'quiz' variable
                        q.open_file(quiz)
                        # calls the 'run_quiz'method in the 'Quiz' class
                        q.run_quiz()
                        # calls the 'check2' method in the 'Quiz' class, to
                        # check the answers for quiz 2
                        q.check2()
                    # checks to see if the input is neither 1 or 2
                    else:
                        # tells the user that their answer was not accepted
                        # and that the quiz will restart as a result
                        print("Invalid input - the quiz will now restart")
                        # calls the 'main' function to restart the program
                        main()
                    # calls the 'mark' method in the 'Quiz' class
                    q.mark()
                    # calls the 'user_file' method in the 'Quiz' class, passing
                    # in the value of the 'quiz' variable
                    q.user_file(quiz)
                # catches if the user enters anything other than an integer for
                # the 'quiz' input
                except ValueError:
                    # displays a message to the user saying that their input
                    # was not accepted and the quiz will restart
                    print("Invalid input - the quiz will now restart")
                    # calls the 'main' function to restart the quiz
                    main()
            # checks to see if the user's choice is equal to 2
            elif choice == 2:
                # attempts to take an integer value for the following input
                try:
                    # takes an input from the user of which quiz results
                    # they would like to be displayed in a leaderboard and
                    # assigns this value to the variable 'lead'
                    lead = int(input("Would you like to see the leaderboard for quiz 1 or 2: "))
                    # checks to see if the value assigned to the 'lead' variable
                    # if equal to 1
                    if lead == 1:
                        # calls the 'leaderboard_1' method in the 'Quiz' class
                        q.leaderboard_1()
                    # checks to see if the value assigned to the 'lead' variable
                    # is equal to 2
                    elif lead == 2:
                        # calls the 'leaderboard_2' method in the 'Quiz' class
                        q.leaderboard_2()
                    # checks to see if the value assigned to 'lead' is anything
                    # other than 1 or 2
                    else:
                        # tells the user that their input was not accepted and that
                        # the quiz will restart as a result
                        print("Invalid input - the quiz will now restart")
                        # calls the 'main' function to restart the program
                        main()
                # catches if the user enters enything other than an integer for
                # the 'lead' input
                except ValueError:
                    # tells the user that their input was not accepted and that
                    # the quiz will restart as a result
                    print("Invalid input - the quiz will now restart")
                    # calls the 'main' function to restart the quiz
                    main()
            # checks to see if the user's choice is equal to 3
            elif choice == 3:
                # displays a thank you message to the user
                print("Thank you for playing the quiz game!")
                # this command will terminate the program
                break
            # checks to see if the user entered any number other than 1, 2 or 3
            else:
                # tells the user that their input has not been accepted and
                # that the quiz will restart
                print("Invalid input - the quiz will now restart")
                # calls the 'main' function to restart the program
                main()
        # catches is the user enters anything other than an integer for
        # the 'choice' input
        except ValueError:
            # tells the user that their answer has not been accepted and that
            # the quiz will now restart as a result
            print("Invalid input - the quiz will now restart")
            # calls the 'main' function to restart the program
            main()


# calls the 'main' function
if __name__ == "__main__":
    main()
