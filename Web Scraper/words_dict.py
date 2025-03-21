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

BASE_URL = sys.argv[2]
INDEX_FILE = sys.argv[3]
OUT_FILE = sys.argv[4]


def sort_dictionary(dictionary):
    """help function the sorts a dictionary based on its keys from lowest to highest"""
    sorted_dict = {}
    keys_list = sorted(dictionary.keys())
    for key in keys_list:
        sorted_dict[key] = dictionary[key]
    return sorted_dict


def generate_word_dictionary(index_file, base_url_sys):
    """generates the word dictionary"""
    words_dict = {}
    index_file_open = open(index_file, 'r')
    lines = index_file_open.readlines()
    for line in lines:
        base_url = urllib.parse.urljoin(base_url_sys, line.strip())
        response = requests.get(base_url)
        base_url_html = response.text
        soup = bs4.BeautifulSoup(base_url_html, "html.parser")
        words_list = []
        for p in soup.find_all("p"):
            content = p.text.replace("\n", " ").replace("\t", " ")
            for word in content.split(" "):
                if word != "":
                    words_list.append(word)
            for word in words_list:
                if word not in words_dict.keys():
                    words_dict[word] = {}
                    words_dict[word][line.strip()] = 1
                else:
                    if line.strip() in words_dict[word].keys():
                        words_dict[word][line.strip()] += 1
                    else:
                        words_dict[word][line.strip()] = 1
            words_list = []

    return words_dict


if __name__ == "__main__":
    final_words_dict = sort_dictionary(generate_word_dictionary(INDEX_FILE, BASE_URL))
    with open(OUT_FILE, 'wb') as out_file:
        pickle.dump(final_words_dict, out_file)
