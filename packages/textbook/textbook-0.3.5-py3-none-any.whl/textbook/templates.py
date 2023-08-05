#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-13 09:30:08
# @Author  : Chenghao Mou (chengham@isi.edu)

# pylint: disable=unused-wildcard-import

from typing import *
from loguru import logger

LABEL2INT = {
    "anli": {
        "1": 0,
        "2": 1,
    },
    "hellaswag": {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
    },
    "piqa": {
        "0": 0,
        "1": 1,
    },
    "siqa": {
        "1": 0,
        "2": 1,
        "3": 2
    },
    "codah": {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3
    },
    "cqa": {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4
    },
    "cosmosqa": {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
    },

}

INT2LABEL = {
    key: {
        i: l for l, i in LABEL2INT[key].items()
    }
    for key in LABEL2INT
}


TEMPLATES = {}
__all__ = ["LABEL2INT", "INT2LABEL", "TEMPLATES"]


def template(func):
    global __all__
    global TEMPLATES
    __all__.append(func.__name__)
    TEMPLATES[func.__name__] = func

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@template
def template_anli(datum: Dict, label2int: Dict[str, int]) -> Dict[str, Any]:

    template: Dict[str, Any] = {
        "text": [
                [datum["obs1"], datum["hyp1"], datum["obs2"]],
                [datum["obs1"], datum["hyp2"], datum["obs2"]],
        ],
        "label": None if "label" not in datum else label2int[str(datum["label"])],
        "image": None,
        "token_type_id": [0, 1, 0],
        "attention": [1, 1, 1]
    }

    assert template['label'] is not None, "anli"

    return template


@template
def template_hellaswag(datum: Dict, label2int: Dict[str, int]) -> Dict[str, Any]:

    template: Dict[str, Any] = {
        "text": [
            [datum["ctx"], x] for x in datum["ending_options"]
        ],
        "label": None if "label" not in datum else label2int[str(datum['label'])],
        "image": None,
        "token_type_id": [0, 1],
        "attention": [1, 1]
    }
    assert template['label'] is not None, "hellaswag"

    return template


@template
def template_piqa(datum: Dict, label2int: Dict[str, int]) -> Dict[str, Any]:

    template = {
        "text": [
                [datum["goal"], datum["sol1"]],
                [datum["goal"], datum["sol2"]],
        ],
        "label": None if "label" not in datum else label2int[str(datum['label'])],
        "image": None,
        "token_type_id": [0, 1],
        "attention": [1, 1]
    }

    assert template['label'] is not None, "piqa"

    return template


@template
def template_siqa(datum: Dict, label2int: Dict[str, int]) -> Dict[str, Any]:

    template = {
        "text": [
                [datum["context"], datum["question"], datum["answerA"]],
                [datum["context"], datum["question"], datum["answerB"]],
                [datum["context"], datum["question"], datum["answerC"]],
        ],
        "label": None if "label" not in datum else label2int[str(datum['label'])],
        "image": None,
        "token_type_id": [0, 0, 1],
        "attention": [1, 1, 1]
    }

    assert template['label'] is not None, "siqa"

    return template


@template
def template_cqa(datum: Dict, label2int: Dict[str, int]) -> Dict[str, Any]:

    template = {
        "text": [
                [datum["question"]["stem"], x['text']] for x in datum["question"]["choices"]
        ],
        "label": None if "answerKey" not in datum else label2int[str(datum["answerKey"])],
        "image": None,
        "token_type_id": [0,  1],
        "attention": [1, 1]
    }

    assert template['label'] is not None, "cqa"

    return template


@template
def template_cosmosqa(datum: Dict, label2int: Dict[str, int]) -> Dict[str, Any]:

    template = {
        "text": [
                [datum["context"], datum['question'], datum["answer0"]],
                [datum["context"], datum['question'], datum["answer1"]],
                [datum["context"], datum['question'], datum["answer2"]],
                [datum["context"], datum['question'], datum["answer3"]],

        ],
        "label": None if "label" not in datum else label2int[str(datum["label"])],
        "image": None,
        "token_type_id": [0, 0, 1],
        "attention": [1, 1, 1]
    }

    assert template['label'] is not None, "cqa"

    return template


@template
def template_codah(datum: Dict, label2int: Dict[str, int]) -> Dict[str, Any]:

    result = {
        # "category": datum['category'],
        "text": [
            [datum['prompt'], datum['answer0']],
            [datum['prompt'], datum['answer1']],
            [datum['prompt'], datum['answer2']],
            [datum['prompt'], datum['answer3']]
        ],
        "image": None,
        "label": None if datum['label'] is None else label2int[str(datum['label'])],
        "token_type_id": [0, 1],
        "attention": [1, 1],
    }

    return result


@template
def template_smthsmth(datum: Dict, label2int: Dict[str, int]) -> Dict[str, Any]:
    template = {
        "text": [
                [datum["label"]]
        ],
        "label": None,
        "image": datum["id"],
        "token_type_id": [0],
        "attention": [1]
    }

    return template
