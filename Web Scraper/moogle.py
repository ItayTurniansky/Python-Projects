import bs4
import sys
import urllib.parse
import pickle
import requests


def main():
    with open(f"src/{sys.argv[1]}.py") as f:
        exec(f.read())


if __name__ == "__main__":
    main()
