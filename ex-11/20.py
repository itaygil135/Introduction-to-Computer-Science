YES = 'y'
NO = 'n'

def get_yes_no_answer(question):
    while True:
        answer = input(question + " ")
        if answer== YES:
            return True
        elif answer == NO:
            return False
        else:
            print ("i did not undertand")


class Question:
    def __init__(self, question_text, yes_answer=None, no_answer=None):
        self.__question_text = question_text
        self.__on_yes_answer = yes_answer
        self.__on_no_answer = no_answer

    def ask_question(self):
        if self.__on_no_ansewr is not None:
            if get_yes_no_answer(self.__question_text):
                self.__on_yes_answer.ask_question()
             else:
                self.__on_no_ansewr.ask_question()
        else:
            if get_yes_no_answer("is it " + self.__question_text + "?"):
                print("I new it ")
            else:
                print("I guessed wrong")
                self.__add_new_question()

    def __add_new_question(self):
        other_answer = input("what did you have in minde?")
        new_question = input("please enter a question to differentiate betweedn " +\
                                self.__question_text + "and " + other_answer +": ")
        if get_yes_no_answer(self.__question_text + ". " + new_question):
            self.__on_yes_answer = Question(self.__question_text)
            self.__on_no_answer = Question(other_answer)
        else:
            self.__on_yes_answer = Question(other_answer)
            self.__on_no_answer = Question(self.__question_text)
        self.__question_text = new_question


def play_twenty_questions():
    root_question = Question("a sparrow")

    print("lets play")
    print("I willguess")
    root_question.ask_question()
    while get_yes_no_answer("\n\n Do you want ot play?"):
        root_question.ask_question()

    print("\n\n here are all the possible answer entered ito the gaem:")
    root_question.print_all_answers()


def print_all_answers

if __name__ == "__manin__":
    play_twenty_questions()

            '''
            i = 0
            root_question(symptome[i])
            
            
            
            def root_question(self):
            if i < len (symptome)  # no more symptomesn
                root_question(yes, i - 1)   update and send the path_to_this_leaf
                root_wuestion (no, i - 1)   update and send the path_to_this_leaf
            else:
                illness = fine_illness(path_to_this_leaf  === list of symptoms that are yes and list of symptome that are no)
                create/update leaf with the illness
                
            clean the path_to_this_leaf    
                
                
                
            def find_ilnnese(self, records, path_to_this_leaf)
                for  record in recores:
                    if record has all "yes symptomes" and does not have all "no symptom":
                        if record.illense in cadidate_lsit:
                            increates illnese.counter
                        esle:
                            add record to candidate_list with counter = 1
                if there is no illnese in the cadidate_list - return None
                elif there is one illenss with higher than all --> return it
                else - return one of the illness at the candidate_list
                
            '''