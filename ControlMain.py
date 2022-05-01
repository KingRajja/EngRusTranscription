from DB.DBControl import DB
import sqlite3

conn = sqlite3.connect('DB/Dictonary.db')
cur = conn.cursor()
db = DB(conn,cur)

print(db.getTrans('egg'))


'''
f = open('Dictonary', 'r', encoding='utf-8')
eng_text = open('EngText', 'r', encoding='utf-8')
dictonary = []
class Word(object):
    def __init__(self,eng,trans):
        self.eng = eng
        self.trans = trans
for line in f:
    fline = line.replace('\n','')
    temp = fline.split('[')
    dictonary.append(Word(temp[0].lower()[:len(temp[0])-1],temp[1].replace(']','').lower()))

for line in eng_text:
    if line != '\n':
        fline = line.replace('\n','').replace('. ', '.\n').replace('? ', '?\n').replace('! ', '!\n')
        line_arr = fline.split('\n')
        for str in line_arr:
            str = f'{str}.'.replace('..','.').replace('!.','!').replace('?.','?')
            print(str)
            temp_1 = ""
            for word in str.split(' '):
                temp = word.lower().replace('.','').replace(',','').replace('!','').replace('?','').replace(':','')
                if search_word(temp) == None:
                    temp_1+= f'{temp} '
                else:
                    temp_1+= f'{search_word(temp).lower()} '
            print(f'{temp_1}\n')
'''