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
dict ={'N_NNP_O_NU':'null','PR_PRP_':'null','N_NNP':'null','tagg':'null'}
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
		dict['tagg']=w[1]
		print "result" , dict['N_NNP_O_NU']
                f_out1.write(w[0]+' '+w[1]+' $')
                        #f_out1.write(w[1])
	elif str4.startswith("N_NNP"):
		dict['N_NNP']=w[0]
		dict['tagg']=w[1]
		print "result" , dict['N_NNP']
                f_out1.write(w[0]+' '+w[1]+' $')
                        #f_out1.write(w[1])
	elif str4.startswith("DM_DMD"):
		w[0]=dict['N_NNP']
		w[1]=dict['tagg']
		print "result" , w[0]
                f_out1.write(w[0]+' '+w[1]+' $')
                        #f_out1.write(w[1])
	elif str4.startswith("PR_PRP_"):
		w[0]=dict['N_NNP_O_NU']
		w[1]=dict['tagg']
		print "result" , w[0]
                f_out1.write(w[0]+' '+w[1]+' $')
                        #f_out1.write(w[1])
		
        else :
                f_out1.write(w[0]+' '+w[1]+' $')
                continue
                
#dict['JJ']=dict['N_NNP_O_NU']
#print "ressssssss" , dict['JJ']
#f_out = open('qwery.txt', 'w')
#f_out1.write(dict['JJ'])

        # else:
	#	continue	
         


