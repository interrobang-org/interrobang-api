from textblob import TextBlob
import nltk
from textblob import Word
import random
import json

verbose=False
 
def parse(string, max_questions):
    """
    Parse a paragraph. Devide it into sentences and try to generate quesstions from each sentences.
    """
    print("inside parse")
    question = []
    answer = []
    selected_questions = []
    selected_answers = []
    try:
        txt = TextBlob(string)
        print("after text blob")
        # Each sentence is taken from the string input and passed to genQuestion() to generate questions.
        for sentence in txt.sentences:
            single_question, single_answer = genQuestion(sentence)
            if single_question:
                question.append(single_question)
                answer.append(single_answer)
 
        if max_questions >= len(question):
            return question, answer
 
        while (max_questions > 0):
           i = random.randint(0, len(question)-1)
           if question:
               selected_questions.append(question[i])
               selected_answers.append(answer[i])
               del question[i]
               del answer[i]
               max_questions -= 1
 
           else:
               break
        print("before return")
        return json.dumps(selected_questions), json.dumps(selected_answers)
 
    except Exception as e:
        raise e
 
 
def genQuestion(line):
    """
    outputs question from the given text
    """
    if type(line) is str:     # If the passed variable is of type string.
        line = TextBlob(line) # Create object of type textblob.blob.TextBlob
 
    bucket = {}               # Create an empty dictionary
 
    subject_list = []
    question_subject=""
    answer_subject=""
    for i,j in enumerate(line.tags):  # line.tags are the parts-of-speach in English        
        question_subject += j[0] + " "
        if (j[1] == "NNP" or j[1] == "NNS"):      
            subject_list.append(j[0])
        if j[1] not in bucket:
            bucket[j[1]] = i  # Add all tags to the dictionary or bucket variable
 
    if len(subject_list):
        random_subject_val = random.randint(0, len(subject_list)-1)
        question_subject = question_subject.replace(str(subject_list[random_subject_val]), "______")
        answer_subject = str(subject_list[random_subject_val])
   
    return question_subject, answer_subject
 
 
def extractQuestions(textinput, max_questions):
    #verbose mode is activated when we give -v as argument.
    global verbose
    if verbose == '-v':
        print('Verbose Mode Activated\n')
        verbose = True
 
    return parse(textinput, max_questions)
 
def main():  
    """
    Accepts a text file as an argument and generates questions from it.
    """
 
    # Set verbose if -v option is given as argument.
    if len(sys.argv) >= 3:
        if sys.argv[2] == '-v':
            print('Verbose Mode Activated\n')
            verbose = True
 
    # Open the file given as argument in read-only mode.
    filehandle = open(sys.argv[1], 'r')
    textinput = filehandle.read()
    # print('\n-----------INPUT TEXT-------------\n')
    print(textinput,'\n')
    # print('\n-----------INPUT END---------------\n')
 
    # Send the content of text file as string to function parse()
    questions, answers = extractQuestions(textinput, 10)
    # print("Questions \n ----------------")
    # print(questions)
    # print("\n Answers \n ----------------")
    # print(answers)