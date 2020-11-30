import os
import random

class WordList():  
    word_list = []
    def __init__(self): 
        list = self.__read_file()
        self.word_list = self.__split_list_in_words(list)

    def __split_list_in_words(self, list):
        word_list = []
        for line in list:
            res = line.split(';')
            word_list.append(res)
        return word_list

    def __read_file(self):
        try: 
            file = open("termen.txt", "r")
            list = []
            for line in file.readlines():
                if line.strip():
                    list.append(line.rstrip())
            file.close()
        except:
            return "niet gelukt"
        return list

    def get_word_list(self): 
        return self.word_list   

class WordGame():
    wordlist = []
    def __get_word(self): 
        random.shuffle(self.wordlist)
        return self.wordlist[0]

    def print_explanation(self): 
        os.system('cls' if os.name=='nt' else 'clear')
        print("**********************************************************************")
        print("* Bij Scheikunde atomen leren. Je krijgt eerst het atoom. Geef de    *")
        print("* afkorting en daarna metaal of niet-metaal. Volgende ronde krijg    *")
        print("* je de afkorting en mag je de volledige naam invoeren.              *")
        print("**********************************************************************")

    def play(self): 
        keep_playing = True
        while keep_playing:
            wordlist = WordList()
            self.wordlist = wordlist.get_word_list()    
            self.print_explanation()
            while (len(self.wordlist) > 0): 
                play_word = self.__get_word()
                answer = input("({})  ==> {} : ".format(str(len(self.wordlist)),play_word[0]))
                answerlist = answer.split(" ")
                if len(answerlist) == 2: #check whether two words have been entered 
                    afkorting = answerlist[0] 
                    metaal = answerlist[1]
                    if (afkorting == play_word[1]) and (metaal.lower() == play_word[2].lower()): 
                        del self.wordlist[0]
                    else:
                        print("Helaas: de afkorting is \033[92m{}\033[0m  en het is \033[92m{}\033[0m".format(play_word[1], play_word[2]))
                else:
                    print("Geef de afkorting en metaal of niet-metaal.")
            again = input("Lekker bezig!! Nog een keer oefenen (Y)?")
            if not (again.lower() == "y"): 
                keep_playing = False

g = WordGame()
g.play() 
