from __future__ import absolute_import, division, print_function

import json
import os
import sys
from argparse import ArgumentParser

import numpy as np

from loguru import logger
from marisa_trie import Trie
from embed_compress import EmbeddingCompressor

from gumbelcodes.utils.matutils import matrix_bincount, bitpack_uint8_matrix
from gumbelcodes.utils.fileutils import create_file_path

from zipfile import ZipFile


class PipelineTemplate(object):

    def __init__(self,
                 source_path=None,
                 dimension=None,
                 target_path=None,
                 dictionary_path=None,
                 trie_path=None,
                 codebook_prefix=None,
                 trimmed_prefix='trimmed_',
                 codebook_suffix='.codebook.npy',
                 codes_suffix='.codes',
                 logging=True):
        self.source_path = source_path
        self.dimension = dimension
        self.target_path = target_path
        self.dictionary_path = dictionary_path
        self.trie_path = trie_path
        self.codebook_prefix = codebook_prefix
        self.trimmed_prefix = trimmed_prefix
        self.codebook_suffix = codebook_suffix
        self.codes_suffix = codes_suffix
        self.logging = logging


class Pipeline(PipelineTemplate):

    def __init__(self, **kwargs):
        super(Pipeline, self).__init__(**kwargs)
        self.codebook_path = self.codebook_prefix + self.codebook_suffix
        self.codes_path = self.codebook_prefix + self.codes_suffix
        if self.logging:
            logger.debug("Source: {0} \n Target: {1}".format(
                self.source_path, self.target_path))

    def get_words(self, generate_trie=True, generate_dictionary=True):
        words = [x.strip().split()[0]
                 for x in list(open(self.source_path, encoding="utf-8"))]

        if generate_dictionary:
            dictionary = {key: idx for idx, key in enumerate(words)}
            with open(self.dictionary_path, 'w+') as f:
                json.dump(dictionary, f)

        if generate_trie:
            if generate_dictionary:
                del dictionary
            trie = Trie(words)
            trie.save(self.trie_path)

        return self

    def get_embeddings(self):
        lines = list(open(self.source_path, encoding="utf-8"))
        embed_matrix = np.zeros((len(lines), self.dimension), dtype='float32')
        if self.logging:
            logger.debug("Embedding shape: {0}".format(embed_matrix.shape))
        for i, line in enumerate(lines):
            parts = line.strip().split()
            try:
                vec = np.array(parts[1:], dtype='float32')
                embed_matrix[i] = vec
            except:
                if self.logging:
                    logger.debug(line)
                    logger.debug("Invalid embedding at line {0}".format(i))
        np.save(self.target_path, embed_matrix)
        return self

    def train(self):
        matrix = np.load(self.target_path)
        compressor = EmbeddingCompressor(32, 16, self.codebook_prefix)
        compressor.train(matrix)
        distance = compressor.evaluate(matrix)
        if self.logging:
            logger.debug("Mean euclidean distance:", distance)
        compressor.export(matrix, self.codebook_prefix)
        return self

    def trim(self):
        codes = np.loadtxt(self.codes_path)
        codes = codes.astype(dtype=np.int64)
        max_value = codes.max()
        min_value = codes.min()

        assert(max_value < len(codes[0]))

        max_rep, codes = matrix_bincount(codes)

        try:
            assert(max_value < 16)
        except:
            if self.logging:
                logger.debug("{0} : min_value = {1}, max_value = {2}".format(
                    self.codebook_prefix, min_value, max_value))
            return

        try:
            assert(max_rep < 16)
        except:
            codes[codes > 15] = 15
            if self.logging:
                logger.debug(
                    "{0} : max_rep = {1} - rounded down to 15".format(self.codebook_prefix, max_rep))

        codes = bitpack_uint8_matrix(codes)

        np.save(create_file_path(self.codes_path, self.trimmed_prefix), codes)

        codebook = np.load(self.codebook_path)
        array_length = max_value + 1
        codebook = codebook[0:array_length]
        codebook_even = np.array(codebook[::2], dtype=np.float32)
        codebook_odd = np.array(codebook[1::2], dtype=np.float32)
        codebook = np.array([codebook_even, codebook_odd], dtype=np.float32)

        np.save(create_file_path(self.codebook_path,
                                 self.trimmed_prefix), codebook)
        return self

    def compress(self, zip_suffix='embedding.zip', npz_suffix='vectors.npz'):
        codes = create_file_path(self.codes_path, self.trimmed_prefix)
        if not codes.endswith('.npy'):
            codes += '.npy'
        codebook = create_file_path(self.codebook_path, self.trimmed_prefix)
        if not codebook.endswith('.npy'):
            codebook += '.npy'

        codes_arr = np.load(codes)
        codebook_arr = np.load(codebook)
        zip_target_path = self.codebook_prefix + zip_suffix
        npz_target_path = self.codebook_prefix + npz_suffix
        np.savez_compressed(npz_target_path, codes=codes_arr, codebook=codebook_arr)
        with ZipFile(zip_target_path, 'w') as zipObject:
            zipObject.write(npz_target_path)
            zipObject.write(self.trie_path)
        return self


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        settings = json.load(f)
    for entry in settings:
        pipe = Pipeline(**entry)
        # pipe\
        #     .get_words(generate_dictionary=False)\
        #     .get_embeddings()\
        #     .train()\
        #     .trim()\
        #     .compress()
        pipe\
            .trim()\
            .compress()
