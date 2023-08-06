#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-13 09:48:30
# @Author  : Chenghao Mou (chengham@isi.edu)

# pylint: disable=no-member
# pylint: disable=unused-wildcard-import


import os
from typing import *
from pathlib import Path

from .transforms_video import *

import torchvision
import av
from transformers import PreTrainedTokenizer
from loguru import logger

SCALE = 1.1


def renderer_text(datum: Dict[str, Any], tokenizer: PreTrainedTokenizer, task_token: str = None) -> Dict[str, Any]:

    assert getattr(tokenizer, "cls_token") is not None, "cls token not found"
    assert getattr(tokenizer, "pad_token") is not None, "pad token not found"
    assert getattr(tokenizer, "mask_token") is not None, "mask token not found"

    task_token = task_token if task_token is not None else tokenizer.cls_token

    template = {
        "input_id": [[] for _ in range(len(datum["text"]))],
        "label": datum["label"],
        "attention": [[] for _ in range(len(datum["text"]))],
        "token_type_id": [[] for _ in range(len(datum["text"]))],
        "image": datum["image"],
    }

    max_seq_len = 0

    for i, group in enumerate(datum["text"]):

        for j, (attn, token_type, sentence) in enumerate(zip(datum["attention"], datum["token_type_id"], group)):
            tokens = tokenizer.tokenize(sentence)
            if j == 0:
                tokens = [task_token] + tokens
            tokens = tokens + [tokenizer.pad_token]

            template["attention"][i].extend(attn for _ in tokens)
            template["token_type_id"][i].extend(token_type for _ in tokens)
            template["input_id"][i].extend(tokenizer.convert_tokens_to_ids(tokens))

        max_seq_len = max(max_seq_len, len(template["input_id"][i]))

    for j in range(len(template["input_id"])):
        while len(template["input_id"][j]) < max_seq_len:
            template["input_id"][j].append(tokenizer.pad_token_id)
            template["attention"][j].append(0)
            template["token_type_id"][j].append(0)

    return template


def renderer_video(datum: Dict[str, Any],
                   data_dir: Union[Path, str],
                   nframe: int = 72,
                   nclip: int = 1,
                   width: int = 64,
                   dstep_size: int = 1):

    upscale_size = int(width * SCALE)
    transform_pre = ComposeMix([
        [Scale(upscale_size), "img"],
        [RandomCropVideo(width), "vid"],
    ])
    transform_post = ComposeMix([
        [torchvision.transforms.ToTensor(), "img"],
    ])

    path = os.path.join(data_dir, datum["image"] + ".webm")
    reader = av.open(path)

    try:
        imgs = []
        imgs = [f.to_rgb().to_ndarray() for f in reader.decode(video=0)]
    except (RuntimeError, ZeroDivisionError) as exception:
        logger.debug('{}: WEBM reader cannot open {}. Empty list returned.'.format(type(exception).__name__, path))

    imgs = transform_pre(imgs)
    imgs = transform_post(imgs)

    num_frames = len(imgs)

    if nclip > -1:
        num_frames_necessary = nframe * nclip * dstep_size
    else:
        num_frames_necessary = num_frames

    offset = 0
    if num_frames_necessary < num_frames:
        # If there are more frames, then sample a starting offset.
        diff = (num_frames - num_frames_necessary)
        offset = np.random.randint(0, diff)

    imgs = imgs[offset: num_frames_necessary + offset: dstep_size]

    if len(imgs) < (nframe * nclip):
        imgs.extend([imgs[-1]] * ((nframe * nclip) - len(imgs)))

    data = torch.stack(imgs)
    data = data.permute(1, 0, 2, 3)

    datum["image"] = data

    return datum


__all__ = ["renderer_video", "renderer_text"]
