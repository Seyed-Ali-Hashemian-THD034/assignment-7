#Crazy translator

my_dict=[]
def load():
    print("*LOADING...*")
    my_file=open("Dictionary.txt" , "r")
    my_dict=my_file.read().split("\n")

    for i in range(0,len(my_dict),2):
            my_dict.append({"wordenglish":my_dict[i], "wordpersian" : my_dict[i+1]})

    from pyfiglet import Figlet
    f= Figlet(font="standard")
    print(f.renderText("Crazy translator"))

    print ('''If you do not know the meaning of a word, he does not know the meaning of that word!
    So what good is it? ''')

def options():
    print("1- add new word to Dictionary")
    print("2-English => persian")
    print("3-persian <= English")
    print("4- show_menu ")
    print("5- exit")

def add_word_to_Dictionary():
    eng=input("Write the word in English: ")
    per=input("Write the word in Persian: ")
    my_dict.append({"wordenglish" : eng ,"wordpersian" : per})
    dict=open("Dictionary.txt" , "a")
    dict.write("\n" +eng) 
    dict.write("\n" +per )
    print("completed ")
    dict.close()

def translation_persian_to_English():
    sentence =input ("Well, type your sentence: ")
    perword = sentence.split( )
    for i in range(len(my_dict)):
        for j in range (len(perword)):
            if perword[i] == my_dict[j]["wordpersian"]:
                print(my_dict[j]["wordenglish"] , end=" ")
                break
            else:
             print(perword )
                
def translation_English_to_persian():
    sentece = input("Well, type your sentence: ")
    engword = sentece.split( )
    for i in range(len(my_dict)):
        for j in range(len(engword)):
            if engword[i]==my_dict[j]["wordenglish"]:
                print(my_dict[j]["wordpersian"] , end= " ")
            else:
                print(engword)

load()                        
while True:
    options()
    choice = input("What should we do? Select from the list.")
    if choice=="1":
        add_word_to_Dictionary()
    elif choice=="2":
        translation_persian_to_English()
    elif choice=="3":
        translation_English_to_persian()
    elif choice=="4":
        options()
    elif choice=="5":
        exit()