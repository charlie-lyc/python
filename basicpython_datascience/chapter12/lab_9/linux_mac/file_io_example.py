# -*- coding: utf8 -*-

def get_file_contents(filename):
    contents = None
    with open(filename, 'r', encoding='utf8') as f:
        contents = f.read()
    f.close()
    return contents


def get_number_of_characters_with_blank(filename):
    contents = get_file_contents(filename)
    result = len(contents)
    return result


def get_number_of_characters_without_blank(filename):
    contents = get_file_contents(filename)
    character_list = [c for c in contents if c != ' ' and c != '\t' and c != '\n']
    result = len(character_list)
    return result


def get_number_of_lines(filename):
    contents = get_file_contents(filename)
    line_list = contents.split('\n')
    result = len(line_list[:-1])
    return result


def get_number_of_target_words(filename, target_words):
    contents = get_file_contents(filename)
    lower_contents = contents.lower()
    result = lower_contents.count(target_words.lower())
    return result




