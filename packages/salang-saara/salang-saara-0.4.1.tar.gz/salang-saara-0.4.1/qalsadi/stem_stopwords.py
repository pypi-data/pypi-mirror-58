﻿#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        stem_unknown
# Purpose:     Arabic lexical analyser, provides feature for stemming arabic word as unknown word
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
#-------------------------------------------------------------------------------

import arramooz.stopwordsdictionaryclass  as stopwordsdictionaryclass  
from . import wordCase

class stopWordStemmer:
	"""
        Arabic stopwords stemmer.
		get predifined stemming for stopwords
	"""
	def __init__(self, debug=False):
		# stopwords  dictionary
		self.swDictionary= stopwordsdictionaryclass.stopWordsDictionary('stopwords', stopwordsdictionaryclass.stopwords_DICTIONARY_INDEX);
		# use the word frequency dictionary as a dictionary for unkonwn words
		#word frequency dictionary
		self.debug=debug;
	def stemming_stopword(self, word):
		"""
		Analyze word morphologically as noun
		@param word: the input word.
		@type word: unicode.
		@return: list of dictionaries of analyzed words with tags.
		@rtype: list.
		"""	
		# the detailled stemmming result
		detailed_result=[];
		# search the sw in the dictionary
		# we can return the tashkeel
		#list of IDs of found stopwords in dictionary
		swIdList = [];
		# search in database by word, and return all ids
		#word = araby.stripTashkeel(word);
		swIdList = self.swDictionary.lookup(word);
		for sw_tuple in swIdList:
			# sw_tuple = self.swDictionary.getEntryById(id);
			detailed_result.append(wordCase.wordCase({
			'word':		word,
			'affix': (sw_tuple['procletic'],
								'',
								'',
								sw_tuple['encletic']),			
			'stem':			sw_tuple['stem'],
			'original':		sw_tuple['original'],
			'vocalized':	sw_tuple['vocalized'],
			'tags':			sw_tuple['tags'],
			'type':			sw_tuple['type'],
			'freq':'freqstopword',
			'originaltags':sw_tuple['tags'],
			'syntax':'',
			}));
		return detailed_result;

	def set_debug(self,debug):
		"""
		Set the debug attribute to allow printing internal analysis results.
		@param debug: the debug value.
		@type debug: True/False.
		"""
		self.debug=debug;
