#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-13 10:43:56
# @Author  : Chenghao Mou(chengham@isi.edu)

# pylint: disable=no-member
# pylint: disable=unused-wildcard-import
# pylint: disable=invalid-sequence-index
# pylint: disable=not-callable

import os
import random
import json
from typing import *
from pathlib import Path
from dataclasses import dataclass
from itertools import zip_longest

from .templates import *
from .renderers import *

import torch
from torch.utils.data import Dataset, Sampler
from torch.nn.utils.rnn import pad_sequence
from transformers import PreTrainedTokenizer
import pandas as pd


class TokenBasedSampler(Sampler):

    def __init__(self, data_source, batch_size=128):
        self.data_source = data_source
        self.batch_size = batch_size

    def __iter__(self):

        indices: List[List[int]] = [[]]
        curr_max: int = 0
        for i, x in enumerate(self.data_source):
            num, max_len = len(x['input_id']), max(map(len, x['input_id']))
            curr_max = max(max_len, curr_max)
            l = ((len(indices[-1]) + 1) * num) * curr_max
            if l > self.batch_size and indices[-1]:
                indices.append([i])
                curr_max = max_len
            else:
                indices[-1].append(i)

        return iter(indices)


@dataclass
class BatchTool:

    tokenizer: PreTrainedTokenizer
    max_seq_len: int = 128
    mlm: bool = False
    mlm_probability: float = 0.15
    source: str = ""

    def collate_fn(self, samples: List[Dict[str, Any]]) -> Dict[str, Any]:

        template: Dict = {
            "input_ids": [],
            "labels": [],
            "attentions": [],
            "images": [],
            "token_type_ids": [],
            "source": self.source
        }

        for sample in samples:

            template["input_ids"].append(torch.LongTensor(sample["input_id"]).transpose(0, 1))
            template["attentions"].append(torch.LongTensor(sample["attention"]).transpose(0, 1))
            template["token_type_ids"].append(torch.LongTensor(sample["token_type_id"]).transpose(0, 1))
            if sample["image"] is not None:
                template["images"].append(sample["image"])
            if sample["label"] is not None:
                template["labels"].append(sample["label"])

        template["input_ids"]: torch.tensor = pad_sequence(template["input_ids"], batch_first=True).transpose(1, 2)
        template["attentions"]: torch.tensor = pad_sequence(template["attentions"], batch_first=True).transpose(1, 2)
        template["token_type_ids"]: torch.tensor = pad_sequence(template["token_type_ids"], batch_first=True).transpose(1, 2)

        template["input_ids"]: torch.tensor = template["input_ids"][..., :self.max_seq_len]
        template["attentions"]: torch.tensor = template["attentions"][..., :self.max_seq_len]
        template["token_type_ids"]: torch.tensor = template["token_type_ids"][..., :self.max_seq_len]

        template["images"] = torch.stack(template["images"]) if template["images"] else None

        if template["labels"] != []:
            template["labels"] = torch.LongTensor(template["labels"])
        if self.mlm == True:
            batch_size, num_choice, seq_length = template["input_ids"].shape
            template["input_ids"], template["labels"] = self.mask_tokens(
                template["input_ids"].reshape(-1, seq_length))
            template["input_ids"] = template["input_ids"].reshape(batch_size, num_choice, seq_length)
            template["labels"] = template["labels"].reshape(batch_size, num_choice, seq_length)

        return template

    def mask_tokens(self, input_ids):
        labels = input_ids.clone()
        probability_matrix = torch.full(labels.shape, self.mlm_probability)
        special_tokens_mask = [self.tokenizer.get_special_tokens_mask(val, already_has_special_tokens=True) for val in labels.tolist()]
        probability_matrix.masked_fill_(torch.tensor(special_tokens_mask, dtype=torch.bool), value=0.0)
        masked_indices = torch.bernoulli(probability_matrix).bool()
        labels[~masked_indices] = -1  # We only compute loss on masked tokens

        # 80% of the time, we replace masked input tokens with tokenizer.mask_token ([MASK])
        indices_replaced = torch.bernoulli(torch.full(labels.shape, 0.8)).bool() & masked_indices
        input_ids[indices_replaced] = self.tokenizer.mask_token_id

        # 10% of the time, we replace masked input tokens with random word
        indices_random = torch.bernoulli(torch.full(labels.shape, 0.5)).bool() & masked_indices & ~indices_replaced
        random_words = torch.randint(len(self.tokenizer), labels.shape, dtype=torch.long)
        input_ids[indices_random] = random_words[indices_random]

        # The rest of the time (10% of the time) we keep the masked input tokens unchanged
        return input_ids, labels

    @classmethod
    def uncollate_fn(cls, samples: List):

        assert len(samples) == 1

        return samples[0]


__all__ = ["BatchTool", "TokenBasedSampler"]
