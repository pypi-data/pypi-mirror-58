﻿#!/usr/bin/python

# -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------

# Name:        disambig_const.py
# Purpose:     Arabic lexical analyser constants used for disambiguation before analysis
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
from __future__ import print_function

# import  pyarabic.araby as araby
from . import disambig_const
import naftawayh.wordtag
class disambiguator:
	def __init__(self,):
		self.tagger = naftawayh.wordtag.WordTagger();

	def disambiguateWords(self, word_list, tag_list):
		"""
		Disambiguate some word according to tag guessing to reduce cases.
		return word list with dismbiguate.
		@param word_list: the given word lists.
		@type word_list: unicode list.
		@param tag_list: the given tag lists, produced by naftawayh
		@type tag_list: unicode list.		
		@return: a new word list
		@rtype: unicode list 
		"""
		# print u" ".join(word_list).encode('utf8');
		# print u" ".join(tag_list).encode('utf8');
	
		if len(word_list)==0 or len(word_list)!=len(tag_list):
			return word_list;
		else:
			newwordlist=[];
			wordtaglist=list(zip(word_list,tag_list));
			# print wordtaglist
			for i in range(len(wordtaglist)):
				currentWord=wordtaglist[i][0]; 
				if i+1<len(wordtaglist):
					nextTag=wordtaglist[i+1][1];
					# if the current exists in disambig table,
					# and the next is similar to the expected tag, return vocalized word form
					if self.isAmbiguous(currentWord):
						# test if expected tag is verb and 
						if self.tagger.isVerbTag(nextTag) and self.isDisambiguatedByNextVerb(currentWord) :
							currentWord = self.getDisambiguatedByNextVerb(currentWord);
						elif self.tagger.isNounTag(nextTag) and self.isDisambiguatedByNextNoun(currentWord)  :
							currentWord = self.getDisambiguatedByNextNoun(currentWord);
				newwordlist.append(currentWord);
			return newwordlist;

	def isAmbiguous(self, word):
		""" test if the word is an ambiguous case
		@param word: input word.
		@type word: unicode.
		@return : if word is ambiguous
		@rtype: True/False.
		"""
		return word in disambig_const.DISAMBIGUATATION_TABLE;

	def getDisambiguatedByNextNoun(self, word):
		""" get The disambiguated form of the word by the next word is noun.
		The disambiguated form can be fully or partially vocalized.
		@param word: input word.
		@type word: unicode.
		@return : if word is ambiguous
		@rtype: True/False.
		"""
		return disambig_const.DISAMBIGUATATION_TABLE.get(word, {}).get('noun', {}).get('vocalized', word);


	def getDisambiguatedByNextVerb(self, word):
		""" get The disambiguated form of the word by the next word is a verb.
		The disambiguated form can be fully or partially vocalized.
		@param word: input word.
		@type word: unicode.
		@return : if word is ambiguous
		@rtype: True/False.
		"""
		return disambig_const.DISAMBIGUATATION_TABLE.get(word, {}).get('verb', {}).get('vocalized', word);

	def isDisambiguatedByNextNoun(self, word):
		""" test if the word can be disambiguated if the next word is a noun
		@param word: input word.
		@type word: unicode.
		@return : if word has an disambiguated.
		@rtype: True/False.
		"""
		return 'noun' in disambig_const.DISAMBIGUATATION_TABLE.get(word, {});

	def isDisambiguatedByNextVerb(self, word):
		""" test if the word can be disambiguated if the next word is a verb
		@param word: input word.
		@type word: unicode.
		@return : if word has an disambiguated.
		@rtype: True/False.
		"""
		return 'verb' in disambig_const.DISAMBIGUATATION_TABLE.get(word, {});

		
	def disambiguateWordsOld(self, word_list, tag_list):
		"""
		Disambiguate some word according to tag guessing to reduce cases.
		return word list with dismbiguate.
		@param word_list: the given word lists.
		@type word_list: unicode list.
		@param tag_list: the given tag lists, produced by naftawayh
		@type tag_list: unicode list.		
		@return: a new word list
		@rtype: unicode list 
		"""
		# print u" ".join(word_list).encode('utf8');
		# print u" ".join(tag_list).encode('utf8');			
	
		if len(word_list)==0 or len(word_list)!=len(tag_list):
			return word_list;
		else:
			newwordlist=[];
			wordtaglist=zip(word_list,tag_list);
			# print wordtaglist
			for i in range(len(wordtaglist)):
				if i+1<=len(wordtaglist):
					# do tests with next word
					# إذا كانت الكلمة الحالية "أن" تكون "أنْ" حرف نصب إذا سبقت فعلا
					# وتكون أنّ، من أخوات إنّ إذا كان ما بعدها اسما
					if wordtaglist[i][0]==u'أن' and self.tagger.isVerbTag(wordtaglist[i+1][1]):
						# print' case1';
						wordtaglist[i]=(u'أَنْ','t');
					elif wordtaglist[i][0]==u'أن' and self.tagger.isNounTag(wordtaglist[i+1][1]):
						# print' case 2';
						wordtaglist[i]=(u'أَنَّ','t');
				newwordlist.append(wordtaglist[i][0]);
			return newwordlist;

if __name__ == "__main__":
	import sys
	sys.path.append('N:\googleapps\mishkal27-10-2012\lib');
	text = u"أن السلام مفيد أن يركبوا"
	# tokenize the text
	wordlist = text.split(' ');
	# create the disambiguator instance
	disamb = disambiguator();
	# tag the word list
	taglist = disamb.tagger.wordTagging(wordlist);
	newwordlist = disamb.disambiguateWords(wordlist, taglist);
	print(u" ".join(newwordlist).encode('utf8')); 



