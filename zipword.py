import zipfile
import time
folderpath=input('path to the file:')
zipf=zipfile.ZipFile(folderpath)
global result
result=0
global tried
tried=0
c=0
if not zipf:
    print('the zipped file/folder is not password protected ! you can successfully open it!')
else:
    starttime=time.time()
    wordlistfile=open('wordlist.txt','r',errors='ignore')
    body=wordlistfile.read().lower()
    words=body.split('\n')

    for i in range(len(words)):
        word=words[i]
        password=word.encode('utf-8').strip()
        c+=1
        print('trying to decode password by:{}'.format(word))
        try:
            with zipfile.ZipFile(folderpath,'r') as zf:
                zf.extractall(pwd=password)
                print('success the password is :'+word)
                endtime=time.time()
                result=1
            break
        except:
            pass
    if result==0:
        print('sorry , password not found. a total of'+str(c)+'+possible combo tried in seconds.password is not of 4 characters')
    else:
        duration=endtime-starttime
        print('congs!!password found after trying'+str(c)+'combinations in'+str(duration)+'seconds')

