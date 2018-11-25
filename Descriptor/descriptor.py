import gensim
import numpy as np
import pycorpora as pc
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class FoodDescriptor:
    """Class for analysing and checking text from image. We could recognize
    several types of food which you can find in dictionary initialiazing method.
    As output we provide ingredients list from input food composition text.
    """
    def __init__(self):
        self.food_ingred = {}
        self.__initialize_food_dictionary()

    def __initialize_food_dictionary(self):
        """Initialize dictionary of food ingredients for detection"""

        self.food_ingred['fruits'] = np.array(pc.foods.fruits['fruits'])
        self.food_ingred['condiments'] = np.array(pc.foods.condiments['condiments'])
        self.food_ingred['herbs'] = np.array(pc.foods.herbs_n_spices['herbs'])
        self.food_ingred['spices'] = np.array(pc.foods.herbs_n_spices['spices'])
        self.food_ingred['vegetables'] = np.array(pc.foods.vegetables['vegetables'])
        self.food_ingred['curds'] = np.array(pc.foods.curds['curds'])
        # clean dictionary of ingredient words
        for food_key in self.food_ingred.keys():
            self.food_ingred[food_key] = list(map(lambda ingred: ingred.lower(), self.food_ingred[food_key]))

    def __clean_text(self, text):
        """Clean text for further processing and information mining

        Arguments
            text : str
                Text of food composition.

        Returns
            cleaned_text : str
                Text without stop words and commas.

        """
        text = text.lower()
        text = text.replace(',', '')
        cleaned_text = text.split()
        return cleaned_text

    def __get_ngrams(self, text):
        """Get ngrams from the input text

        Arguments
            text : str
                Text of food composition.

        Returns
            text_onegram : list of shape = (num_onegrams, 1)
                One-grams generated from input text.
            text_bigram : list of shape = (num_bigrams, 1)
                Bi-grams generated from input text.
            text_trigram : list of shape = (num_trigrams, 1)
                Tri-grams generated from input text.

        """
        text_onegram = [onegram[0] for onegram in ngrams(text, 1)]
        text_bigram = [bigram[0] + ' ' + bigram[1] for bigram in ngrams(text, 2)]
        text_trigram = [trigram[0] + ' ' + trigram[1] + ' ' + trigram[2] for trigram in ngrams(text, 3)]
        return text_onegram, text_bigram, text_trigram

    def __count_ingredients(self, text):
        """Count number of each ingredient from food composition

        Arguments
            text : str
                Text of food composition.

        Returns
            food_ingred_counter : dict key=ingredient, value=number of appearance
                Counts of food ingredients

        """
        text_onegram, text_bigram, text_trigram = self.__get_ngrams(text)

        food_ingred_counter = {}

        for ingred_kind in self.food_ingred.keys():
            food_ingred_counter[ingred_kind] = []
            for ingred in self.food_ingred[ingred_kind]:
                if ingred in text_onegram or ingred in text_bigram or ingred in text_trigram:
                    food_ingred_counter[ingred_kind].append(ingred)

        return food_ingred_counter

    def get_description(self, text):
        """Main function of food descriptor

        Parameters
            text : str
                Input text from image text miner

        Returns
            food_ingred_counter : dict
                Counts of food ingredients
        
        """
        text = self.__clean_text(text)
        food_ingred_counter = self.__count_ingredients(text)
        return food_ingred_counter

