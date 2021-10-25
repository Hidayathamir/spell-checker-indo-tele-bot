import re
from typing import Set

import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


def get_wrong_word(text_filename: str) -> str:
    """
    return string that does not in kbbi.csv
    (https://raw.githubusercontent.com/Hidayathamir/kata-kbbi-github/main/kbbi.csv)
    first get set_wrong without stem, then stem, then try again to get set_wrong.

    Dev Note : cost for stemming is high. so we only stem word that not in set_kbbi
    """
    set_kbbi = get_set_from_csv("kbbi.csv")
    set_text_user = get_set_from_txt(text_filename)
    set_wrong = set_text_user - set_kbbi
    set_wrong = stem_set(set_wrong)
    set_wrong = set_wrong - set_kbbi
    return " ".join(sorted(set_wrong))


def string_to_txt(text_filename: str, str_wrong: str) -> None:
    """create new file from string"""
    with open(text_filename, "w") as file:
        file.write(str_wrong)


def get_set_from_csv(csv_filename) -> Set[str]:
    """return set from csv file"""
    return set(pd.read_csv(csv_filename)["kata"])


def get_set_from_txt(filename: str) -> Set[str]:
    """return set from file text file, and only accept letters"""
    with open(filename, "r") as file:
        text = file.read().lower()
        text = re.sub("[^a-zA-Z ]+", " ", text)
        return set(text.split())


def stem_set(set_wrong: Set[str]) -> Set[str]:
    """return set that has been stem"""
    stemmer = StemmerFactory().create_stemmer()
    text = " ".join(set_wrong)
    str_wrong = stemmer.stem(text)
    return set(str_wrong.split())
