# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd

from .data import data_path, split_df

__all__ = ['load']


def load():
    df = pd.read_csv(data_path('miso', 'MISO_DAMEC_2015-2017.csv'))
    return df
