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

ITERATIONS = sys.argv[2]
CRAWL_DICT_FILE = sys.argv[3]
OUT_FILE = sys.argv[4]


def generate_page_rank_dictionary(crawl_dict_file):
    """generates the first page rank dictionary with all 1 values"""
    dict_crawl_file_open = open(crawl_dict_file, 'rb')
    crawl_dict = pickle.load(dict_crawl_file_open)
    page_rank_dict = {}
    for page in crawl_dict.keys():
        page_rank_dict[page] = 1
    return page_rank_dict


def generate_total_links_counter_dict(crawl_dict_file):
    """generate total out links per page dictionary """
    dict_crawl_file_open = open(crawl_dict_file, 'rb')
    crawl_dict = pickle.load(dict_crawl_file_open)
    page_rank_dict = {}
    tmp_total = 0
    for page in crawl_dict.keys():
        for link_counter in crawl_dict[page].values():
            tmp_total += int(link_counter)
        page_rank_dict[page] = tmp_total
        tmp_total = 0
    return page_rank_dict


def calculate_page_rank(iterations, crawl_dict_file, page_rank_dict, crawl_counter_dict):
    """"updates the page rank dictionary based on the formula and iterations"""
    dict_crawl_file_open = open(crawl_dict_file, 'rb')
    crawl_dict = pickle.load(dict_crawl_file_open)
    for i in range(int(iterations)):
        tmp_dict = {}
        for page in page_rank_dict.keys():
            tmp_dict[page] = 0
        for page in tmp_dict.keys():
            for sub_page in tmp_dict.keys():
                if page in crawl_dict[sub_page].keys():
                    tmp_dict[page] += (page_rank_dict[sub_page])*(int(crawl_dict[sub_page][page]) / int(crawl_counter_dict[sub_page]))
        for page in tmp_dict.keys():
            page_rank_dict[page] = tmp_dict[page]
    return page_rank_dict


if __name__ == "__main__":
    first_page_rank_dict = generate_page_rank_dictionary(CRAWL_DICT_FILE)
    counter_dict = generate_total_links_counter_dict(CRAWL_DICT_FILE)
    final_page_rank_dict = calculate_page_rank(ITERATIONS, CRAWL_DICT_FILE, first_page_rank_dict, counter_dict)
    with open(OUT_FILE, 'wb') as out_file:
        pickle.dump(final_page_rank_dict, out_file)


