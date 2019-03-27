import requests
topics = [ 'DNA','Apple','Epigenetics','Hollywood','Maya','Microsoft','Precision','Tuscany','99 balloons','Computer Programming','Financial meltdown','Justin Timberlake','Least Squares','Mars robots','Page six','Roman Empire','Solar energy','Statistical Significance','Steve Jobs','The Maya','Triple Cross','US Constitution','Eye of Horus','Madam I’m Adam','Mean Average Precision','Physics Nobel Prizes','Read the manual','Spanish Civil War','Do geese see god','Much ado about nothing' ]

URL = 'https://en.wikipedia.org/wiki/'

for topic in topics:
    wiki_page = requests.get(URL+topic)
    file_name = topic+'.txt'
    file = open(file_name,"w")
    file.write(str(wiki_page.content))
    file.close()
    #print(wiki_page.content)