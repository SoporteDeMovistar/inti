str = open("log.txt","r").read()
lista=str.split("commit")
alt = lista [4]
alt2= alt.split("Date")
alt3= alt2[1]
alt4= alt3.split("\n")
alt5= alt4[1:]
print(''.join(alt5))
