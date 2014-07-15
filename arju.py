# This Python file uses the following encoding: utf-8
import array
import nltk
f=open("ana-output.txt","r")
string=f.read()
text=string.split(".")
#text= text.split('-')
print text
abc="എതൃ ലാൺ N_NN/നാസ N_NN/വോയജര്‍ DM_DMD/പേടകം N_NN_O_NU/വിക്ഷേപിച്ചത് V_VM_VF/"

abc= abc.split(' ')
i = -1

lis = {}
for item in text:
	item=item.split(' ')
	count = 0
	i=i+1;
	for j in set(abc).intersection(item):
		count=count+1;
	lis[i]=count

print lis

large=0;
id1=0;
for a in lis.keys():
	if lis[a]>large:
		large=lis[a]
		id1=a;

print lis[id1]
print text[id1]
abc="എതൃ ലാൺ N_NN/നാസ N_NN/വോയജര്‍ DM_DMD/പേടകം N_NN_O_NU/വിക്ഷേപിച്ചത് V_VM_VF/"
if abc.startswith("എതൃ"):
    w=text[id1].split()
    str5=w[1]
    if str5.startswith("QT_QTC"):
		#dict['QT_QTC']=w[0]
		print "result" , w[0]#dict['QT_QTC']
                #f_out1.write(w[0]+' '+w[1]+'/')
                        #f_out1.write(w[1])


#print set(abc).intersection(text[id1].split(' '))
#print set(abc).difference(text[id1].split(' '))
#temp=set(text[id1].split(' ')).difference(abc)
#gk=open("answer.txt","w")
#for z in temp:
#	gk.write(z)

