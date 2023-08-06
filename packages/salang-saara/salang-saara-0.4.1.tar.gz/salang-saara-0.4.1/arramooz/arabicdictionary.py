﻿#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Arabic Dictionary from Arramooz Al Waseet
# Purpose:     Morphological porpus Dictionary.
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     16-12-2013
# Copyright:   (c) Taha Zerrouki 2013
# Licence:     GPL
#-------------------------------------------------------------------------------
"""
Arabic Dictionary Class from Arramooz Al Waseet.
Used in multiporpus morpholigical treatment
"""
from __future__ import print_function

import re
import os, os.path
#from pysqlite2 import dbapi2 as sqlite
import sqlite3 as sqlite
import sys
FILE_DB=u"data/arabicdictionary.sqlite"
import pyarabic.araby as araby
class arabicDictionary:
	"""
	Arabic dictionary Class
	Used to allow abstract acces to lexicon of arabic language,
	can get indexed and hashed entries from the  basic lexicon
	add also, support to extract attributtes from entries
	"""

	def __init__(self, tableName):
		"""
		initialisation of dictionary from a data dictionary, create indexes to speed up the access.

		"""
		# load data from the brut dictionary into a new dictionary with numeric ids
		self.dictionary={};
		# self.attribIndex=attribIndex;
		# self.keyAttribute= keyAttribute;
		self.attribNumIndex={};
		# create the attribute num index
		# attribIndex: 		attribNumIndex
		# vocalized: 0		0: vocalized
		#unvocalized: 1		1: unvocalized
		#
		# for k in self.attribIndex.keys():
			# v=self.attribIndex[k];
			# self.attribNumIndex[v]=k;
		self.tableName=tableName;

		# get the database path
		if hasattr(sys,'frozen'): # only when running in py2exe this exists
			base = sys.prefix
		else: # otherwise this is a regular python script
			base = os.path.dirname(os.path.realpath(__file__))
		file_path=os.path.join(base,FILE_DB);

		if os.path.exists(file_path):
			try:
				# self.dbConnect = sqlite.connect("file:%s?mode=ro"%file_path, uri=True)
				self.dbConnect = sqlite.connect(file_path)				
				self.dbConnect.row_factory = sqlite.Row 
				self.cursor = self.dbConnect.cursor()
			except:
				print("Fatal Error Can't find the database file", file_path)
		else:
			print(u" ".join(["Inexistant File", file_path, " current dir ", os.curdir]).encode('utf8'));
		#create index  by word stampfor dictionary to accelerate word search.
		# the word stamp is the arabic word without any affixation  letters, for example
		# the word مضرب give ضر, by removing meem and beh, the word ضرم give ضر. the stamp is used as a first level of indexing,especially
		# for verbs
		# the stamp pattern is used to create the word stamp
		self.STAMP_pat=re.compile(u"[%s%s%s%s%s%s%s%s%s]"%(araby.ALEF, araby.YEH, araby.HAMZA,  araby.ALEF_HAMZA_ABOVE, araby.WAW_HAMZA,  araby.YEH_HAMZA,   araby.WAW,  araby.ALEF_MAKSURA, araby.SHADDA),re.UNICODE)

	def __del__(self):
		"""
		Delete instance and close database connection
		
		"""
		if self.dbConnect:
			self.dbConnect.close();


	def getEntryById(self,id):
		""" Get dictionary entry by id from the dictionary
		@param id :word identifier
		@type id: integer
		@return: all attributes
		@rtype: dict
		"""
		# if the id exists and the attribute existe return the value, else return False
		# The keys in the dictinary are numeric, for comression reason,
		# then we use text keys in output, according to the self.attribNumIndex
		# eg.
		# entry ={0:"kataba", 1:"ktb"}
		# output entry ={'vocalized':'kataba', 'unvocalized':'ktb'}
		sql = u"select * FROM %s WHERE id='%s'"%(self.tableName,id);
		try:
			self.cursor.execute(sql);
			if self.cursor:
				return self.curser.fetchall();			
				# for row in self.cursor:
					# entryDict={}
					# for numKey in self.attribNumIndex:
						# textKey = self.attribNumIndex[numKey]
						# entryDict[textKey] = row[numKey]
					# return entryDict;
		except:
			return False;
		return False;

	def getAttribById(self,id, attribute):
		""" Get attribute value by id from the dictionary
		@param id :word identifier
		@type id: integer
		@param attribute :the attribute name
		@type attribute: unicode
		@return: The attribute
		value
		@rtype: mix.
		"""
		# if the given attribute existes on the attrib index
		#in order to redure the dictionary size we use numecric index to show the attributes
		# like
		#NOUN_DICTIONATY_INDEX={u'vocalized':0, u'unvocalized':1, u'wordtype':2, u'root':3, u'original':4, u'mankous':5, u'feminable':6, u'number':7, u'dualable':8, u'masculin_plural':9, u'feminin_plural':10, u'broken_plural':11, u'mamnou3_sarf':12, u'relative':13, u'w_suffix':14, u'hm_suffix':15, u'kal_prefix':16, u'ha_suffix':17, u'k_suffix':18, u'annex':19, u'definition':20, u'note':21, }
		#NOUN_DICTIONARY={
		#u'مفرد/تكسير':{0:u'مفرد/تكسير', 1:u'مفرد/تكسير', 2:u'اسم فاعل', 3:u'', 4:u'', 5:u'المنقوص', 6:u'التأنيث', 7:u'جمع تكسير', 8:u'التثنية', 9:u'"ج. مذ. س."', 10:u'"ج. مؤ. س."', 11:u'الجمع', 12:u'', 13:u'نسب', 14:u'ـو', 15:u'هم', 16:u'كال', 17:u'ها', 18:u'ك', 19:u'"إض. لف."', 20:u'', 21:u':لا جذر:لا مفرد:لا تشكيل:لا شرح', },
		#u'شَاذّ':{0:u'شَاذّ', 1:u'شاذ', 2:u'اسم فاعل', 3:u'', 4:u'', 5:u'', 6:u'Ta', 7:u'جمع تكسير', 8:u'DnT', 9:u'Pm', 10:u'Pf', 11:u'":شواذ"', 12:u'', 13:u'', 14:u'', 15:u'', 16:u'', 17:u'', 18:u'', 19:u'', 20:u'', 21:u':لا جذر:لا مفرد:لا شرح', },

		# if self.attribIndex.has_key(attribute):
			# attnum=self.attribIndex[attribute];
		# else:
			# return False;
		# if the id exists and the attribute existe return the value, else return False
		sql = u"select * FROM %s WHERE id='%s'"%(self.tableName,id);
		try:
			self.cursor.execute(sql);
			entryDict={}
			if self.cursor:
				for row in self.cursor:
						# return  row[attnum]
						return  row[attribute]						
		except:
			return False;
		return False;

	def lookup(self,normalized):
		"""
		look up for all word forms in the dictionary
		@param normalized: the normalized word.
		@type normalized: unicode.
		@return: list of dictionary entries .
		@rtype: list.
		"""
		idList=[];
		normword=araby.normalizeHamza(normalized)
		#print "###", normword.encode('utf8');

		sql = u"select * FROM %s WHERE normalized='%s'"%(self.tableName,normword);
		try:
			self.cursor.execute(sql);
			if self.cursor:
				# return self.curser.fetchall();
				for row in self.cursor: idList.append(row);
			return idList;
		except:
			return [];
	def existsAsStamp(self, word):
		"""
		look up for word if exists by using the stamp index,
		the input word is stamped by removing infixes letters like alef, teh
		the stamped word is looked up in the stamp index
		@param word: word to look for.
		@type word: unicode.
		@return: True if exists.
		@rtype: Boolean.
		"""
		stamp=self.wordStamp(word)
		sql = u"select id FROM %s WHERE stamped='%s'"%(self.tableName,stamp);
		try:
			self.cursor.execute(sql);
			if self.cursor:
				return True;
		except:
			return False;
		return False;
	def lookupByStamp(self,word):
		"""
		look up for word if exists by using the stamp index,
		the input word is stamped by removing infixes letters like alef, teh
		the stamped word is looked up in the stamp index
		@param word: to look for.
		@type word: unicode.
		@return: list of dictionary entries IDs.
		@rtype: list.
		"""
		idList=[]
		stamp=self.wordStamp(word)
		sql = u"select * FROM %s WHERE stamped='%s'"%(self.tableName,stamp);
		try:
			self.cursor.execute(sql);
			if self.cursor:
				# return self.curser.fetchall();
				for row in self.cursor: idList.append(row);
			return idList;
		except:
			return [];



	def wordStamp(self,word):
		"""
		generate a stamp for a word,
		remove all letters which can change form in the word :
			- ALEF,
			- HAMZA,
			- YEH,
			- WAW,
			- ALEF_MAKSURA
			- SHADDA
		@return: stamped word
		"""
		# strip the last letter if is doubled
		if word[-1:]== word[-2:-1]:
			word=word[:-1];
		return self.STAMP_pat.sub('',word)

#Class test
if __name__ == '__main__':
	#ToDo: use the full dictionary of arramooz
	VERB_DICTIONARY_INDEX={
u'id':0,
u'vocalized':1,
u'unvocalized':2,
u'root':3,
u'normalized':4,
u'stamped':5,
u'future_type':6,
u'triliteral':7,
u'transitive':8,
u'double_trans':9,
u'think_trans':10,
u'unthink_trans':11,
u'reflexive_trans':12,
u'past':13,
u'future':14,
u'imperative':15,
u'passive':16,
u'future_moode':17,
u'confirmed':18,
	}
	#from   dictionaries.verb_dictionary  import *
	mydict=arabicDictionary('verbs', VERB_DICTIONARY_INDEX);
	wordlist=[u"استقلّ", u'استقل']
	for word in wordlist:
		print("jjjjjjjj")
		idlist=mydict.lookupByStamp(word);
		print(idlist);
		for id in idlist:
			print(mydict.getAttribById(id, u'vocalized').encode('utf8'));
			myentry= mydict.getEntryById(id);
			print(repr(myentry));
			for k in myentry.keys():
				print(u"\t".join([k,unicode(myentry[k])]).encode('utf8'));