# Copyright 2019, The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Python utilities for the `tensor_encoding` package.

The methods in this file should not modify the TensorFlow graph.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import enum
import numpy as np
import six
import tensorflow as tf


class OrderedEnum(enum.Enum):
  """Ordered version of `Enum`.

  As opposed to `IntEnum`, This class maintains other `Enum` invariants, such as
  not being comparable to other enumerations.
  """

  def __ge__(self, other):
    if self.__class__ is other.__class__:
      return self.value >= other.value
    return NotImplemented

  def __gt__(self, other):
    if self.__class__ is other.__class__:
      return self.value > other.value
    return NotImplemented

  def __le__(self, other):
    if self.__class__ is other.__class__:
      return self.value <= other.value
    return NotImplemented

  def __lt__(self, other):
    if self.__class__ is other.__class__:
      return self.value < other.value
    return NotImplemented


def static_or_dynamic_shape(value):
  """Returns shape of the input `Tensor` or a `np.ndarray`.

  If `value` is a `np.ndarray` or a `Tensor` with statically known shape, it
  returns a Python object. Otherwise, returns result of `tf.shape(value)`.

  Args:
    value: A `Tensor` or a `np.ndarray` object.

  Returns:
    Static or dynamic shape of `value`.

  Raises:
    TypeError:
      If the input is not a `Tensor` or a `np.ndarray` object.
  """
  if tf.is_tensor(value):
    return value.shape if value.shape.is_fully_defined() else tf.shape(value)
  elif isinstance(value, np.ndarray):
    return value.shape
  else:
    raise TypeError('The provided input is not a Tensor or numpy array.')


def split_dict_py_tf(dictionary):
  """Splits dictionary based on Python and TensorFlow values.

  Args:
    dictionary: An arbitrary `dict`. Any `dict` objects in values will be
      processed recursively.

  Returns:
    A tuple `(d_py, d_tf)`, where
    d_py: A `dict` of the same structure as `dictionary`, with TensorFlow values
      removed, recursively.
    d_tf: A `dict` of the same structure as `dictionary`, with non-TensorFlow
      values removed, recursively.

  Raises:
    TypeError:
      If the input is not a `dict` object.
  """
  if not isinstance(dictionary, dict):
    raise TypeError
  d_py, d_tf = {}, {}
  for k, v in six.iteritems(dictionary):
    if isinstance(v, dict):
      d_py[k], d_tf[k] = split_dict_py_tf(v)
    else:
      if tf.is_tensor(v):
        d_tf[k] = v
      else:
        d_py[k] = v
  return d_py, d_tf


def merge_dicts(dict1, dict2):
  """Merges dictionaries of corresponding structure.

  The inputs must be dictionaries, which have the same key only if the
  corresponding values are also dictionaries, which will be processed
  recursively.

  This method is mainly to be used together with the `split_dict_py_tf` method.

  Args:
    dict1: An arbitrary `dict`.
    dict2: A `dict`. A key is in both `dict1` and `dict2` iff both of the
      corresponding values are also `dict` objects.

  Returns:
    A `dict` with values merged from the input dictionaries.

  Raises:
    TypeError:
      If either of the input arguments is not a dictionary.
    ValueError:
      If the input dictionaries do not have corresponding structure.
  """
  merged_dict = {}
  if not (isinstance(dict1, dict) and isinstance(dict2, dict)):
    raise TypeError

  for k, v in six.iteritems(dict1):
    if isinstance(v, dict):
      if not (k in dict2 and isinstance(dict2[k], dict)):
        raise ValueError('Dictionaries must have the same structure.')
      merged_dict[k] = merge_dicts(v, dict2[k])
    else:
      merged_dict[k] = v

  for k, v in six.iteritems(dict2):
    if isinstance(v, dict):
      if not (k in dict1 and isinstance(dict1[k], dict)):
        # This should have been merged in previous loop.
        raise ValueError('Dictionaries must have the same structure.')
    else:
      if k in merged_dict:
        raise ValueError('Dictionaries cannot contain the same key, unless the '
                         'corresponding values are dictionaries.')
      merged_dict[k] = v

  return merged_dict


def assert_compatible(spec, value):
  """Asserts that values are compatible with given specs.

  Args:
    spec: A structure compatible with `tf.nest`, with `tf.TensorSpec` values.
    value: A collection of values that should be compatible with `spec`. Must be
      the same structure as `spec`.

  Raises:
    TypeError: If `spec` does not contain only `tf.TensorSpec` objects.
    ValueError: If the provided `value` is not compatible with `spec`.
  """

  def validate_spec(s, v):
    if not isinstance(s, tf.TensorSpec):
      raise TypeError('Each value in `spec` must be a tf.TensorSpec.')
    return s.is_compatible_with(v)

  compatible = tf.nest.map_structure(validate_spec, spec, value)
  if not all(tf.nest.flatten(compatible)):
    raise ValueError('The provided value is not compatible with spec.')
