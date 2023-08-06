# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-12-29 15:14
from typing import Union, Tuple, List, Iterable

import tensorflow as tf

from hanlp.common.structure import SerializableDict
from hanlp.common.transform import Transform
from hanlp.common.vocab import Vocab
from hanlp.components.taggers.transformers.utils import convert_examples_to_features, config_is
from hanlp.layers.transformers import BertTokenizer, PretrainedConfig
from hanlp.transform.tsv import TsvTaggingFormat


class TransformerTransform(TsvTaggingFormat, Transform):
    def __init__(self,
                 transformer_config: PretrainedConfig = None,
                 tokenizer: BertTokenizer = None,
                 config: SerializableDict = None,
                 map_x=False, map_y=False, **kwargs) -> None:
        super().__init__(config, map_x, map_y, **kwargs)
        self.transformer_config = transformer_config
        self._tokenizer = tokenizer
        self.tag_vocab: Vocab = None
        self.special_token_ids = None

    @property
    def tokenizer(self):
        return self._tokenizer

    @tokenizer.setter
    def tokenizer(self, tokenizer):
        self._tokenizer = tokenizer
        self.special_token_ids = tf.constant(self.tokenizer.all_special_ids, dtype=tf.int32)

    def fit(self, trn_path: str, **kwargs) -> int:
        self.tag_vocab = Vocab(unk_token=None)
        num_samples = 0
        for words, tags in self.file_to_inputs(trn_path, gold=True):
            num_samples += 1
            self.tag_vocab.update(tags)
        return num_samples

    def create_types_shapes_values(self) -> Tuple[Tuple, Tuple, Tuple]:
        types = (tf.int32, tf.int32, tf.int32), tf.int32
        # (input_ids, input_mask, segment_ids), label_ids
        shapes = ([None], [None], [None]), [None]
        values = (0, 0, 0), self.tag_vocab.pad_idx
        return types, shapes, values

    def inputs_to_samples(self, inputs, gold=False):
        max_seq_length = self.config.get('max_seq_length', 128)
        tokenizer = self._tokenizer
        config = self.transformer_config
        pad_label_idx = self.tag_vocab.pad_idx
        pad_token = tokenizer.convert_tokens_to_ids([tokenizer.pad_token])[0]
        for sample in inputs:
            if gold:
                words, tags = sample
            else:
                words, tags = sample, [self.tag_vocab.pad_token] * len(sample)
            input_ids, input_mask, segment_ids, label_ids = convert_examples_to_features(words, tags,
                                                                                         self.tag_vocab.token_to_idx,
                                                                                         max_seq_length, tokenizer,
                                                                                         cls_token_at_end=config_is(
                                                                                             config,
                                                                                             'xlnet'),
                                                                                         # xlnet has a cls token at the end
                                                                                         cls_token=tokenizer.cls_token,
                                                                                         cls_token_segment_id=2 if config_is(
                                                                                             config,
                                                                                             'xlnet') else 0,
                                                                                         sep_token=tokenizer.sep_token,
                                                                                         sep_token_extra=config_is(
                                                                                             config,
                                                                                             'roberta'),
                                                                                         # roberta uses an extra separator b/w pairs of sentences, cf. github.com/pytorch/fairseq/commit/1684e166e3da03f5b600dbb7855cb98ddfcd0805
                                                                                         pad_on_left=config_is(config,
                                                                                                               'xlnet'),
                                                                                         # pad on the left for xlnet
                                                                                         pad_token=pad_token,
                                                                                         pad_token_segment_id=4 if config_is(
                                                                                             config,
                                                                                             'xlnet') else 0,
                                                                                         pad_token_label_id=pad_label_idx)

            yield (input_ids, input_mask, segment_ids), label_ids

    def x_to_idx(self, x) -> Union[tf.Tensor, Tuple]:
        raise NotImplementedError('transformers has its own tokenizer, not need to convert idx for x')

    def y_to_idx(self, y) -> tf.Tensor:
        raise NotImplementedError('transformers has its own tokenizer, not need to convert idx for y')

    def input_is_single_sample(self, input: Union[List[str], List[List[str]]]) -> bool:
        return isinstance(input[0], str)

    def Y_to_outputs(self, Y: Union[tf.Tensor, Tuple[tf.Tensor]], gold=False, X=None, inputs=None,
                     **kwargs) -> Iterable:
        assert X is not None, 'Need the X to know actual length of Y'
        input_ids, input_mask, segment_ids = X

        mask = tf.reduce_all(tf.not_equal(tf.expand_dims(input_ids, axis=-1), self.special_token_ids), axis=-1)
        Y = tf.argmax(Y, axis=-1)
        Y = Y[mask]
        tags = [self.tag_vocab.idx_to_token[tid] for tid in Y]
        offset = 0
        for words in inputs:
            yield tags[offset:offset + len(words)]
            offset += len(words)
