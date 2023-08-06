#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        analex
# Purpose:     Arabic lexical analyser, provides feature to stem arabic words as noun, verb, stopword 
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
from __future__ import print_function

if __name__=="__main__":
	import sys
	sys.path.append('..');

import re
import pyarabic.araby as araby  # basic arabic text functions
from . import analex_const # special constant for analex
from . import stem_noun		# noun stemming
from . import stem_verb		# verb stemming
from . import stem_unknown		# unknown word stemming
from . import stem_stopwords		# stopwords word stemming
from . import stem_pounct_const # pounctaution constants
import naftawayh.wordtag  # word tagger
import arramooz.wordfreqdictionaryclass as wordfreqdictionaryclass
from . import disambig  # disambiguation const
from . import wordCase
from . import stemmedword# the result object for stemming
from . import cache

class analex :
	"""
		Arabic text morphological analyzer.
		Provides routins  to alanyze text.
		Can treat text as verbs or as nouns.
	"""


	def __init__(self,  allowTagGuessing  =True, allowDisambiguation=True):
		"""
		Create Analex instance.
		"""

		self.nounstemmer=stem_noun.nounStemmer(); # to stem nouns
		self.verbstemmer=stem_verb.verbStemmer(); # to stem verbs
		self.unknownstemmer=stem_unknown.unknownStemmer(); # to stem unknown
		self.stopwordsstemmer=stem_stopwords.stopWordStemmer(); # to stem stopwords
		
		self.allowTagGuessing =allowTagGuessing # allow gueesing tags by naftawayh before analyis
		# if taggin is disabled, the disambiguation is also disabled
		self.allowDisambiguation = allowDisambiguation and allowTagGuessing # allow disambiguation before analyis
		# enable the last mark (Harakat Al-I3rab) 
		self.allowSyntaxLastMark =True; 
		if self.allowTagGuessing :
			self.tagger=naftawayh.wordtag.WordTagger();
		if self.allowDisambiguation: 
			self.disambiguator=disambig.disambiguator();
		self.debug=False; # to allow to print internal data
		self.limit=10000; # limit words in the text
		self.wordcounter=0;
		# the words contain arabic letters and harakat.
		# the unicode considers arabic harakats as marks not letters,
		# then we add harakat to the regluar expression to tokenize
		marks=u"".join(araby.TASHKEEL)# contains [FATHA,DAMMA,KASRA,SUKUN,DAMMATAN,KASRATAN,FATHATAN,SHADDA])
		# used to tokenize arabic text
		self.token_pat=re.compile(u"([\w%s]+)"%marks,re.UNICODE);				
		#used to split text into clauses
		self.Clause_pattern=re.compile(u"([\w%s\s]+)"%(u"".join(araby.TASHKEEL),),re.UNICODE);

		# allow partial vocalization support, 
		#~The text is analyzed as partial or fully vocalized.
		self.partial_vocalization_support=True;
		
		#word frequency dictionary
		self.wordfreq= wordfreqdictionaryclass.wordfreqDictionary('wordfreq', wordfreqdictionaryclass.wordfreq_DICTIONARY_INDEX);
		
		# added to avoid duplicated search in the word frequency database
		# used as cache to reduce database access
		#added as a global variable to avoid duplucated search in mutliple call of analex
		# cache used to avoid duplicata
		self.allowCacheUse =False;
		if self.allowCacheUse:
			self.cache = cache.cache()


	def __del__(self):
		"""
		Delete instance and clear cache
		"""
		self.wordfreq=None;
		self.nounstemmer=None
		self.verbstemmer=None
		self.unknownstemmer=None
		self.stopwordsstemmer=None
		self.tagger=None
		self.disambiguator=None
		
	def text_treat(self,text):
		""" deprecated: treat text to eliminate pountuation.
		@param text: input text;
		@type text: unicode;
		@return : treated text.
		@rtype: unicode.
		"""
		return text;

	def count_word(self, word):
		""" count input words.
		Used just for profiling and tests.
		@param word: input word;
		@type word: unicode;
		@return : counter.
		@rtype: integer.
		"""
		self.wordcounter+=1;	
		return self.wordcounter;

	def tokenize(self,text=u""):
		"""
		Tokenize text into words
		@param text: the input text.
		@type text: unicode.
		@return: list of words.
		@rtype: list.
		"""
		if text==u'':
			return [];
		else:
			mylist = self.token_pat.split(text)
			mylist = [re.sub("\s",'',x) for x in mylist if x]
			# for i in range(len(mylist)):
				# mylist[i]=re.sub("\s",'',mylist[i]);
			# while u'' in mylist: mylist.remove(u'');
			# remove empty substring
			mylist = [x for x in mylist if x]
			#print u"'".join(mylist).encode('utf8');
			return mylist;


	def splitIntoPhrases(self, text):
		"""
		Split Text into clauses
		@param text: input text;
		@type text: unicode;
		@return: list of clauses
		@rtype: list of unicode
		"""
		if text:
			list_phrase = self.Clause_pattern.split(text);
			if list_phrase:
				j=-1;
				newlist=[];
				for ph in list_phrase:
					if not self.Clause_pattern.match(ph):
						#is pounctuation or symboles
						#print 'not match', ph.encode('utf8');
						if j<0:
							# the symbols are in the begining
							newlist.append(ph);
							j=0;
						else:
							# the symbols are after a phrases
							newlist[j]+=ph;
					else:
						newlist.append(ph);
						j+=1;
				return newlist;
			else: return [];
		return [];

	def text_tokenize(self,text):
		"""
		Tokenize text into words, after treatement.
		@param text: the input text.
		@type text: unicode.
		@return: list of words.
		@rtype: list.
		"""	
		text=self.text_treat(text);
		list_word=self.tokenize(text);
		return list_word;

	def set_debug(self,debug):
		"""
		Set the debug attribute to allow printing internal analysis results.
		@param debug: the debug value.
		@type debug: True/False.
		"""
		self.debug=debug;
		self.nounstemmer.set_debug(debug); # to set debug on noun stemming
		self.verbstemmer.set_debug(debug); # to set debug on verb stemming

	def enableAllowSyntaxLastMark(self):
		"""
		Enable the syntaxic last mark attribute to allow use of I'rab harakat.
		"""
		self.allowSyntaxLastMark=True;
		self.nounstemmer.enableAllowSyntaxLastMark(); # to allow syntax last mark on noun stemming
		self.verbstemmer.enableAllowSyntaxLastMark(); # to allow syntax last mark  on verb stemming

	def disableAllowSyntaxLastMark(self):
		"""
		Disable the syntaxic last mark attribute to allow use of I'rab harakat.
		"""
		self.allowSyntaxLastMark=False;
		self.nounstemmer.disableAllowSyntaxLastMark(); # to allow syntax last mark on noun stemming
		self.verbstemmer.disableAllowSyntaxLastMark(); # to allow syntax last mark  on verb stemming

	def set_limit(self,limit):
		"""
		Set the number of word treated in text.
		@param limit: the word number limit.
		@type limit: integer.
		"""
		self.limit=limit;

	def enableAllowCacheUse(self):
		"""
		Allow the analex to use Cache to reduce calcul.
		"""
		self.allowCacheUse=True;

	def disableAllowCacheUse(self):
		"""
		Not allow the analex to use Cache to reduce calcul.
		"""
		self.allowCacheUse=False;

	def check_text(self,text, mode='all'):
		"""
		Analyze text morphologically.
The analyzed data given by morphological analyzer Qalsadi have the following format:
				"<th>المدخل</th>", "<th>تشكيل</th>","<th>الأصل</th>","<th>السابقة</th>", "<th>الجذع</th>",
				"<th>اللاحقة</th>", "<th>الحالة الإعرابية</th>","<th>الجذر</th>", "<th>النوع</th><th>شيوع</th>",
				"</tr>"
		morphological Result is a list of list of dict.
		The list contains all possible morphological analysis as a dict
		[
		[
		 {
			"word": "الحياة",		# input word
			"vocalized": "الْحَيَاةُ",   # vocalized form of the input word 
			"procletic": "ال",		# the syntaxic pprefix called procletic
			"prefix": "",			# the conjugation or inflection prefix
			"stem": "حياة",			# the word stem
			"suffix": "ُ", 			# the conjugation suffix of the word
			"encletic": "",			# the syntaxic suffix
			
			"tags": "تعريف::مرفوع*", # tags of affixes and tags extracted form lexical dictionary

			"freq": 0,				# the word frequency from Word Frequency database 
			"root": "",				# the word root; not yet used
			"template": "",			# the template وزن 
			"type": "Noun:مصدر",	# the word type
			"original": "حَيَاةٌ"		#original word from lexical dictionary
			"syntax":""				# used for syntaxique analysis porpos
			},
		 {"vocalized": "الْحَيَاةِ", "suffix": "ِ", "tags": "تعريف::مجرور", "stem": "حياة", "prefix": "", "freq": 0, "encletic": "", "word": "الحياة", "procletic": "ال", "root": "", "template": "", "type": "Noun:مصدر", "original": "حَيَاةٌ", "syntax":""}, 
		 {"vocalized": "الْحَيَاةَ", "suffix": "َ", "tags": "تعريف::منصوب", "stem": "حياة", "prefix": "", "freq": 0, "encletic": "", "word": "الحياة", "procletic": "ال", "root": "", "template": "", "type": "Noun:مصدر", "original": "حَيَاةٌ", "syntax":""}
		],
		[ 
		 {"vocalized": "جَمِيلَةُ", "suffix": "َةُ", "tags": "::مؤنث:مرفوع:ممنوع من الصرف", "stem": "جميل", "prefix": "", "freq": 63140, "encletic": "", "word": "جميلة", "procletic": "", "root": "", "template": "", "type": "Noun:صيغة مبالغة", "original": "جَمِيلٌ", "syntax":""}, 
		 {"vocalized": "جَمِيلَةِ", "suffix": "َةِ", "tags": "::مؤنث:مجرور:ممنوع من الصرف", "stem": "جميل", "prefix": "", "freq": 63140, "encletic": "", "word": "جميلة", "procletic": "", "root": "", "template": "", "type": "Noun:صيغة مبالغة", "original": "جَمِيلٌ"}, {"vocalized": "جَمِيلَةَ", "suffix": "َةَ", "tags": "::مؤنث:منصوب:ممنوع من الصرف", "stem": "جميل", "prefix": "", "freq": 63140, "encletic": "", "word": "جميلة", "procletic": "", "root": "", "template": "", "type": "Noun:صيغة مبالغة", "original": "جَمِيلٌ", "syntax":""}
		]
		],
		@param text: the input text.
		@type text: unicode.
		@param mode: the mode of analysis as 'verbs', 'nouns', or 'all'.
		@type mode: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""
		list_word=self.text_tokenize(text);
		if self.allowTagGuessing :
			list_guessed_tag = self.tagger.wordTagging(list_word);
			# avoid errors
			if len(list_guessed_tag)!=len(list_word):
				#if the two lists have'nt the same length, 
				# we construct a empty list for tags with the same length
				# print "error on guess tags"
				# sys.exit();
				list_guessed_tag=['nv']*len(list_word);
		# disambiguate  some words to speed up the analysis
		# newWordlist = self.disambiguator.disambiguateWords( list_word, list_guessed_tag);
		if self.allowDisambiguation :		
			newWordlist = self.disambiguator.disambiguateWords( list_word, list_guessed_tag);
			# avoid the incomplete list
			if len(newWordlist)==len(list_word):
				list_word = newWordlist;
				# print u" ".join(list_word).encode('utf8');
				# print u" ".join(list_guessed_tag).encode('utf8');			

		resulted_text=u""
		resulted_data=[];
		#checkedWords={}; #global
		if mode=='all':
			for i in range(len(list_word[:self.limit])):
				word = list_word[i];
				self.count_word(word);
				#~ if self.allowCacheUse and word in self.cache['checkedWords']: #.has_key(word):
				if self.allowCacheUse and self.cache.isAlreadyChecked(word):
					#~ print (u"'%s'"%word).encode('utf8'), 'found'
					one_data_list = self.cache.getChecked(word)
					Stemmed_one_data_list = [ stemmedword.stemmedWord(w) for w in one_data_list ]
					resulted_data.append(Stemmed_one_data_list);
				else:
					guessedTag    = list_guessed_tag[i];	
					#~ print (u"'%s'"%word).encode('utf8'), ' not'			
					one_data_list = self.check_word(word, guessedTag);
					Stemmed_one_data_list = [stemmedword.stemmedWord(w) for w in one_data_list ]
					resulted_data.append(Stemmed_one_data_list);

					#~ resulted_data.append(one_data_list);
					#~ if self.allowCacheUse: self.cache['checkedWords'][word]=one_data_list;
					one_data_list_to_serialize = [w.__dict__ for w in one_data_list]
					if self.allowCacheUse:
						self.cache.addChecked(word, one_data_list_to_serialize);

		elif mode=='nouns':
		
			for word in list_word[:self.limit] :
				one_data_list=self.check_word_as_noun(word);
				Stemmed_one_data_list = [ stemmedword.stemmedWord(w) for w in one_data_list ]
				resulted_data.append(Stemmed_one_data_list);
				#~ resulted_data.append(one_data_list);
		elif mode=='verbs':
			for word in list_word[:self.limit] :
				one_data_list=self.check_word_as_verb(word);
				Stemmed_one_data_list = [stemmedword.stemmedWord(w) for w in one_data_list ]
				resulted_data.append(Stemmed_one_data_list);				
				#~ resulted_data.append(one_data_list);
		return resulted_data;


	def check_word(self,word, guessedTag=""):
		"""
		Analyze one word morphologically as verbs
		@param word: the input word.
		@type word: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""	
		word=araby.stripTatweel(word);
		word_vocalised=word;
		word_nm=araby.stripTashkeel(word);
		resulted_text=u"";
		resulted_data=[];
		# if word is a pounctuation
		resulted_data+=self.check_word_as_pounct(word_nm);
		# Done: if the word is a stop word we have  some problems,
		# the stop word can also be another normal word (verb or noun),
		# we must consider it in future works
		# if word is stopword allow stop words analysis
		resulted_data+=self.check_word_as_stopword(word_nm);

		#if word is verb
		# مشكلة بعض الكلمات المستبعدة تعتبر أفعلا أو اسماء
		if  self.tagger.hasVerbTag(guessedTag) or self.tagger.isStopWordTag(guessedTag):
			resulted_data+=self.check_word_as_verb(word_nm);
			#print "is verb", rabti,len(resulted_data);
		#if word is noun
		if self.tagger.hasNounTag(guessedTag) or self.tagger.isStopWordTag(guessedTag):			
			resulted_data+=self.check_word_as_noun(word_nm);
		if len(resulted_data)==0:
			#check the word as unkonwn
			resulted_data+=self.check_word_as_unknown(word_nm);
			#check if the word is nomralized and solution are equivalent
		resulted_data = self.check_normalized(word_vocalised, resulted_data)
		#check if the word is shadda like
		resulted_data = self.check_shadda(word_vocalised, resulted_data)

		#check if the word is vocalized like results			
		if self.partial_vocalization_support:
			resulted_data=self.check_partial_vocalized(word_vocalised, resulted_data);
		# add word frequency information in tags
		resulted_data = self.addWordFrequency(resulted_data);

		if len(resulted_data)==0:
			resulted_data.append(wordCase.wordCase({
			'word':word,  
			'affix': ('' , '', '', ''),       
			'stem':'',
			'original':word,
			'vocalized':word,
			'tags':u'',
			'type':'unknown',
			'root':'',
			'template':'',
			'freq':self.wordfreq.getFreq(word, 'unknown'),
			'syntax':'',
			})
			);
		return resulted_data;

	def check_text_as_nouns(self,text):
		"""
		Analyze text morphologically as nouns
		@param text: the input text.
		@type text: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""
		return self.check_text(text,"nouns");


	def check_text_as_verbs(self,text):
		"""
		Analyze text morphologically as verbs
		@param text: the input text.
		@type text: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""	
		return self.check_text(text,"verbs");




	def check_normalized(self, word_vocalised, resulted_data):
		"""
		If the entred word is like the found word in dictionary, to treat some normalized cases, 
		the analyzer return the vocalized like words;
		ُIf the word is ذئب, the normalized form is ذءب, which can give from dictionary ذئبـ ذؤب.
		this function filter normalized resulted word according the given word, and give ذئب.
		@param word_vocalised: the input word.
		@type word_vocalised: unicode.
		@param resulted_data: the founded resulat from dictionary.
		@type resulted_data: list of dict.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""
		#print word_vocalised.encode('utf8');
		filtred_data=[];
		inputword = araby.stripTashkeel(word_vocalised)
		for item in  resulted_data:
			vocalized = getattr(item, 'vocalized') 
			if vocalized:
				outputword = araby.stripTashkeel(vocalized)
				if inputword == outputword:
					filtred_data.append(item);
		return  filtred_data;



	def check_shadda(self, word_vocalised,resulted_data):
		"""
		if the entred word is like the found word in dictionary, to treat some normalized cases, 
		the analyzer return the vocalized like words.
		This function treat the Shadda case.
		@param word_vocalised: the input word.
		@type word_vocalised: unicode.
		@param resulted_data: the founded resulat from dictionary.
		@type resulted_data: list of dict.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""
		return [x for x in resulted_data if araby.shaddalike(word_vocalised, getattr(x, 'vocalized', ''))]


	def check_partial_vocalized(self, word_vocalised,resulted_data):
		"""
		if the entred word is vocalized fully or partially, 
		the analyzer return the vocalized like words;
		This function treat the partial vocalized case.
		@param word_vocalised: the input word.
		@type word_vocalised: unicode.
		@param resulted_data: the founded resulat from dictionary.
		@type resulted_data: list of dict.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.		
		"""
		#print word_vocalised.encode('utf8');
		filtred_data=[];
		if not araby.isVocalized(word_vocalised):
			return resulted_data;
		else:
			#compare the vocalized output with the vocalized input
			#print ' is vocalized';
			for item in  resulted_data:
				if 'vocalized' in item and araby.vocalizedlike(word_vocalised,item['vocalized']):
					item['tags']+=':'+analex_const.partialVocalizedTag;
					filtred_data.append(item);
			return  filtred_data;

	def test25(self):
		return 100;
	def addWordFrequency(self, resulted_data):
		"""
		If the entred word is like the found word in dictionary, to treat some normalized cases, 
		the analyzer return the vocalized like words;
		ُIf the word is ذئب, the normalized form is ذءب, which can give from dictionary ذئبـ ذؤب.
		this function filter normalized resulted word according the given word, and give ذئب.
		@param word_vocalised: the input word.
		@type word_vocalised: unicode.
		@param resulted_data: the founded resulat from dictionary.
		@type resulted_data: list of dict.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""
		# added to avoid duplicated search in the word frequency database
		# used as cache to reduce database access
		#added as a global variable to avoid duplucated search in mutliple call of analex
		#checkedFreqWords={'noun':{}, 'verb':{}}; # global
		for i in  range(len(resulted_data)):  
			# get the original word of dictionary,
			item=resulted_data[i]
			# search for the original (lexique entry)
			original = getattr(item, 'original', '')

			# in the freq attribute we found 'freqverb, or freqnoun, or a frequency for stopwords or unkown
			# the freqtype is used to note the wordtype,
			# this type is passed by stem_noun ,or stem_verb modules
			freqtype=getattr(item, 'freq', ''); 
			if freqtype=='freqverb':    
				wordtype='verb';
			elif freqtype=='freqnoun':
				wordtype='noun';
			elif freqtype=='freqstopword':
				wordtype='stopword';
			else: 
				wordtype='';
			if wordtype:
				# if frequency is already get from database, don't access to database
				if self.allowCacheUse: 
					setattr(item, 'freq', self.cache.getFreq(original, wordtype)) 
				else:
					freq=self.wordfreq.getFreq(original, wordtype);
					# just used to count funtion calls
					self.test25();
					#store the freq in the cache
					if self.allowCacheUse:
						self.cache.addFreq(original, wordtype, freq);

					setattr(item, 'freq', freq)
			resulted_data[i]=item;
		return  resulted_data;

	def check_word_as_stopword(self,word):
		"""
		Check if the word is a stopword, 
		@param word: the input word.
		@type word: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.		
		"""	
		return self.stopwordsstemmer.stemming_stopword(word);


	def check_word_as_pounct(self,word):
		"""
		Check if the word is a pounctuation, 
		@param word: the input word.
		@type word: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.		
		"""		
		detailed_result=[]
		# ToDo : fix it to isdigit, by moatz saad
		if word.isnumeric():
			detailed_result.append(wordCase.wordCase({
			'word':word,
			'affix': ('', '', '', ''),			
			'stem':'',
			'original':word,
			'vocalized':word,
			'tags':self.get_number_tags(word),
			'type':'NUMBER',
			'freq':0,
			'syntax':'',			
			}));	
		if word in stem_pounct_const.POUNCTUATION:
			detailed_result.append(wordCase.wordCase({
			'word':word,
			'affix': ('', '', '', ''),
			'stem':'',
			'original':word,
			'vocalized':word,
			'tags':stem_pounct_const.POUNCTUATION[word]['tags'],
			'type':'POUNCT',
			'freq':0,
			'syntax':'',			
			}));

		return detailed_result;


	def check_word_as_verb(self,verb):
		"""
		Analyze the word as verb.
		@param verb: the input word.
		@type verb: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.		
		"""	
		return self.verbstemmer.stemming_verb(verb)


	def check_word_as_noun(self,noun):
		"""
		Analyze the word as noun.
		@param noun: the input word.
		@type noun: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""
		return self.nounstemmer.stemming_noun(noun);


	def check_word_as_unknown(self,noun):
		"""
		Analyze the word as unknown.
		@param noun: the input word.
		@type noun: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""
		return self.unknownstemmer.stemming_noun(noun)

	def context_analyze(self,result):
		"""
		Deprecated: Analyze the context.
		@param result: analysis result.
		@type result: list of dict.
		@return: filtred relust according to context.
		@rtype: list.
		"""	
		return result;

	def get_number_tags(self, word):
		"""
		Check the numbers and return tags.
		@param word: the input word.
		@type word: unicode.
		@return: tags.
		@rtype: text.
		"""	
		return u"عدد";

def mainly():
	print("test");		
	analyzer=analex();
	analyzer.disableAllowCacheUse()
	# text=u"""تجف أرض السلام بالسلام الكبير.	مشى على كتاب السلام.
	# جاء الولد السمين من قاعة القسم الممتلئ""";
	for i in range(2):
		text=u"يعبد الله تطلع الشمس"
		voc = analyzer.check_text(text);
		# voc = analyzer.check_text(text);		
		print(voc);#.encode('utf8');
	
if __name__=="__main__":
	mainly();
