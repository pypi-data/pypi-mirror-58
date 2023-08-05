# Rules are based on previous work from Pablo Ruiz

import re

ENJAMBMENT_PREPOSITIONS = (
    "a", "al", "ante", "bajo", "con", "contra", "desde", "en", "entre",
    "hacia", "hasta", "para", "por", "según", "sin", "sobre", "tras",
    "mediante", "durante", "salvo", "excepto", "cabe", "so", "como", "cuando",
    "donde")


def get_sirrematic_enjambment(previous_token, next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word after a newline character
    :return: Sirrematic pair or None if not found
    """
    sirremactic_pairs = [
        ['ADJ', 'NOUN'],
        ['ADJ', 'ADV'],
        ['ADJ', 'ADP'],
        ['ADV', 'ADP'],
        ['VERB', 'ADV'],
        ['VERB', 'ADP'],
    ]
    while sirremactic_pairs:
        sirrematic_pair = sirremactic_pairs.pop()
        if sorted((previous_token.pos_, next_token.pos_)) == sorted(
                sirrematic_pair):
            return [previous_token.pos_, next_token.pos_]
        elif next_token.n_rights > 0 and sorted(
                (previous_token.pos_, next_token.nbor().pos_)
        ) == sorted(sirrematic_pair) and next_token.pos_ == "ADV":
            return [previous_token.pos_, next_token.nbor().pos_]
    return None


def get_sirrematic_relation_words_preposition_enjambment(previous_token,
                                                         next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word after a newline character
    :return: Sirrematic type or None if not found
    """
    if (previous_token.lower_ in ENJAMBMENT_PREPOSITIONS
            and re.search('AdpType=Prep', previous_token.tag_)):
        return [previous_token.pos_, next_token.pos_]
    return None


def get_sirrematic_relation_words_conjunction_enjambment(previous_token,
                                                         next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Sirrematic type or None if not found
    """
    if (previous_token.pos_ in ('SCONJ', 'CCONJ', 'CONJ')
            and next_token.pos_):
        return [previous_token.pos_, next_token.pos_]
    return None


def get_sirrematic_relation_words_determiners_enjambment(previous_token,
                                                         next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Sirrematic type or None if not found
    """
    if (previous_token.pos_ == 'DET'
            and next_token.pos_ in ('NOUN', 'ADJ', 'ADV', 'DET')):
        return [previous_token.pos_, next_token.pos_]
    return None


def get_sirrematic_with_verb_enjambment(previous_token, next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Sirrematic type or None if not found
    """
    if previous_token.pos_ in ('AUX', 'VERB') and next_token.pos_ == 'VERB':
        return [previous_token.pos_, next_token.pos_]
    return None


def get_sirrematic_relation_words_verbs_enjambment(previous_token, next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Sirrematic type or None if not found
    """
    if (previous_token.pos_ in ('AUX', 'VERB')
            and re.search('AdpType=Prep', next_token.tag_)
            and next_token.lower_ in ('de', 'del')):
        return [previous_token.pos_, 'PREP']
    return None


def get_sirrematic_orational_enjambment(previous_token, next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Sirrematic type or None if not found
    """
    if (previous_token.pos_ in ('ADJ', 'NOUN', 'ADV')
            and re.search('NumType', next_token.tag_)
            and next_token.lower_ in (
                    'que', 'cuyo', 'cuya', 'cuyos', 'cuyas', 'donde')):
        return [previous_token.pos_, next_token.pos_]
    return None


def get_sirrematic_prepositional_enjambment(previous_token, next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Sirrematic type or None if not found
    """
    if next_token.n_rights > 0 or (next_token.head == previous_token.head):
        if (previous_token.pos_ in ('ADJ', 'ADV', 'NOUN')
                and re.search('AdpType=Prep', next_token.tag_)
                and next_token.nbor().is_ancestor(previous_token)):
            return [previous_token.pos_, 'PREP']
    return None


def get_sirrematic_prepositional_without_de_enjambment(previous_token,
                                                       next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Sirrematic type or None if not found
    """
    if next_token.n_rights > 0 or (next_token.head == previous_token.head):
        if (previous_token.pos_ in ('ADJ', 'NOUN')
                and re.search('AdpType=Prep', next_token.tag_)
                and next_token.lower_ not in ('de', 'del')
                and next_token.nbor().is_ancestor(previous_token)):
            return [previous_token.pos_, 'PREP']
    return None


def get_sirrematic_prepositional_before_noun_adjective_enjambment(
        previous_token, next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Sirrematic type or None if not found
    """
    if next_token.n_rights > 0 or (next_token.head == previous_token.head):
        if (previous_token.dep_ in ('ROOT', 'nsubj')
                and previous_token.pos_ == 'NOUN'
                and re.search('AdpType=Prep', next_token.tag_)
                and next_token.lower_ not in ('de', 'del')
                and next_token.nbor().is_ancestor(previous_token)):
            return [previous_token.pos_, 'PREP']
    return None


def get_link_enjambment(previous_token, next_token):
    """
    Checks if a link enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Link type or None if not found
    """
    if next_token.n_rights > 0 or (next_token.head == previous_token.head):
        if ((previous_token.dep_ in ('ROOT', 'nsubj')
             and previous_token is next_token.head)
                or (next_token.nbor().is_ancestor(previous_token))):
            return [previous_token.pos_, next_token.pos_]
    return None


def get_orational_enjambment(previous_token, next_token):
    """
    Checks if a link enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word before a newline character
    :return: Link type or None if not found
    """
    if (next_token.n_rights > 0
            or next_token.sent.root == previous_token.sent.root):
        if next_token.tag_ == "PRON__PronType=Rel":
            return [previous_token, next_token]
    return None


rules = locals()
