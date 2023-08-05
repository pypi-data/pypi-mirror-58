#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-17 18:09:14
# @Author  : Chenghao Mou (mouchenghao@gmail.com)
# @Link    : link
# @Version : 1.0.0

# pylint: disable=unused-wildcard-import
# pylint: disable=no-member
# pylint: disable=not-callable

import os
import random
import json
from typing import *
from pathlib import Path
from dataclasses import dataclass

from .templates import *
from .renderers import *

import pandas as pd
from torch.utils.data import Dataset
from tqdm import tqdm
from loguru import logger


class MultiModalDataset(Dataset):

    def __init__(self, df: pd.DataFrame, template: Callable, renderers: List[Callable]):
        df = df.apply(template, axis=1, result_type='expand')
        for renderer in renderers:
            df = df.apply(renderer, axis=1, result_type='expand')
        self.data: List[Dict] = df.to_dict('records')

    def __len__(self):

        return len(self.data)

    def __getitem__(self, index):

        return self.data[index]


class MultiTaskDataset(Dataset):

    def __init__(self, dataloaders, shuffle: bool = True):

        self.data: List = []

        for loader in tqdm(dataloaders):
            for batch in tqdm(loader, leave=False):
                self.data.append(batch)

        if shuffle:
            random.shuffle(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]


__all__ = ["MultiTaskDataset", "MultiModalDataset"]
