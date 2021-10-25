from ._mymodule import get_wrong_word, string_to_txt


def spell_check(text_filename: str) -> None:
    str_wrong = get_wrong_word(text_filename)
    string_to_txt(f"wrong_{text_filename}", str_wrong)
