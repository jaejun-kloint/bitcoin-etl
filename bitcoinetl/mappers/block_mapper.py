# MIT License
#
# Copyright (c) 2018 Omidiora Samuel, samparsky@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from bitcoinetl.domain.block import BtcBlock
from bitcoinetl.mappers.transaction_mapper import BtcTransactionMapper
from blockchainetl.utils import hex_to_dec, to_normalized_address


class BtcBlockMapper(object):
    def __init__(self, transaction_mapper=None):
        if transaction_mapper is None:
            self.transaction_mapper = BtcTransactionMapper()
        else:
            self.transaction_mapper = transaction_mapper

            'size',
    'stripped_size',
    'weight',
    'height',
    'version',
    'version_hex',
    'merkle_root',
    'time',
    'median_time',
    'nonce',
    'bits',
    'difficulty',
    'chain_work',
    'previous_block_hash',
    'next_block_hash',
    'tx',
    'transaction_count',
    'hash',
    'confirmations',
    def json_dict_to_block(self, json_dict):
        block = BtcBlock()
        block.hash = json_dict.get('hash')
        block.confirmations = json_dict.get('confirmations')
        block.size = json_dict.get('size')
        block.stripped_size = json_dict.get('strippedsize')
        block.weight = json_dict.get('weight')
        block.height = json_dict.get('height')
        block.version = json_dict.get('version')
        block.version_hex = json_dict.get('versionHex')
        block.merkle_root = json_dict.get('merkleroot')
        block.time = json_dict.get('time')
        block.median_time = json_dict.get('mediantime')
        block.nonce = json_dict.get('nonce')
        block.bits = json_dict.get('bits')
        block.difficulty = json_dict.get('difficulty')
        block.chain_work = json_dict.get('chainwork')
        block.previous_block_hash = json_dict.get('previousblockhash')
        block.next_block_hash = json_dict.get('nextblockhash')

        if 'tx' in json_dict:
            block.transactions = [
                self.transaction_mapper.json_dict_to_transaction(tx) for tx in json_dict['tx']
                if isinstance(tx, dict)
            ]

            block.transaction_count = len(json_dict['tx'])

        return block

    def block_to_dict(self, block):
        return {
            'type': 'block',
            'hash': block.hash,
            'size': block.size,
            'stripped_size': block.stripped_size,
            'weight': block.weight,
            'height': block.height,
            'version': block.version,
            'version_hex': block.version_hex,
            'merkle_root': block.merkle_root,
            'time': block.time,
            'median_time': block.median_time,
            'nonce': block.nonce,
            'bits': block.bits,
            'difficulty': block.difficulty,
            'chain_work': block.chain_work,
            'previous_block_hash': block.previous_block_hash,
            'next_block_hash': block.next_block_hash,
            'confirmations': block.confirmations,
        }
