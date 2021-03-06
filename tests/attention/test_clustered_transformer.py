#
# Copyright (c) 2020 Idiap Research Institute, http://www.idiap.ch/
# Written by Angelos Katharopoulos <angelos.katharopoulos@idiap.ch>,
# Apoorv Vyas <avyas@idiap.ch>
#


import unittest

import torch

from fast_transformers.attention import AttentionLayer, ClusteredAttention
from fast_transformers.masking import FullMask
from fast_transformers.transformers import TransformerEncoderLayer, TransformerEncoder


class TestTransformerEncoder(unittest.TestCase):
    def test_full_attention_forward(self):
        d_model = 128
        n_heads = 4
        transformer = TransformerEncoder([
            TransformerEncoderLayer(
                AttentionLayer(
                    ClusteredAttention(
                        clusters = 10
                    ),
                    d_model,
                    n_heads
                ),
                d_model,
                n_heads
            )
            for i in range(6)
        ])

        x = transformer(torch.rand(100, 20, d_model))
        self.assertEqual(x.shape, (100, 20, d_model))


if __name__ == "__main__":
    unittest.main()
