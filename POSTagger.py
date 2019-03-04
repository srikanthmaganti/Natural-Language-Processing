# -*- coding: utf-8 -*-
from decimal import Decimal
import string
def computelexicalandbigram(corpus,k):
	a,lexicalandbigram,flag=[],[],0
	text=corpus.split()
	for i in text:
		a.append(i.split('/'))
	lexicalandbigram=[]
	a.append(['$','$'])
	for mainindex,mainvalue in enumerate(a):
		
		if mainindex==len(a)-1:
			break
		lexical,tagbigram,weightcount,tagcount,tagbigramcount=a[mainindex][0],a[mainindex][1],0,0,0

		for checkindex,checkvalue in enumerate(a):
			if [lexical,tagbigram]==[a[checkindex][0],a[checkindex][1]]:
				weightcount=weightcount+1
			if tagbigram==a[checkindex][1]:
				tagcount=tagcount+1
			if mainindex>=1:
				if [a[mainindex-1][1],a[mainindex][1]]==[a[checkindex-1][1],a[checkindex][1]]:
					tagbigramcount=tagbigramcount+1
				

		if mainindex==0:
			lexicalandbigram.append([a[mainindex][0],'nothing',a[mainindex][1],round((float(weightcount)/tagcount),3),1.0])
		else:
			lexicalandbigram.append([a[mainindex][0],prevtag,a[mainindex][1],round((float(weightcount)/tagcount),3),round((float(tagbigramcount)/flag),5)])
		flag,prevtag=tagcount,a[mainindex][1]

	print("All the probability computations of corpus in the format [word(wi),previoustag(ti-1),currenttag(ti),p(wi/ti),p(ti/ti-1]")
	#print(lexicalandbigram)
	file = open("nlph.txt","w")
	for i in lexicalandbigram:
		# print(" P("+ i[0] + "/" +i[2]+")" + "="+str(i[3])+"        P("+i[2]+"/"+i[1]+")"+"="+str(i[4]))
		file.write(" P("+ i[0] + "/" +i[2]+")" + "="+str(i[3])+"        P("+i[2]+"/"+i[1]+")"+"="+str(i[4]) + "\n")
	li,checkli=[],[]
	giventext=k.split()
	for check,k in enumerate(giventext):
		li=[]
		for j in lexicalandbigram:

			if k==j[0] and j not in li: 
				#print(j,k)
				li.append(j)
		checkli.append(li)
	print("new strings")	
	print(checkli)
	f=[[]]
	for x in checkli:
		temp=[]
		for y in x:
			for z in f:
				temp.append(z+[y])
		f=temp

	print("all the permutted lists")
	print(len(temp))
	#Total no of permutted lists
	totalcount=[]
	for p in checkli:
		total=0
		for q in p:
			total=total+1
		totalcount.append(total)
	print("total no of permutted lists")
	print(totalcount)
	print("lists which do have tag matching")
	filteredli=[]
	for i in temp:
		count=0
		for j in range(1,len(i)):
			   if (i[j-1][2]==i[j][1]):
			   		#print("inside ")
			   		#print(i[j-1][2],i[j][1])

			   		count=count+1
			   else:
			   		break
		
		#print(count)
		if count==(len(i)-1):
			#print("inside print")
			filteredli.append(i)
	print("Most likely sequence of tags")
	print(len(filteredli))
	print("[word(wi),previoustag(ti-1),currenttag(ti),p(wi/ti),p(ti/ti-1]")
	print(filteredli)

	problist,reference,maxi=[],0,0
	for k,i in enumerate(filteredli):
		prob=1
		for j in range(len(i)):
			prob=prob*i[j][3]*i[j][4]
		if prob>maxi:
			maxi=prob
			reference=k
		#problist.append([prob,reference])
		#reference=reference+1
	print("\n list which do have maximum probability \n")
	print("[word(wi),previoustag(ti-1),currenttag(ti),p(wi/ti),p(ti/ti-1]\n")
	print(filteredli[reference])
	print("value of maximum probability")
	print(maxi)
if __name__ == "__main__":
	corpussentences="""
	 $/$ Chicago/NNP is/VBZ an/DT international/JJ hub/NN for/IN finance/NN ,/, commerce/NN ,/, industry/NN ,/, technology/NN ,/, telecommunications/NN ,/,
	 and/CC transportation/NN ./. $/$ It/PRP was/VBD the/DT site/NN of/IN the/DT creation/NN of/IN the/DT first/JJ standardized/JJ futures/NNS contracts/NNS at/IN 
	 the/DT Chicago/NNP Board/NNP of/IN Trade/NNP ,/, which/WDT today/NN is/VBZ the/DT largest/JJS and/CC most/RBS diverse/JJ derivatives/NNS market/NN in/IN the/DT world/NN ./. 
	 $/$ generating/VBG 20/CD %/NN of/IN all/DT volume/NN in/IN commodities/NNS and/CC financial/JJ futures/NNS ./. $/$ OHare/NNP International/NNP Airport/NNP is/VBZ the/DT
	 one/NN of/IN the/DT busiest/JJS airports/NNS in/IN the/DT world/NN ,/, and/CC the/DT region/NN also/RB has/VBZ the/DT largest/JJS number/NN of/IN U.S./NNP highways/NNS 
	 and/CC greatest/JJS amount/NN of/IN railroad/NN freight/NN ./.  $/$ In/IN 2012/CD ,/, Chicago/NNP was/VBD listed/VBN as/IN an/DT alpha/JJ global/JJ city/NN by/IN the/DT 
	 Globalization/NNP and/CC World/NNP Cities/NNPS Research/NNP Network/NNP ,/, and/CC it/PRP ranked/VBD seventh/JJ in/IN the/DT entire/JJ world/NN in/IN the/DT 
	 2017/NNP Global/NNP Cities/NNPS Index/NNP ./. $/$ Chicago/NNP has/VBZ one/CD of/IN the/DT highest/JJS gross/JJ metropolitan/JJ products/NNS in/IN the/DT world/NN 
	 generating/VBG over/RP 679.69/CD billion/CD in/IN 2017/CD ./. $/$ In/IN addition/NN ,/, it/PRP has/VBZ one/CD of/IN the/DT world/NNmost/JJS diversified/VBN 
	 and/CC balanced/VBN economies/NNS ,/, not/RB being/VBG dependent/JJ on/IN any/DT one/CD industry/NN ,/, with/IN no/DT single/JJ industry/NN employing/VBG more/JJR 
	 than/IN 14/CD %/NN of/IN the/DT workforce/NN ./. $/$ Chicago/NNP welcomed/VBD a/DT record/NN 58/CD million/CD domestic/JJ and/CC international/JJ visitors/NNS in/IN 2018/CD making/VBG it/PRP
  	 the/DT second/JJ most/RBS visited/JJ city/NN in/IN the/DT nation/NN after/IN New/NNP York/NNP ./. $/$ The/DT city/NN ranked/VBD first/JJ place/NN in/IN the/DT 
  	 2018/CD Time/NN Out/IN City/NNP Life/NNP Index/NNP ./. $/$ a/DT global/JJ quality/NN of/IN life/NN survey/NN of/IN 15,000/CD people/NNS in/IN 32/CD cities/NNS ./. 
  	 $/$ Landmarks/NNS in/IN the/DT city/NN include/VBP Millennium/NNP Park/NNP ,/, Navy/NNP Pier/NNP ./. $/$ the/DT Magnificent/NNP Mile/NNP ,/, Institute/NNP of/IN Chicago/NNP ,/, Museum/NNP Campus/NNP ,/, the/DT Willis/NNP -LRB-/-LRB- Sears/NNP -RRB-/-RRB- Tower/NN ,/, Grant/NNP Park/NNP -LRB-/-LRB- 
  	 Chicago/NNP -RRB-/-RRB- ,/, the/DT Museum/NN of/IN Science/NNP and/CC Industry/NNP ,/, and/CC Lincoln/NNP Park/NNP Zoo/NNP ./. $/$ Chicago/NNP 's/POS culture/NN 
  	 includes/VBZ the/DT visual/JJ arts/NNS ,/, literature/NN ,/, film/NN ,/, theater/NN ,/, comedy/NN ,/, food/NN ,/, and/CC music/NN ,/, particularly/RB jazz/NN ,/, 
  	 blues/NN ,/, soul/NN ,/, hiphop/NN ,/, gospel/NN and/CC electronic/JJ dance/NN music/NN including/VBG house/NN music/NN ./. """
	#k=s.translate(None,string.punctuation)
	corpus=corpussentences.lower()
	#print(corpus)
  	k='$ chicago has one of the largest and most diverse derivatives market in the world .'
  	Testsentence=k.lower()
  	computelexicalandbigram(corpus,Testsentence)
