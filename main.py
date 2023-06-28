import re

def ra(string):
    return re.sub(r'\W+', '', string)


class song_lyric:
    def __init__(self,slyrics):
        #linenum = 0
        #pos = 0
        self.given_up = False
        self.lyrics = []
        for line in slyrics.split("\n") :
            cline = []
            for word in line.split():
                cline.append(lyric(word))
            self.lyrics.append(cline)
    def print(self):
        print("*" * 200 + '\n' * 5)
        for line in self.lyrics:
            cline = ""
            for word in line:
                cline += word.get() + " "
            print(cline) 
    def print2(self):
        clines = []
        for line in self.lyrics:
            
            cline = ""
            for word in line:
                cline += word.get() + " "
            if(len(cline) < 100):
                cline = cline + (100 - len(cline)) * ' '
            clines.append(cline)

        #print(clines)    
        l = int (len(clines) / 2)
        for i in (range(l)):
            print(clines[i] + clines[i+l])
    def print3(self):
        clines = []
        buf = []
        for line in self.lyrics: 
            cline = ""
            for word in line:
                cline += word.get() + " "
            if(cline.find('*') != -1):
                if(len(cline) < 100):
                    cline = cline + (100 - len(cline)) * ' '
                clines.append(cline)
            

        #print(clines)    
        l = int (len(clines) / 2)
        for i in (range(l)):
            print(clines[i] + clines[i+l])
    def print4(self):
        clines = []
        for line in self.lyrics:
            
            cline = ""
            for word in line:
                cline += word.get() + " "
            if(len(cline) < 100):
                cline = cline + (100 - len(cline)) * ' '
            clines.append(cline)
        i = 0
        while i < len(clines):
            guessed = True
            for j in range(max(i-3,0),min(i+4,len(clines))):
                #print("len",len(clines))
                #print(j)
                #print(clines[j].find('*'),clines[j])
                guessed = guessed and clines[j].find('*') == -1
                #print(guessed)
            if(guessed and i < len(clines) and i > -1):
                #print(i)
                del clines[i]
            else: i+=1
            
        #print(clines)    
        l = int (len(clines) / 2)
        print("*" * 200 + '\n' * 5)
        for i in (range(l)):
            print(clines[i] + clines[i+l])
    def guess(self,guess):
        if(guess == "[debug lyrics]"):
            self.debug_lyrics()
        if(guess == "[give up]"): 
            self.give_up()
            return False
        for line in self.lyrics:
            for word in line:
                if(ra(guess.lower()) == ra(word.word.lower())):
                    word.guessed = True
    def guessed(self):
        if(self.given_up):
            return True
        for line in self.lyrics:
            for word in line:
                if(word.guessed == False):
                    return False
        return True
    def debug_lyrics(self):
        print("*" * 200 + '\n' * 5)
        for line in self.lyrics:
            cline = ""
            for word in line:
                cline += word.word + " "
            print(cline)
    def give_up(self):
        all = 0
        correct = 0
        self.given_up = True
        for line in self.lyrics:
            for word in line:
                if(word.guessed == True): correct += 1
                all += 1
        print("A helyes megfejtés:")
        self.debug_lyrics()
        print("{0}/{1} szót találtál el.".format(correct,all))
        print("Ez {0}%".format(round(correct/all*100,4)))
       

class lyric:
    def __init__(self,word):
        self.word = word
        #self.line = line
        #self.pos = pos
        self.guessed = False
    def get(self):
        if(self.guessed):
            return (self.word)
        else:
            return (len(self.word) * '*')

f = open("input.txt","r",encoding="utf=8")
lyrics = song_lyric(f.read())

print( (not lyrics.guessed()) == True)
print(True)

while( (not lyrics.guessed()) == True):
    lyrics.print4()
    lyrics.guess(input("Enter guess:"))

