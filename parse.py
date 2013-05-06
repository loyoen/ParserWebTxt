# coding=utf-8
import urllib2
url='http://www.5kwx.com/book/0/1/287025.html'
baseurl = 'http://www.5kwx.com/book/0/1/'
nextpage='287025.html'
f=open('f.txt','w')
while nextpage!='index.html':
    content=urllib2.urlopen(baseurl+nextpage).read()
    nstartpos=content.find('div id=\"booktext\"')
    nendpos  =content.find('div class=\"movenext\"')
    ans=content[nstartpos:nendpos]
    ans = ans.replace('&nbsp;',' ').replace('<br />','')
    f.write(ans)
    n = content.find('·µ»ØÄ¿Â¼')
    while content[n]!='\"':
        n += 1
    n += 1
    temp=''
    while content[n]!='\"':
        temp += content[n]
        n += 1
    nextpage = temp
    print nextpage
f.close()
    

        


