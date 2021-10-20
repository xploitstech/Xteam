import urllib.request, requests
import os, sys, time
###############

W = "\033[0m"
G = '\033[32;1m'
Y = '\033[33;1m'
R = '\033[31;1m'
B = '\033[1;34;40m'
LB = '\033[1;36;40m'
BG_R = '\033[0;37;41m'
BG_G = '\033[0;37;42m'
BG_P = '\033[0;37;44m'
BG_K = '\033[0;37;45m'

dict = {
	"FirstMsg" :   "		WELCOME TO XTEAM\n		How Are You Doing ? ",
	"Answer" : " I Hope You're Good",
	"Spaces" : "\n",
	"No Internet" : " You Are Not Connected ",
	"Check" : "You Must Be Connected With Internet ",
	"Connected" : "You Are Connected\n",
	"Try" : "Try Again\n",
	"GoodBye" : "[~] See You Later ",
	"IK" : '"',
	"Help" : '''
	 ----------------------------------------------------
	| Command                | For What                  |
	 ----------------------------------------------------
	| Help                   | Show Help Table           |
	······················································
	| CTRL + C + ENTER       | EXIT FROM THE TOOL        |
	······················································
	| Exit                   | EXIT FROM THE TOOL	     |
	······················································
        | Enter A Username       | Dump All User Information |
	 ----------------------------------------------------

''',
	"Draw" : '''
        +++++++++++++ X TEAM +++++++++++
	    + - -- [ coded BY incredible hacker ]
	    + - -- [ V 1.5 ]
	    + - -- [ YouTube : XPLOITSTECH ]
            + - -- [ Telegram : @xploitstech]

	>>>  EXIT USE : CTRL + C + ENTER  <<<
''',
	"Draw2" : '''
	  、[ DOWNLOAD ALL POSTS FROM INSTAGRAM ]
	  、[ GET USERS FROM ANY HASHTAG ]
''',
	"Draw3" : '''
		、[ Internet connection required ]

''',
	"Headers" : {
				"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
				"X-requested-with" : "XMLHttpRequest",
				"Accept" : "*/*",
				"Content-type" : "application/json; charset=utf-8"
			}
}

def Flush(Which, Color1, Color2, SleepTime1, SleepTime2):
    for char in Which :
        sys.stdout.write(Color1+char+Color2)
        sys.stdout.flush()
        time.sleep(SleepTime1)
    time.sleep(SleepTime2)
    
def connect():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False
        
def main():
    Flush(dict["Connected"], BG_G, W, 0.05, 0.3)
    os.system('clear')
    Banner()

def FalseMain():
    Flush(dict["No Internet"], BG_R, W, 0.05, 1)
    print ("                        ", end="\r")
    print (BG_R+dict["No Internet"]+W, end="\r")
    Flush(dict["Check"], Y, W, 0.1, 0)
    Flush(dict["Try"] , BG_R, W, 0.1, 0)
    sys.exit()

def Banner():
    Flush(dict["Draw"], Y, W, 0.03, 0)
    Flush(dict["Draw2"], LB, W, 0.03, 0)
    Flush(dict["Draw3"], B, W, 0.03, 0)

def Screen():
    os.system('clear')
    Flush(dict["Spaces"]*14, W, W, 0.01, 0)
    Flush(dict["FirstMsg"], B, W, 0.05, 0.5)
    Flush(dict["Answer"], G, W, 0.03, 0)
    Flush(dict["Spaces"]*4, W, W, 0.01, 0)
    connect()
    if connect() :
        main()
    else :
        FalseMain()
