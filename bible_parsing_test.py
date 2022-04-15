from bs4 import BeautifulSoup
import requests
import os

def parseBible(url):
    print("###" + url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    rawText = soup.find_all("span", "txt")

    bible = []

    for item in rawText:
        text = str(item)
        text = text[text.find('>')+1:]
        text = text[text.find('>')+1:]
        text = text[:text.find('<')] + " " + text[text.find('>')+1:]

        while text.find('<')!=-1:
            tmp_text = text[:text.find('<')] + text[text.find('>')+1:]
            text = tmp_text
        bible.append(text)
    
    return bible

def cutRange(bible):
    verse = len(bible)

    begin = input('시작 절 입력 (1~' + str(verse)+ ') : ')
    begin = int(begin)
    while (begin<1 or begin>verse):
        begin = input('시작 절 입력 (1~' + str(verse) +') : ')
        begin = int(begin)

    end = input('끝 절 입력 ('+ str(begin) + '~' + str(verse) +') : ')
    end = int(end)
    while (end<begin or end>verse):
        end = input('끝 절 입력 ('+str(begin)+'~'+ str(verse)+ ') : ')
        end = int(end)
    return bible[begin-1:end]

def Writer(target):
    f = open("C:\\Users\\user\\Documents\\python\\parsingBible.txt", "w")
    for t in target:
        f.write(t + '\n\n')
    f.close()
    os.system("C:\\Users\\user\\Documents\\python\\parsingBible.txt")

old = ['gen', 'exo', 'lev', 'num', 'deu', 'jos', 'jdg', 'rut', '1sa', '2sa', '1ki', '2ki', '1ch', '2ch', 'ezr', 'neh', 'est', 'job', 'psa', 'pro', 'ecc', 'sng', 'isa', 'jer', 'lam', 'ezk', 'dan', 'hos', 'jol', 'amo', 'oba', 'jnh', 'mic', 'nam', 'hab', 'zep', 'hag', 'zec', 'mal']
new = ['mat', 'mrk', 'luk', 'jhn', 'act', 'rom', '1co', '2co', 'gal', 'eph', 'php', 'col', '1th', '2th', '1ti', '2ti', 'tit', 'phm', 'heb', 'jas', '1pe', '2pe', '1jn', '2jn', '3jn', 'jud', 'rev']

old_bible = ['창세기','출애굽기','레위기','민수기','신명기','여호수아',
             '사사기','룻기','사무엘상','사무엘하','열왕기상','열왕기하',
             '역대상','역대하','에스라','느헤미야','에스더','욥기','시편',
             '잠언','전도서','아가','이사야','예레미야','예레미야애가','에스겔',
             '다니엘','호세아','요엘','아모스','오바댜','요나','미가','나훔',
             '하박국','스바냐','학개','스가랴','말라기']

old_bible_eng = ['ckdtprl','cnfdornqrl','fpdnlrl','alstnrl','tlsaudrl','dughtndk',
                 'tktkrl','fntrl','tkandpftkd','tkandpfgk','dufdhkdrltkd','dufdhkdrlgk',
                 'dureotkd','dureogk','dptmfk','smgpaldi','dptmej','dyqrl','tlvus',
                 'wkadjs','wjsehtj','dkrk','dltkdi','dPfpaldi','dPfpaldidork','dptmrpf',
                 'eksldpf','ghtpdk','dydpf','dkahtm','dhqkei','dysk','alrk','skgna',
                 'gkqkrrnr','tmqksi','gkrro','tmrkfi','akffkrl']

new_bible = ['마태복음','마가복음','누가복음','요한복음','사도행전','로마서',
             '고린도전서','고린도후서','갈라디아서','에베소서','빌립보서','골로새서','데살로니가전서',
             '데살로니가후서','디모데전서','디모데후서','디도서','빌레몬서','히브리서',
             '야고보서','베드로전서','베드로후서','요한1서','요한2서','요한3서',
             '유다서','요한계시록']

new_bible_eng = ['akxoqhrdma','akrkqhrdma','snrkqhrdma','dygksqhrdma','tkehgodwjs','fhaktj',
                 'rhflsehwjstj','rhflsehgntj','rkffkeldktj','dpqpthtj','qlfflqqhtj','rhffhtotj',
                 'eptkffhslrkwjstj','eptkffhslrkgntj','elahepwjstj','elahepgntj','elehtj','qlffpahstj','glqmfltj',
                 'dirhqhtj','qpemfhwjstj','qpemfhgntj','dygks1tj','dygks2tj','dygks3tj','dbektj','dygksrPtlfhr']

book_name = input('성경 입력 : ')

while(True):
    if book_name in old_bible:
        book_number = old_bible.index(book_name)
        book_code = old[book_number]
        break
    elif book_name in old_bible_eng:
        book_number = old_bible_eng.index(book_name)
        book_code = old[book_number]
        break
    elif book_name in new_bible:
        book_number = new_bible_index(book_name)
        book_code = new[book_number]
        break
    elif book_name in new_bible_eng:
        book_number = new_bible_eng.index(book_name)
        book_code = new[book_number]
        break
    else:
        book_name = input('성경 입력 : ')

chap = input('장 입력 : ')

url = 'http://bible.godpia.com/read/reading.asp?ver=gae&ver2=&vol=' + book_code + '&chap=' + chap + '&sec='
bible = parseBible(url)

while not bible:
    print('Wrong!')
    chap = input('장 입력 : ')
    url = 'http://bible.godpia.com/read/reading.asp?ver=gae&ver2=&vol=' + book_code + '&chap=' + chap + '&sec='
    bible = parseBible(url)

target = cutRange(bible)

Writer(target)
