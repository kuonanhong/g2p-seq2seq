# Copyright 2016 AC Technologies LLC. All Rights Reserved.
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
# ==============================================================================

""" G2P training and evaluationpackage
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.insert(1, "./g2p_seq2seq")
from g2p_seq2seq import app
from g2p_seq2seq import g2p
from g2p_seq2seq import params
from g2p_seq2seq import g2p_trainer_utils
from g2p_seq2seq import g2p_problem
from g2p_seq2seq import g2p_encoder
