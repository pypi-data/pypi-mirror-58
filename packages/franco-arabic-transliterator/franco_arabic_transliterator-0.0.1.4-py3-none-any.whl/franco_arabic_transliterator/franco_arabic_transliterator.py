import re
import hfst
import string
import logging
import pkg_resources
from functools import reduce

class FrancoArabicTransliterator:
	def __init__(self):
		""" Construct a transliterator object"""
		rules_file_location = pkg_resources.resource_filename('data', 'hfst.att')
		with open(rules_file_location, 'r') as f:
			self.transducer = hfst.AttReader(f).read()
		self.logger = logging.getLogger('franco_arabic_transliterator')
		logging.basicConfig(level=logging.DEBUG)

		with open(pkg_resources.resource_filename('data', 'lexicon'), 'r') as f:
			self.wordlist = {l.split('\t')[0]: int(l.split('\t')[1]) for l in f.readlines()}

	def transliterate(self, sentence):
		"""Transliterate a sentence."""
		transliteration = []
		for word in sentence.split():
			word = word.lower()
			transliteration.append(
				sorted(self.__transliterate_word('^{}$'.format(word))))
		self.logger.info('Number of valid strings before lexicon search are: {}'.format(
			reduce((lambda x, y: x * y), [len(t) for t in transliteration])))
		transliteration = [self.__filter(r, w.lower()) for r, w in zip(transliteration, sentence.split())]
		self.logger.info('Number of valid strings after lexicon search are: {}'.format(
			reduce((lambda x, y: x * y), [len(t) for t in transliteration])))
		return ' '.join([self.__disambiguate(results) for results in transliteration])

	def __transliterate_word(self, word, temperorary_results_dictionary={}):
		"""Find all the possible transliteration given the regex rules
		- Divide the word into all the valid prefixes, suffixes
		- Find the possible transliterations for the prefixes, suffixes
		- Join the prefix and suffix transliterations
		"""
		if not word:
			return set()
		if word in temperorary_results_dictionary:
			return temperorary_results_dictionary[word]
		results = self.__get_analyses(word)
		for index in range(1, len(word)):
			results = results.union(self.__join(
				self.__transliterate_word(word[:index], temperorary_results_dictionary),
				self.__transliterate_word(word[index:], temperorary_results_dictionary)))
		temperorary_results_dictionary[word] = results
		return results

	def __filter(self, word_results, word):
		"""Use the lexicon to filter the results"""
		self.logger.debug('Results before disambiguation: {}'.format(' '.join(word_results)))
		if sum([r in self.wordlist for r in word_results]) >0:
			return {r: self.wordlist[r] - 50 * abs(len(r) - len(word)) for r in word_results if r in self.wordlist}
		return {w:1/(1+abs(len(w) - len(word))) for w in word_results}

	def __disambiguate(self, word_results):
		"""Select the most relevant result"""
		self.logger.debug('Results before disambiguation: {}'.format(' '.join(['{}: {}'.format(w, word_results[w])for w in word_results])))
		# TODO: Use a better sorting function
		return sorted(word_results, key=lambda t: word_results[t])[-1]

	def __get_analyses(self, word):
		"""Find all the possible matches for a word string in the regex transducer"""
		results = self.transducer.lookup(word, output='raw')
		if results:
			return set([''.join([r for r in result[1] if not '@_EPSILON_SYMBOL_@' in r]) for result in results])
		else:
			return set()

	def __join(self, prefixes_set, suffixes_set):
		"""Join the results of prefix and suffix sets into a single merged results set"""
		if not prefixes_set and not suffixes_set:
			return set()

		if not prefixes_set:
			return suffixes_set

		if not suffixes_set:
			return prefixes_set

		prefixes_set = list(prefixes_set)
		suffixes_set = list(suffixes_set)
		return set(['{}{}'.format(i1, i2) for i1 in prefixes_set for i2 in suffixes_set])

if __name__=='__main__':
	word = input()
	transliterator = FrancoArabicTransliterator()
	print(transliterator.transliterate(word))
