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

"""Whitespace tokenizer for string tensors."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.framework import dtypes
from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops.ragged import ragged_conversion_ops
from tensorflow.python.ops.ragged import ragged_tensor
from tensorflow.python.ops.ragged.ragged_tensor import RaggedTensor
from tensorflow_text.python.ops.tokenization import Detokenizer
from tensorflow_text.python.ops.tokenization import TokenizerWithOffsets

from tensorflow.python.framework import load_library
from tensorflow.python.platform import resource_loader
gen_sentencepiece_tokenizer = load_library.load_op_library(resource_loader.get_path_to_datafile('_sentencepiece_tokenizer.dylib'))  # pylint: disable=g-bad-import-order


class SentencepieceTokenizer(TokenizerWithOffsets, Detokenizer):
  """Tokenizes a tensor of UTF-8 strings."""

  def __init__(self,
               model=None,
               out_type=dtypes.int32,
               nbest_size=0,
               alpha=1.0,
               reverse=False,
               add_bos=False,
               add_eos=False,
               name=None):
    """Creates & initializes a Sentencepiece processor.

    Args:
      model: The sentencepiece model serialized proto.
      out_type: output type. tf.int32 or tf.string (Default = tf.int32) Setting
        tf.int32 directly encodes the string into an id sequence.
      nbest_size: A scalar for sampling.
                nbest_size = {0,1}: No sampling is performed. (default)
                nbest_size > 1: samples from the nbest_size results.
                nbest_size < 0: assuming that nbest_size is infinite and samples
                  from the all hypothesis (lattice) using
                  forward-filtering-and-backward-sampling algorithm.
      alpha: A scalar for a smoothing parameter. Inverse temperature for
        probability rescaling.
      reverse: Reverses the tokenized sequence (Default = false)
      add_bos: Add <s> to the result (Default = false)
      add_eos: Add </s> to the result (Default = false) <s>/</s> is added after
        reversing (if enabled).
      name: The name argument that is passed to the op function.

    Returns:
      pieces: A SentencepieceTokenizer.
    """
    self.nbest_size = nbest_size
    self.alpha = alpha
    self.out_type = out_type
    self.reverse = reverse
    self.add_bos = add_bos
    self.add_eos = add_eos
    with ops.name_scope(name, "SentenceTokenizerInitializer", [model]):
      self._resource_handle = gen_sentencepiece_tokenizer.sentencepiece_op(
          model=model)

  def tokenize(self, input, name=None):  # pylint: disable=redefined-builtin
    """Tokenizes a tensor of UTF-8 strings.

    Args:
      input: A `RaggedTensor` or `Tensor` of UTF-8 strings with any shape.
      name: The name argument that is passed to the op function.

    Returns:
      A `RaggedTensor` of tokenized text. The returned shape is the shape of the
      input tensor with an added ragged dimension for tokens of each string.
    """
    with ops.name_scope(name, "SentenceTokenizer", [input, self]):
      input_tensor = ragged_tensor.convert_to_tensor_or_ragged_tensor(input)
      if input_tensor.shape.ndims is None:
        raise ValueError("Rank of input_tensor must be statically known.")
      if ragged_tensor.is_ragged(input_tensor):
        # Recursively process the values of the ragged tensor.
        tokens = self.tokenize(input_tensor.flat_values)
        return input_tensor.with_flat_values(tokens)
      else:
        if input_tensor.shape.ndims > 1:
          # Convert the input tensor to ragged and process it.
          return self.tokenize(ragged_conversion_ops.from_tensor(input_tensor))
        elif input_tensor.shape.ndims == 0:
          tokens = self.tokenize(array_ops.stack([input_tensor]))
          return tokens.values
        else:
          # Our rank 1 tensor is the correct shape, so we can process it as
          # normal.
          (output_values, row_splits) = (
              gen_sentencepiece_tokenizer.sentencepiece_tokenize_op(
                  self._resource_handle, input_tensor, self.nbest_size,
                  self.alpha, self.add_bos, self.add_eos, self.reverse,
                  self.out_type))
          tokens = RaggedTensor.from_nested_row_splits(
              flat_values=output_values,
              nested_row_splits=[row_splits],
              validate=False)
          return tokens

  def tokenize_with_offsets(self, input, name=None):  # pylint: disable=redefined-builtin
    """Tokenizes a tensor of UTF-8 strings.

    Args:
      input: A `RaggedTensor` or `Tensor` of UTF-8 strings with any shape.
      name: The name argument that is passed to the op function.

    Returns:
      A `RaggedTensor` of tokenized text. The returned shape is the shape of the
      input tensor with an added ragged dimension for tokens of each string.
    """
    with ops.name_scope(name, "SentenceTokenizer", [input, self]):
      input_tensor = ragged_tensor.convert_to_tensor_or_ragged_tensor(input)
      if input_tensor.shape.ndims is None:
        raise ValueError("Rank of input_tensor must be statically known.")
      if ragged_tensor.is_ragged(input_tensor):
        # Recursively process the values of the ragged tensor
        (tokens, starts,
         limits) = self.tokenize_with_offsets(input_tensor.flat_values)
        tokens = input_tensor.with_flat_values(tokens)
        starts = input_tensor.with_flat_values(starts)
        limits = input_tensor.with_flat_values(limits)
        return (tokens, starts, limits)
      else:
        if input_tensor.shape.ndims > 1:
          # Convert the input tensor to ragged and process it.
          return self.tokenize_with_offsets(
              ragged_conversion_ops.from_tensor(input_tensor))
        elif input_tensor.shape.ndims == 0:
          (tokens, starts, limits) = self.tokenize_with_offsets(
              array_ops.stack([input_tensor]))
          tokens = tokens.values
          starts = starts.values
          limits = limits.values
          return (tokens, starts, limits)
        else:
          # Our rank 1 tensor is the correct shape, so we can process it as
          # normal.
          (output_values, output_splits, output_offset_starts,
           output_offset_limits) = (
               gen_sentencepiece_tokenizer
               .sentencepiece_tokenize_with_offsets_op(
                   self._resource_handle, input_tensor, self.nbest_size,
                   self.alpha, self.add_bos, self.add_eos, self.reverse,
                   self.out_type))
          tokens = RaggedTensor.from_nested_row_splits(
              flat_values=output_values,
              nested_row_splits=[output_splits],
              validate=False)
          starts = RaggedTensor.from_nested_row_splits(
              flat_values=output_offset_starts,
              nested_row_splits=[output_splits],
              validate=False)
          limits = RaggedTensor.from_nested_row_splits(
              flat_values=output_offset_limits,
              nested_row_splits=[output_splits],
              validate=False)
          return (tokens, starts, limits)

  def detokenize(self, input, name=None):  # pylint: disable=redefined-builtin
    """Detokenizes tokens into preprocessed text.

    Args:
      input: A `RaggedTensor` or `Tensor` of UTF-8 string tokens with a rank of
        at least 1.
      name: The name argument that is passed to the op function.

    Returns:
      A N-1 dimensional string Tensor or RaggedTensor of the detokenized text.
    """
    with ops.name_scope(name, "SentenceTokenizer", [input, self]):
      input_tensor = ragged_tensor.convert_to_tensor_or_ragged_tensor(input)
      if input_tensor.shape.ndims is None:
        raise ValueError("Rank of input_tensor must be statically known.")
      if input_tensor.shape.ndims == 0:
        raise ValueError("Rank of input_tensor must be at least 1.")
      if ragged_tensor.is_ragged(input_tensor):
        if input_tensor.flat_values.shape.ndims > 1:
          # If the flat_values of our ragged tensor is multi-dimensional, we can
          # process it separately and our output will have the same nested
          # splits as our input.
          tokens = self.detokenize(input_tensor.flat_values)
          return input_tensor.with_flat_values(tokens)
        elif input_tensor.ragged_rank > 1:
          # Recursively process the values of the ragged tensor.
          tokens = self.detokenize(input_tensor.values)
          return input_tensor.with_values(tokens)
        else:
          return gen_sentencepiece_tokenizer.sentencepiece_detokenize_op(
              self._resource_handle, input_tensor.flat_values,
              input_tensor.row_splits, self.add_bos, self.add_eos, self.reverse)
      else:
        if input_tensor.shape.ndims > 1:
          # Convert the input tensor to ragged and process it.
          return self.detokenize(
              ragged_conversion_ops.from_tensor(input_tensor))
        else:
          tokens = self.detokenize(array_ops.stack([input_tensor]))
          return array_ops.reshape(tokens, [])

  def vocab_size(self, name=None):
    """Returns the vocabulary size.

    Args:
      name: The name argument that is passed to the op function.

    Returns:
      A scalar representing the vocabulary size.
    """
    with ops.name_scope(name, "SentencepieceTokenizerVocabSize", [self]):
      return gen_sentencepiece_tokenizer.sentencepiece_vocab_size_op(
          self._resource_handle)

  def id_to_string(self, input, name=None):  # pylint: disable=redefined-builtin
    """Converts vocabulary id into a token.

    Args:
      input: An arbitrary tensor of int32 representing the token IDs.
      name: The name argument that is passed to the op function.

    Returns:
      A tensor of string with the same shape as input.
    """
    with ops.name_scope(name, "SentencepieceTokenizerIdToString",
                        [self, input]):
      input_tensor = ragged_tensor.convert_to_tensor_or_ragged_tensor(input)
      if input_tensor.shape.ndims is None:
        raise ValueError("Rank of input_tensor must be statically known.")
      if input_tensor.shape.ndims == 0:
        strings = self.id_to_string(array_ops.stack([input_tensor]))
        return strings[0]
      if ragged_tensor.is_ragged(input_tensor):
        strings = self.id_to_string(input_tensor.flat_values)
        return input_tensor.with_flat_values(strings)
      if input_tensor.shape.ndims > 1:
        return array_ops.reshape(
            self.id_to_string(array_ops.reshape(input_tensor, [-1])),
            array_ops.shape(input_tensor))
      return gen_sentencepiece_tokenizer.sentencepiece_id_to_string_op(
          self._resource_handle, input)
