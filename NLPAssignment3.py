# -*- coding: utf-8 -*-
import string
from gensim.models import KeyedVectors
from gensim.models import Word2Vec
#you can use the below one if we mention where the path of google is
model_1 = KeyedVectors.load_word2vec_format("C:/Users/srika/OneDrive/Desktop/Spring19/NLP/Assignments/Assignment3/GoogleNews-vectors-negative300.bin",binary=True)
#you can use the below one, if we place google corpus file in the same folder we run python file 
#model_1 = KeyedVectors.load_word2vec_format(’˜/GoogleNews-vectors-negative300.bin’,binary=True)

def similarity():
	#Chosen Words
	words = ['chair', 'mobile', 'school', 'numbers' , 'bottle']
	#Calculating similarity for each word
	for word in words:
		print("similar words for "+word)
		print model_1.wv.most_similar(word, topn=10)
		print("\n")
def antonyms():
	#Chosen Words 
	antonyms = ['ascend' , 'open' , 'arrive' , 'export' , 'come']
	#Calculating similarity for each word
	for antonym in antonyms:
		print("\n"+antonym)
		print model_1.wv.most_similar(antonym, topn=10)
def existing_analogies():
	#Given document
	docu="""Tokyo Japan London England
		Berlin Germany Madrid Spain
		Athens Greece Baghdad Iraq
		Chicago Illinois Houston Texas
		Chicago Illinois Portland Oregon
		Houston Texas Anchorage Alaska
		boy girl brother sister
		boy girl husband wife
		boy girl nephew niece
		boy girl policeman policewoman
		husband wife king queen
		husband wife man woman
		husband wife prince princess
		husband wife son daughter
		father mother groom bride
		father mother grandfather grandmother
		brother sister father mother
		USA dollar Europe euro
		USA dollar India rupee
		USA dollar Algeria dinar"""
		#splitting into lists
	k=docu.split("\n")
	#Throwing all the obtained lists into K1
	k1=[]
	#count for no of sentences for finding overall accuracy
	Total_no_of_sentences,count=0,0
	#iterating loop wise 
	for i in k:
		k1.append(i.split())
		Total_no_of_sentences=Total_no_of_sentences+1
	#list of semantic relationships
	print("list of all semantic relationships")
	print(k1)
	for p,q in enumerate(k1):
		v_a = model_1[k1[p][0]]
		v_b = model_1[k1[p][1]]
		v_c = model_1[k1[p][2]]
	#for finding analogy prediction by subtracting parallel vectors and addition of vector to form analogy
		v_new = v_b - v_a + v_c
		print("\n")
		#Analogy
		print(q)
		#Top 4 similar words for the analogy prediction
		#print model_1.wv.similar_by_vector(v_new, topn=4)
		#Top 4 similar words
		stereotype_word = model_1.wv.similar_by_vector(v_new, topn=4)
		print(stereotype_word)
		#excluding v_a,_b,v_c words from the top4 similar words 
		for stereotype in stereotype_word:
			if q[0] in list(stereotype):
				stereotype_word.remove(stereotype)
			if q[1] in list(stereotype):
				stereotype_word.remove(stereotype)
			if q[2] in list(stereotype):
				stereotype_word.remove(stereotype)
		#if the resultant word matched with 4th word in the given file in the given analogy
		#print as matched
		if q[3] in stereotype_word[0]:
			print("\n")
			print("Predicted Word is "+q[3]+" Matched")
			count=count+1
		#if not matched then give not matched
		else:
			print("Predicted Word is not matched")
	print("\n")
	#Showing the overall accuracy out of 20 words
	print("Overall Accuracy = "+str((float(count)/Total_no_of_sentences)*100))
	

		
def new_analogies():
	new_analogies="""Patna Bihar Hyderabad Telangana:
	India Delhi Colombia Bogota:
	Indonesia rupiah Czech koruna:
	husband wife patrolman patrolwoman:
	Edmonton Alberta Toronto Ontario"""
	k=new_analogies.split(":")
	#forming all the lists by appending
	k1=[]
	Total_no_of_sentences,count=0,0
	for i in k:
		k1.append(i.split())
		Total_no_of_sentences=Total_no_of_sentences+1
		#obtained list
	print("list of all semantic relationships")
	print(k1)
	for p,q in enumerate(k1):
		v_a_new = model_1[q[0]]
		v_b_new = model_1[q[1]]
		v_c_new = model_1[q[2]]
		#for finding analogy prediction by subtracting parallel vectors and addition of vector to form analogy
		v_new_analogy = v_b_new - v_a_new + v_c_new
		print("\n")
		#Analogy
		print(q)
		#Top 4 similar words for the analogy prediction
		#print model_1.wv.similar_by_vector(v_new_analogy, topn=4)
		stereotype_word = model_1.wv.similar_by_vector(v_new_analogy, topn=4)
		print(stereotype_word)
		#excluding v_a,_b,v_c words from the top4 similar words 
		for stereotype in stereotype_word:
			if q[0] in list(stereotype):
				stereotype_word.remove(stereotype)
			if q[1] in list(stereotype):
				stereotype_word.remove(stereotype)
			if q[2] in list(stereotype):
				stereotype_word.remove(stereotype)
		#if the resultant word matched with 4th word in the given file in the given analogy
		#print as matched
		if q[3] in stereotype_word[0]:
			print("\n")
			print("Predicted Word is "+q[3]+" Matched")
			count=count+1
		#if not matched then give not matched
		else:
			print("Predicted Word is not matched")
	print("\n")
	#Showing the overall accuracy out of 20 words
	print("Overall Accuracy = "+str((float(count)/Total_no_of_sentences)*100))

def train_new_embeddings():
		document="""Environmental pollution occurs when pollutants contaminate the natural surroundings. Pollution disturbs the balance of our ecosystems. 
		affect our normal lifestyles and gives rise to human illnesses and global warming. Pollution has reached its peak. due to the development and modernization in our lives. 
		With the development of science and technology.There has been a huge growth of human potentials. People have become prisoners of their own creations.
		We waste the bounties of our nature.thought that our actions cause serious problems. We must deepen our knowledge of nature laws and broaden.
		our understanding of the laws of the human behavior.in order to deal with pollution problems.it is very important to know different types of pollutions. 
		their effects.That causes on humanity and the environment.we live in.Air pollution is one of the most dangerous forms of pollution. 
		A biological, chemical, and physical alteration of the air.when smoke, dust, and any harmful gases enter into the atmosphere. 
		make it difficult for all living beings.To survive as the air becomes contaminated. Burning of fossil fuels, agriculture related activities.
		mining operations, exhaust from industries.household cleaning products entail air pollution.People release a huge amount of chemical substances in the air every day. 
		The effects of air pollution are alarming. It causes global warming, acid rains, respiratory and heart problems, and eutrophication. 
		A lot of wildlife species are forced to change their habitat.in order to survive.Soil pollution occurs when the presence of pollutants, contaminants, and toxic chemicals in the soil.
		is in high concentration that has negative effect on wildlife, plants, humans, and ground water.accidental oil spill are the main causes of soil pollution. 
		This type of contamination influence health of humans.Affects the growth of plants. Decreases soil fertility, and changes the soil structure.
		Water pollution is able to lead our world on a path of destruction. Water is one of the greatest natural resources of the whole humanity. 
		Nothing will be able to live without water. However, we do not appreciate this gift of nature. Pollute it without thinking. The key causes of the water pollution.
		industrial waste, mining activities, sewage and waste water, accidental oil leakage, marine dumping, chemical pesticides and fertilizers, burning of fossil fuels, animal waste.
		urban development, global warming, radioactive waste. others are leakage from sewer lines. There is less water available for drinking, cooking, irrigating crops, and washing.
		Light pollution occurs because of the prominent excess illumination in some areas. Artificial lights disrupt the world`s ecosystems. 
		They have deadly effects on many creatures including mammals, plants, amphibians, insects, and birds. Every year many bird species die colliding with needlessly illuminated buildings.
		over, artificial lights can lead baby sea turtles to their demise.Noise pollution takes place when noise and unpleasant sounds cause temporary disruption in the natural balance. 
		It is usually caused by industrialization, social events, poor urban planning, household chores.All these cause a lot of impact.Noise pollution leads to hearing problems.
		health issues, cardiovascular issues, sleeping disorders, and trouble communicating. Moreover, it affects wildlife a lot.which leads to death of creatures. 
		Some animals may suffer from hearing loss. while others become inefficient at hunting. It is very important to understand noise pollution.
		In order to lower its impact on the environment.Radioactive pollution is the presence of radioactive substances in the environment. It is highly dangerous when it occurs.
		Radioactive contamination can be caused by breaches. at nuclear power plants or improper transport of radioactive chemicals. 
		Radioactive material should be handled with great care as radiation destroys cells in living organisms that can result in illness or even death.
		Environmental pollution has negatively affected the life of both animals and human-beings. The only way to control current environmental issues is to implement conservation methods.
		and create sustainable development strategies. We should find some effective solutions in order to restore our ecological balance.
		we should make sustainable transportation choices. We should take advantage of public transportation.
		walk or ride bikes whenever possible, consolidate our trips, and consider purchasing an electric car. It is very important to make sustainable food choices. 
		Choose local food whenever possible; buy organically grown vegetables and fruits or grow your own.People should conserve energy. 
		Turn off electronics and lights when you are not in the room. Consider what small changes can lead to big energy savings. Use energy efficient devices. 
		It is also essential to understand the concept of reduce, Reuse and Recycle. Try to buy used items whenever possible. Choose products with minimal packaging. 
		Buy reusable items. Remember that almost everything that you purchase can be recycled.Conserve water as much as possible. 
		Dispose of toxic waste properly. Do not use herbicides and pesticides. Use natural.
		environmentally friendly chemicals for your everyday chores.Environmental pollution is one of the biggest problems caused by human activities.
		that we should overcome to see a tomorrow and guarantee our descendants a healthy life.  There are many environmental concerns for communities around the world to address. 
		We should always remember that pollution problems affect us all so each of us has to do his or her best to help restore ecological balance to this beautiful place we call home.
		Learn about the major polluters in your area to protect the air and water where you live. Encourage people to stop pollution. tell them everything you know about this problem. 
		and protest local polluters together. The masses should be educated on the danger of different types of pollution.
		People should know everything about all consequences of the environmental pollution in order to prevent the worst from happening. 
		Let`s protect the water we drink, the air we breathe, and the soil we use to grow our food."""
		#converting sentences to lists
		documenttosentences=document.split('.')
		sentences=[]
		#removing all the punctuations from corpus
		punctuations = """!()-[]{};:'",<>./?@#$%^&*_~"""
		for i in documenttosentences:
			i=i.lower()
			no_punct = ""
			for char in i:
				if char not in punctuations:
					no_punct=no_punct+char
				#appending sentences
			sentences.append(no_punct.split())


		#print(documenttosentences)
		#wordtovector
		model_2 = Word2Vec(size=50, min_count=1)
		#building vocabulary
		model_2.build_vocab(sentences)
		#training the model sentences
		model_2.train(sentences, total_examples=model_2.corpus_count, epochs=200)
		#sample words to calculate
		b_i=['take','care','able','ride','learn']
		#calculating similar words for each word through model 2
		for k in b_i:
			print("\n"+k)
			print model_2.most_similar(k,topn=10)
			print('\n')
		#calculating similar words for each word through model 1
		for word in b_i:
			print("similar words through model1 "+word)
			print model_1.wv.most_similar(word, topn=10)
			print("\n")

if __name__=="__main__":
	 #similarity()
	 #antonyms()
	 #existing_analogies()
	 #new_analogies()
	 train_new_embeddings()