#
# Copyright © 2024 Intel Corporation
# SPDX-License-Identifier: Apache 2.0
#

from dataclasses import dataclass
from functools import lru_cache
from typing import List, Any, Sequence
import ctypes


@dataclass(frozen=True)
class SupportedOp:
    """A class for supported runtime OPs in the NPU.

    Attrs:
        name (str): Operation name
        inputs (int): Number of inputs
        parameters (Sequence[Any]): Optional parameters type.
    """

    name: str
    inputs: int
    parameters: Sequence[Any] = ()


@lru_cache(maxsize=None)
def get_supported_ops() -> List[SupportedOp]:
    """Generate a list fo supported operations.

    Returns:
        List[SupportedOp]: list fo supported NPU operations
    """
    supported_ops = [
        SupportedOp(name="matmul", inputs=2),
        SupportedOp(name="eltwise_add", inputs=2),
        SupportedOp(name="eltwise_mul", inputs=2),
        SupportedOp(name="eltwise_div", inputs=2),
        SupportedOp(name="abs_act", inputs=1),
        SupportedOp(name="acos_act", inputs=1),
        SupportedOp(name="asin_act", inputs=1),
        SupportedOp(name="atan_act", inputs=1),
        SupportedOp(name="ceiling", inputs=1),
        SupportedOp(
            name="clamp", inputs=1, parameters=[ctypes.c_float, ctypes.c_float]
        ),
        SupportedOp(name="cos_act", inputs=1),
        SupportedOp(name="cosh_act", inputs=1),
        SupportedOp(name="erf_act", inputs=1),
        SupportedOp(name="elu", inputs=1, parameters=[ctypes.c_float]),
        SupportedOp(name="exp_act", inputs=1),
        SupportedOp(name="floor_act", inputs=1),
        SupportedOp(name="grn", inputs=1, parameters=[ctypes.c_float]),
        SupportedOp(name="gelu", inputs=1),
        SupportedOp(name="log_act", inputs=1),
        SupportedOp(name="negative", inputs=1),
        SupportedOp(name="relu", inputs=1),
        SupportedOp(name="sigmoid", inputs=1),
        SupportedOp(name="sign", inputs=1),
        SupportedOp(name="sin_act", inputs=1),
        SupportedOp(name="sinh_act", inputs=1),
        SupportedOp(name="sqrt_act", inputs=1),
        SupportedOp(name="tan_act", inputs=1),
        SupportedOp(name="tanh_act", inputs=1),
        SupportedOp(name="acosh_act", inputs=1),
        SupportedOp(name="asinh_act", inputs=1),
        SupportedOp(name="atanh_act", inputs=1),
        SupportedOp(name="hswish", inputs=1),
        SupportedOp(name="mish", inputs=1),
        SupportedOp(name="softplus", inputs=1),
        SupportedOp(name="hsigmoid", inputs=1),
        SupportedOp(name="round_act", inputs=1),
        SupportedOp(name="softsign", inputs=1),
        SupportedOp(name="softmax", inputs=1),
        SupportedOp(name="swish", inputs=1),
        SupportedOp(name="convert_to_fp16", inputs=1),
        SupportedOp(
            name="scaled_dot_product_attention",
            inputs=4,
            parameters=[ctypes.c_bool],
        ),
    ]
    return supported_ops
