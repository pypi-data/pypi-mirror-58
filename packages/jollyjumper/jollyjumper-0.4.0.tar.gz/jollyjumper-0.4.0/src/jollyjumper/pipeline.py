# -*- coding: utf-8 -*-
import re

import spacy
from spacy.matcher import Matcher
from spacy.tokenizer import Tokenizer
from spacy.tokens import Token
from spacy_affixes import AffixesMatcher
from spacy_affixes.utils import AFFIXES_SUFFIX
from spacy_affixes.utils import load_affixes


def custom_tokenizer(nlp):
    """
    Add custom tokenizer options to the spacy pipeline by adding '-'
    to the list of affixes
    :param nlp: Spacy language model
    :return: New custom tokenizer
    """
    custom_affixes = [r'-']
    prefix_re = spacy.util.compile_prefix_regex(
        list(nlp.Defaults.prefixes) + custom_affixes)
    suffix_re = spacy.util.compile_suffix_regex(
        list(nlp.Defaults.suffixes) + custom_affixes)
    infix_re = spacy.util.compile_infix_regex(
        list(nlp.Defaults.infixes) + custom_affixes)

    return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
                     suffix_search=suffix_re.search,
                     infix_finditer=infix_re.finditer, token_match=None)


# load_pipeline should work as a "singleton"
_load_pipeline = {}


def load_pipeline(lang=None):
    """
    Loads the new pipeline with the custom tokenizer
    :param lang: Spacy language model
    :return: New custom language model
    """
    global _load_pipeline
    if lang is None:
        lang = 'es_core_news_md'
    if lang not in _load_pipeline:
        nlp = spacy.load(lang)
        nlp.tokenizer = custom_tokenizer(nlp)
        nlp.remove_pipe("tmesis") if nlp.has_pipe("tmesis") else None
        nlp.add_pipe(TmesisMatcher(nlp), name="tmesis", first=True)
        nlp.remove_pipe("affixes") if nlp.has_pipe("affixes") else None
        suffixes = {k: v for k, v in load_affixes().items() if
                    k.startswith(AFFIXES_SUFFIX)}
        affixes_matcher = AffixesMatcher(nlp, split_on=["VERB", "AUX"],
                                         rules=suffixes)
        nlp.add_pipe(affixes_matcher, name="affixes", first=True)
        _load_pipeline[lang] = nlp
    return _load_pipeline[lang]


class TmesisMatcher:
    """
    Class defining spacy extended attributes for tmesis
    """

    def __init__(self, nlp):
        self.nlp = nlp
        self.lookup = self.nlp.vocab.lookups.get_table("lemma_lookup")
        if not Token.has_extension("has_tmesis"):
            Token.set_extension("has_tmesis", default=False)
            Token.set_extension("tmesis_text", default="")
        if not Token.has_extension("line"):
            Token.set_extension("line", default=0)

    def __call__(self, doc):
        matcher = Matcher(doc.vocab)
        matcher.add('tmesis', None, [
            {"TEXT": {"REGEX": r"[a-zñ]+"}},
            {"TEXT": {"REGEX": r"-$"}},
            {"TEXT": {"REGEX": r"\n+"}},
            {"TEXT": {"REGEX": r"^[a-zñ]+"}},
        ])
        with doc.retokenize() as retokenizer:
            lookup = self.lookup
            for _, start, end in matcher(doc):
                span_text_raw = doc[start:end].text
                span_text = re.sub(r"-\n", "", span_text_raw)
                has_tmesis = (span_text in lookup.values()
                              or span_text in lookup.keys())
                if has_tmesis:
                    lemma = lookup.get(span_text, span_text)
                else:
                    # If the regular span text is not in the dictionary,
                    # try the lemma under regular Spacy parsing
                    token = self.nlp(span_text)[0]
                    lemma = token.lemma
                    has_tmesis = (token.lemma_ in lookup.values()
                                  or token.lemma_ in lookup.keys())
                attrs = {
                    "LEMMA": lemma,
                    "_": {"has_tmesis": has_tmesis, "tmesis_text": span_text}
                }
                retokenizer.merge(doc[start:end], attrs=attrs)
        line_count = 0
        for token in doc:
            token._.line = line_count  # noqa
            if '\n' in token.text:
                line_count += 1
        return doc
