# This Python file uses the following encoding: utf-8
import os
import re
import MalayalamStemmer as mal
import ddupli
KB=[[]]
tx=[]
tg=[]
def read_in_text(string):
	text=string.split()
	'''	
	for i in range(len(text)):
		print text[i].encode('utf-8')
	'''
	f=open("1test","w")
	for i in range(len(text)):	
		f.write(text[i].encode('utf-8')+"\n")
	f.close()
#######################

def read_in_que(string):
	text=string.split()
	'''	
	for i in range(len(text)):
		print text[i].encode('utf-8')
	'''
	f=open("qa_test","w")
	for i in range(len(text)):	
		f.write(text[i].encode('utf-8')+"\n")
	f.close()
#####################

def stem():
        f_in=open("1test",'r')
        words=f_in.read().split('\n')
	'''
	for i in range(len(text)):
		print text[i].encode('utf-8')
	'''
        f_out=open("test","w")
        for i in words:
	 stem=mal.findstem(i)
	 f_out.write(stem+"\n")
        f_out.close()
#########################
def que_stem():
        f_in=open("qa_test",'r')
        words=f_in.read().split('\n')
	f_in.close()
	'''
	for i in range(len(text)):
		print text[i].encode('utf-8')
	'''
        f_out=open("qaotest","w")
        for i in words:
	 stem=mal.findstem(i)
	 f_out.write(stem+"\n")
        f_out.close()

	
##########################
def read_in_file(path):
	f=open(path,"r")
	string=f.read()
	text=string.split()
	'''	
	for i in range(len(text)):
		print text[i].encode('utf-8')
	'''
	f=open("1test","w")
	for i in range(len(text)):	
		f.write(text[i]+"\n")
	f.close()
	return string
def read_file(path):
	f=open(path,"r")
	string=f.read()
	
	'''	
	for i in range(len(text)):
		print text[i].encode('utf-8')
	'''
	
	f.close()
	return string

def tnt_tagging():
	os.system("./tnt corpus test>temp")
def in_file_tagging():
	
	
	f=open("temp","r")
	text=f.read().split("\n")
	f.close()
	f=open("output","w")
	for i in range(len(text)):		
		if not text[i].startswith("%"):
			f.write(text[i]+"\\")
	f.close()
	q=open("output","r")
        qw=q.read()
        w=re.sub( '\s+', ' ', qw ).strip()
	q.close()
	f_out1=open("space.txt",'w')
	f_out1.write(w)
	f_out1.close()	
####################################################
#anaphora..........................
	f_in = open('space.txt', 'r')
	text = f_in.read()
	f_in.close()
	word_list={}
	word_list=text.split("\\")
#for word in word_list:
	#print word

#no_of_words=len(word_list)
	w={}
	dict_ana={}
	dict ={'N_NNP_O_NU':'null','PR_PRP_':'null','N_NNP':'null'}
#f_out = open('qweryqwery.txt','w')
	f_out1 = open('ana-output.txt','w')
	print len(word_list)
	for word in word_list:
		w=word.split()
       # f_out = open('qweryqwery.txt', 'w')
        #f_out.write(w[0])
		str1=""
		if word is str1:
			w=['null','null']    	
		l=len(w)
	#print w[0]
		str2='null'
		if w[0] is str2:
			break
	#str3='null'
	#if w[0] is str3:
	#	break
       # str4=""
        	str4=w[1]
		print "needed......."+str4
	
        #print w[0] 
        #f_out1.write(w[0])
		if w[1] is str2:
			break
        	if str4.startswith("N_NNP_O_NU"):
			dict['N_NNP_O_NU']=w[0]
			print "result" , dict['N_NNP_O_NU']
                	f_out1.write(w[0]+' '+w[1]+' $')
                        #f_out1.write(w[1])
		elif str4.startswith("N_NNP"):
			dict['N_NNP']=w[0]
			print "result" , dict['N_NNP']
                	f_out1.write(w[0]+' '+w[1]+' $')
                        #f_out1.write(w[1])
		elif str4.startswith("DM_DMD"):
			w[0]=dict['N_NNP']
			print "result" , w[0]
                	f_out1.write(w[0]+' '+w[1]+' $')
                        #f_out1.write(w[1])
		elif str4.startswith("PR_PRP_"):
			w[0]=dict['N_NNP_O_NU']
			print "result" , w[0]
                	f_out1.write(w[0]+' '+w[1]+' $')
                        #f_out1.write(w[1])
		
        	else :
        	        f_out1.write(w[0]+' '+w[1]+' $')
          	        continue
        f_out1.close()        
#dict['JJ']=dict['N_NNP_O_NU']
#print "ressssssss" , dict['JJ']
#f_out = open('qwery.txt', 'w')
#f_out1.write(dict['JJ'])

        # else:
	#	continue	
         









	print "koooooiiiiii"

####################################################


	
	#f=open("ana-output.txt","r")
	#text=f.read().split("$")
	#print text
	#f.close()
	


	fin=open("ana-output.txt","r")
	text=fin.read()
	print text
	abc=text.split("$")
	print abc
	fin.close()
	ff=open("output6.txt","w")
	for i in range(len(abc)):
		#print abc[i]
		ff.write(abc[i]+"\n")
  
	ff.close()
	fff=open("output6.txt","r")
	text=fff.read()
	text=text.split("\n")
	print text
	first = ""
	second = ""
	#f_out1=open("testing.txt",'w')
	#file_point=open("output",'w')
	file_point2=open("output00.txt","w")
	file_point2.write("[taggg]\n")
	for abc in text:
		abc=abc.split(' ')
		#if not abc.startswith("%"):
		#	print abc		
		#	w=re.sub( '\s+', ' ', abc ).strip()	
		#	print w			
		#	efg = w.split(' ')		
		#	print efg

		if (abc[0] != ''):
			first = first + abc[0] + " "
			second = second + abc[1]  + " " 
			#file_point2.write(first+" "+second + "\n")

		if (abc[0] == '.'):
			xyz = first + " = " + second + "\n"
			file_point2.write(xyz)
			first = ""
			second = ""
			print xyz
			

	#f_out1.close()		
	#file_point.close()
	file_point2.close()
			

############################
def tnt_qatagging():
	os.system("./tnt corpus qaotest>temp1")
def in_file_qatagging():
	f=open("temp1","r")
	text=f.read().split("\n")
	print text
	f.close()
	first = ""
	second = ""
	f_out1=open("qaoutput",'w')
	f_out1.write("[taggg]\n")
	for abc in text:
		if not abc.startswith("%"):
			print abc		
			w=re.sub( '\s+', ' ', abc ).strip()	
			print w			
			efg = w.split(' ')		
			print efg

			if (efg[0] != ''):
				first = first + efg[0] + " "
				second = second + efg[1]  + " " 
				
#			if (efg[0] == ''):
	xyz = first + " = " + second + "\n"
	f_out1.write(xyz)
	print xyz
		
			

	f_out1.close()

#	f=open("temp1","r")
#	text=f.read().split("\n")
#  	f.close()
#	f=open("qaoutput","w")
#	for i in range(len(text)):		
#		if not text[i].startswith("%"):
#			f.write(text[i]+"\\")
#	f.close()

########################

##########################
def create_KB_tag_lst():
	f=open("output","r")
	text=f.read().split("\n")
	f.close()	
	global tg
	global tx
	tx=[]
	tg=[]
	for i in range(len(text)):
		if not text[i]=="":
			tx.append(text[i].decode('utf-8'))
			tx[i].split()

			tg.append(tx[i].split()[1])
	'''
	for i in range(len(tx)):
		print tx[i]	
	'''
	return tx
def tokens_sentence(raw_txt):
    tokenize=raw_txt.split(". ")
    return tokenize
#def tokens(sentence):
	#tokenize=sentence.split(" ")
        #return tokenize
f_in=open("space.txt",'r')
f_out=open("sentenceoutput.txt",'w')
#f_out1=open("output1.txt",'w')

context=f_in.read()
sentence=tokens_sentence(context)
print sentence
rec=0
pStart = 1 #adjust start value, if req'd 
pInterval = 1 #adjust interval value, if req'd
for item in sentence:
	#k = tokens(item)
	#for item1 in k:
	global rec
 #pStart = 1 #adjust start value, if req'd 
 #pInterval = 1 #adjust interval value, if req'd
 	if (rec == 0): 
   	   rec = pStart 
	else: 
             rec = rec + pInterval 
 #return rec       	
	#f_out1.write(item1+"\n")
	f_out.write(str(rec) +". "+ item+"\n")
f_out.close()
#f_out1.close()

def create_KB_sub_obj(tx):
	global KB
	global tg
	KB=[]
	
	
	KB_temp=['sub_obj','M_F_N','CAT','SG_PL','F_S_T']
	for i in range(len(tx)):
		KB_temp=['','','','','']
		if tg[i].startswith("N_"):
			KB_temp[2]="Noun"	
			if "_S_" in tg[i]:
				KB_temp[0]="Sub"
			elif "_O_" in tg[i]:
				KB_temp[0]="Obj"
			if tg[i].endswith("_M"):
				KB_temp[1]="M"			
			elif tg[i].endswith("_F"):
				KB_temp[1]="F"
			elif tg[i].endswith("_NU"):
				KB_temp[1]="NU"	
			elif "NNP" in tg[i]:
				KB_temp[2]="NNP"	
		elif tg[i].startswith("V_"):
			KB_temp[2]="Verb"
		elif tg[i].startswith("JJ"):
			KB_temp[2]="Adj"
		else:
			KB_temp[2]="Part"					
		KB.append(KB_temp)	
#	KB.remove(KB[0])
#	s=""
#	for i in range(len(KB)):
#		s=s+ KB[i]+"   "+tx[i]+"\n"		
	return KB
'''
read_in_file()
tnt_tagging()
in_file_tagging()
tx=create_KB_tag_lst()
create_KB_sub_obj(tx)
tokens_sentence(raw_txt)
'''
