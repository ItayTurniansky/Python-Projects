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

argv = sys.argv
BASE_URL_sys = str(argv[2])
INDEX_FILE_sys = argv[3]
OUT_FILE_sys = argv[4]


def generate_traffic_dictionary(index_file):
    """generates the initial traffic dictionary"""
    index_file_open = open(index_file, 'r')
    lines = index_file_open.readlines()
    pages_list = []
    traffic_dict = {}
    for line in lines:
        pages_list.append(line.strip())
        traffic_dict[line.strip()] = {}
        for line2 in lines:
            traffic_dict[line.strip()][line2.strip()] = 0
    return traffic_dict


def count_traffic_dict(traffic_dict, base_url_sys):
    """generates the final traffic dictionary"""
    for page in traffic_dict.keys():
        base_url = urllib.parse.urljoin(base_url_sys, page)
        response = requests.get(base_url)
        base_url_html = response.text
        soup = bs4.BeautifulSoup(base_url_html, "html.parser")
        for p in soup.find_all("p"):
            for link in p.find_all("a"):
                target = link.get("href")
                if target in traffic_dict[page].keys():
                    traffic_dict[page][target] += 1
        traffic_dict[page] = {x: y for x, y in traffic_dict[page].items() if y != 0}
    return traffic_dict


if __name__ == "__main__":
    starting_dict = generate_traffic_dictionary(INDEX_FILE_sys)
    finished_dic = count_traffic_dict(starting_dict, BASE_URL_sys)
    with open(OUT_FILE_sys, 'wb') as out_file:
        pickle.dump(finished_dic, out_file)
