import argparse
import collections
import os
import random
import json
from copy import deepcopy

import ConfigSpace
import numpy as np


# from tabular_benchmarks import FCNetProteinStructureBenchmark, FCNetSliceLocalizationBenchmark,\
#     FCNetNavalPropulsionBenchmark, FCNetParkinsonsTelemonitoringBenchmark
from tabular_benchmarks import NASCifar10A, NASCifar10B