 # -*- coding: utf-8 -*-
import string
def test(s):
	sentence=s.split()
	a=[]
	count=0
	for k in sentence:
		count=count+1
		if k not in a:
			a.append(k)
	modified=[]
	for p in a:
		modified.append([p,0])
	print("modified")
	print(modified)
	print("distinct words")
	print(a)
	print("total words")
	print(count)
	vocabcount=0
	for j in modified:
		vocabcount=vocabcount+1
	print("Vocabulary count")
	print(vocabcount)
	for i in sentence:
		for j in modified:
			
			if i==j[0]:
				j[1]=j[1]+1
	print("vocabulary")
	print(modified)



	

if __name__ == "__main__":
	
	#s="my name is srikanth srikanth maganti"
	#test(s)
  	s='Though a large swath of the nation is in the midst of an arctic chill, Chicago may be bearing the brunt of it. That low broken the previous days record set in 1966 of minus 15. Because of these ridiculously low temperature in chicago is experiencing another bizarre natural phenomenon: frost quakes.According to CNN, residents of Chicago were stirred awake on Wednesday by large booming sounds. By which, CNN explained, were likely an event known as cryoseism, or a "frost quake."'
  	k=s.translate(None,string.punctuation)
  	modifiedtext=k.lower()
  	test(modifiedtext)
  	#print(modifiedtext)