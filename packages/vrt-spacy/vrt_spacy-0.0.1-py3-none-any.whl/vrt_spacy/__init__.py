#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Michael Ruppert <michael.ruppert@fau.de>
import warnings

import spacy
from vrt import Corpus, S, Text


class Annotate:
    def __init__(self, corpus, spacymodel="de_core_news_md", add_pattrs=("tag_", "pos_", "lemma_")):
        assert isinstance(corpus, Corpus), "Corpus must be Corpus"
        self._corpus = corpus
        assert isinstance(spacymodel, str)
        # noinspection PyProtectedMember
        assert self._corpus._pattrs == 1 + len(add_pattrs)

        try:
            self._nlp = spacy.load(spacymodel)
        except Exception as e:
            warnings.warn("""Model must be loadable.
            For example you may execute 'python3 -m spacy download de_core_news_md'""")
            raise e

        allowed = ["ent_type_", "lower_", "norm_", "prefix_", "suffix_", "lemma_", "pos_", "tag_", "dep_"]
        for attr in add_pattrs:
            assert attr in allowed
        self._add_patrs = add_pattrs

    def __call__(self, text, **kwargs):
        """
        Uses Spacy for creating annotext
        :param text:
        :return: None
        """
        assert isinstance(text, str)

        with Text(self._corpus, **kwargs) as _:
            for sentence in self._nlp(text).sents:
                with S(self._corpus) as s:
                    for word in sentence:
                        s.writep(word.text, *[getattr(word, attr) for attr in self._add_patrs])
