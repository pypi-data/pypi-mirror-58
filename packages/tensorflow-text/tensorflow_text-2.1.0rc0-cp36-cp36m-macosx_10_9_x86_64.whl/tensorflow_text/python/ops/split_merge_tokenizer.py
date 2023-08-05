# coding=utf-8
# Copyright 2019 TF.Text Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Ops to tokenize words into subwords."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.framework import dtypes
from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops.ragged import ragged_tensor
from tensorflow.python.ops.ragged.ragged_tensor import RaggedTensor
from tensorflow_text.python.ops.tokenization import TokenizerWithOffsets

# pylint: disable=g-bad-import-order
from tensorflow.python.framework import load_library
from tensorflow.python.platform import resource_loader
gen_split_merge_tokenizer = load_library.load_op_library(resource_loader.get_path_to_datafile('_split_merge_tokenizer.dylib'))


class SplitMergeTokenizer(TokenizerWithOffsets):
  """Tokenizes a tensor of UTF-8 string into words according to labels."""

  def tokenize(self,
               input,  # pylint: disable=redefined-builtin
               labels,
               force_split_at_break_character=True):
    """Tokenizes a tensor of UTF-8 strings according to labels.

    ### Example:
    ```python
    >>> strings = ["HelloMonday", "DearFriday"],
    >>> labels = [[0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                  [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]]
    >>> tokenizer = SplitMergeTokenizer()
    >>> tokenizer.tokenize(strings, labels)
    [['Hello', 'Monday'], ['Dear', 'Friday']]
    ```

    Args:
      input: An N-dimensional `Tensor` or `RaggedTensor` of UTF-8 strings.
      labels: An (N+1)-dimensional `Tensor` or `RaggedTensor` of int32, with
        labels[i1...iN, j] being the split(0)/merge(1) label of the j-th
        character for input[i1...iN].  Here split means create a new word with
        this character and merge means adding this character to the previous
        word.
      force_split_at_break_character: bool indicates whether to force start a
        new word after seeing a ICU defined whitespace character.  When seeing
        one or more ICU defined whitespace character:
         -if force_split_at_break_character is set true, then create a new word
            at the first non-space character, regardless of the label of that
            character, for instance
            input="New York", labels=[0, 1, 1, 0, 1, 1, 1, 1]
            output tokens=["New", "York"]
            input="New York", labels=[0, 1, 1, 1, 1, 1, 1, 1]
            output tokens=["New", "York"]
            input="New York", labels=[0, 1, 1, 1, 0, 1, 1, 1]
            output tokens=["New", "York"]

         -otherwise, whether to create a new word or not for the first non-space
            character depends on the label of that character, for instance
            input="New York", labels=[0, 1, 1, 0, 1, 1, 1, 1]
            output tokens=["NewYork"]
            input="New York", labels=[0, 1, 1, 1, 1, 1, 1, 1]
            output tokens=["NewYork"]
            input="New York", labels=[0, 1, 1, 1, 0, 1, 1, 1]
            output tokens=["New", "York"]

    Returns:
      A `RaggedTensor` of tokens where `tokens[i1...iN, j]` is the string
      contents (or ID in the vocab_lookup_table representing that string)
      of the `jth` token in `input[i1...iN]`
    """
    subword, _, _ = self.tokenize_with_offsets(input, labels)
    return subword

  def tokenize_with_offsets(self,
                            input,  # pylint: disable=redefined-builtin
                            labels,
                            force_split_at_break_character=True):
    """Tokenizes a tensor of UTF-8 string tokens further into subword tokens.

    ### Example:

    ```python
    >>> strings = ["HelloMonday", "DearFriday"],
    >>> labels = [[0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                  [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]]
    >>> tokenizer = SplitMergeTokenizer()
    >>> result = tokenizer.tokenize_with_offsets(strings, labels)
    >>> result[0].to_list()
    [['Hello', 'Monday'], ['Dear', 'Friday']]
    >>> result[1].to_list()
    >>> [[0, 5], [0, 4]]
    >>> result[2].to_list()
    >>> [[5, 11], [4, 10]]
    ```

    Args:
      input: An N-dimensional `Tensor` or `RaggedTensor` of UTF-8 strings.
      labels: An (N+1)-dimensional `Tensor` or `RaggedTensor` of int32, with
        labels[i1...iN, j] being the split(0)/merge(1) label of the j-th
        character for input[i1...iN].  Here split means create a new word with
        this character and merge means adding this character to the previous
        word.
      force_split_at_break_character: bool indicates whether to force start a
        new word after seeing a ICU defined whitespace character.  When seeing
        one or more ICU defined whitespace character:
         -if force_split_at_break_character is set true, then create a new word
            at the first non-space character, regardless of the label of that
            character, for instance
            input="New York", labels=[0, 1, 1, 0, 1, 1, 1, 1]
            output tokens=["New", "York"]
            input="New York", labels=[0, 1, 1, 1, 1, 1, 1, 1]
            output tokens=["New", "York"]
            input="New York", labels=[0, 1, 1, 1, 0, 1, 1, 1]
            output tokens=["New", "York"]

         -otherwise, whether to create a new word or not for the first non-space
            character depends on the label of that character, for instance
            input="New York", labels=[0, 1, 1, 0, 1, 1, 1, 1]
            output tokens=["NewYork"]
            input="New York", labels=[0, 1, 1, 1, 1, 1, 1, 1]
            output tokens=["NewYork"]
            input="New York", labels=[0, 1, 1, 1, 0, 1, 1, 1]
            output tokens=["New", "York"]

    Returns:
      A `RaggedTensor` of tokens where `tokens[i1...iN, j]` is the string
      contents (or ID in the vocab_lookup_table representing that string)
      of the `jth` token in `input[i1...iN]`

    Returns:
      A tuple `(tokens, start_offsets, limit_offsets)` where:

        * `tokens[i1...iN, j]` is a `RaggedTensor` of the string contents (or ID
          in the vocab_lookup_table representing that string) of the `jth` token
          in `input[i1...iN]`.
        * `start_offsets[i1...iN, j]` is a `RaggedTensor` of the byte offsets
          for the start of the `jth` token in `input[i1...iN]`.
        * `limit_offsets[i1...iN, j]` is a `RaggedTensor` of the byte offsets
          for the end of the `jth` token in `input[i`...iN]`.
    """
    name = None
    with ops.name_scope(
        name, 'SplitMergeTokenizeWithOffsets',
        [input, labels, force_split_at_break_character]):
      # Check that the types are expected and the ragged rank is appropriate.
      tokens = ragged_tensor.convert_to_tensor_or_ragged_tensor(input)
      labels = ragged_tensor.convert_to_tensor_or_ragged_tensor(labels)
      rank = tokens.shape.ndims
      if rank is None:
        raise ValueError('input must have a known rank.')

      if rank == 0:
        words, starts, limits = self.tokenize_with_offsets(
            array_ops.stack([tokens]),
            array_ops.stack([labels]),
            force_split_at_break_character)
        return words.values, starts.values, limits.values

      elif rank > 1:
        if not ragged_tensor.is_ragged(tokens):
          tokens = ragged_tensor.RaggedTensor.from_tensor(
              tokens, ragged_rank=rank - 1)

        # Convert to a 2D ragged tensor from labels of shape
        # [#input_string, (labels per string)]
        if not ragged_tensor.is_ragged(labels):
          labels2d = array_ops.reshape(labels, [-1, labels.shape[-1]])
          labels_unpack = ragged_tensor.RaggedTensor.from_tensor(labels2d)
        else:
          labels_unpack = ragged_tensor.RaggedTensor.from_row_splits(
              values=labels.flat_values,
              row_splits=labels.nested_row_splits[-1])
        words, starts, limits = self.tokenize_with_offsets(
            tokens.flat_values,
            labels_unpack,
            force_split_at_break_character)
        words = words.with_row_splits_dtype(tokens.row_splits.dtype)
        starts = starts.with_row_splits_dtype(tokens.row_splits.dtype)
        limits = limits.with_row_splits_dtype(tokens.row_splits.dtype)
        return (tokens.with_flat_values(words),
                tokens.with_flat_values(starts),
                tokens.with_flat_values(limits))

      if not ragged_tensor.is_ragged(labels):
        ragged_labels = ragged_tensor.RaggedTensor.from_tensor(labels)
      else:
        ragged_labels = labels

      row_splits = math_ops.cast(ragged_labels.row_splits, dtypes.int32)

      # Tokenize the strings into tokens.
      values, row_splits, starts, limits = (
          gen_split_merge_tokenizer.split_merge_tokenize_with_offsets(
              input_values=tokens,
              labels=ragged_labels.flat_values,
              row_splits=row_splits,
              force_split_at_break_character=force_split_at_break_character))

      words = RaggedTensor.from_row_splits(values, row_splits, validate=False)
      starts = RaggedTensor.from_row_splits(starts, row_splits, validate=False)
      limits = RaggedTensor.from_row_splits(limits, row_splits, validate=False)
      return words, starts, limits
