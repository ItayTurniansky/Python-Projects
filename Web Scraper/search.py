# ################################################################
# FILE : ex6.py WRITER : Itay Turniansky ,itayturni , 322690397
# EXERCISE : intro2cs ex6 2024 DESCRIPTION: Moogle
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: google, chatgpt
# NOTES: None
# ################################################################

import bs4
import sys
import urllib.parse
import pickle
import requests


QUERY = sys.argv[2]
RANKING_DICT_FILE = sys.argv[3]
WORDS_DICT_FILE = sys.argv[4]
MAX_RESULTS = sys.argv[5]


def sort_dictionary_by_value(dict_input):
    """help function the sorts a dictionary based on its values from highest to lowest"""
    sorted_items = sorted(dict_input.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict


def slice_dictionary_by_max(dict_input, max_results):
    """help function the slices a dictionary based on a max input"""
    sliced_items = list(dict_input.items())[:max_results]
    sliced_dict = dict(sliced_items)
    return sliced_dict


def create_first_pages_dict(search_list, words_dict_func, ranking_dict_func):
    """creates the initial pages dictionary"""
    pages_with_words_dict = {}
    counter = 0
    for page_in_rank in ranking_dict_func.keys():
        for word in search_list:
            if word in words_dict_func.keys():
                if page_in_rank in words_dict_func[word].keys():
                    counter += 1
        if counter == len(search_list):
            pages_with_words_dict[page_in_rank] = ranking_dict_func[page_in_rank]
        counter = 0
    return pages_with_words_dict


def rank_pages(first_pages_dict, search_list, words_dict_func):
    """creates the final ranked pages dictionary"""
    final_ranked_pages_dict = {}
    for page_in_dict in first_pages_dict.keys():
        tmp_min_word_value = words_dict_func[search_list[0]][page_in_dict]
        for word in search_list:
            if words_dict_func[word][page_in_dict] < tmp_min_word_value:
                tmp_min_word_value = words_dict_func[word][page_in_dict]
        final_ranked_pages_dict[page_in_dict] = tmp_min_word_value * first_pages_dict[page_in_dict]
    return final_ranked_pages_dict


if __name__ == "__main__":
    dict_ranking_file_open = open(RANKING_DICT_FILE, 'rb')
    ranking_dict = pickle.load(dict_ranking_file_open)
    ranking_dict = sort_dictionary_by_value(ranking_dict)

    words_dict_file_open = open(WORDS_DICT_FILE, 'rb')
    words_dict = pickle.load(words_dict_file_open)

    search_words_list = str.split(QUERY, " ")

    first_ranked_dict = create_first_pages_dict(search_words_list, words_dict, ranking_dict)
    final_ranked_dict = rank_pages(first_ranked_dict, search_words_list, words_dict)
    final_ranked_dict = sort_dictionary_by_value(slice_dictionary_by_max(final_ranked_dict, int(MAX_RESULTS)))
    if final_ranked_dict != {}:
        for page in final_ranked_dict.keys():
            print(page, final_ranked_dict[page])