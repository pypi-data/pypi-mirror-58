"""Test utilities for FASTQ files."""
import numpy
from ngs_test_utils.base.fastq import FastqEntry


class FastqTestCaseMixin:
    """Mixin for manipulation of FASTA files in tests."""

    @staticmethod
    def make_quality_scores(size, min_chr=33, max_chr=74, rnd_seed=None):
        """Make random quality scores of length `size`."""
        if rnd_seed:
            numpy.random.seed(rnd_seed)
        scores = [chr(i) for i in range(min_chr, max_chr + 1)]
        return "".join(numpy.random.choice(scores, size))

    def make_sequence_id(self, rnd_seed=None):
        """Make sequence ID."""
        if rnd_seed:
            numpy.random.seed(rnd_seed)
        return "random_sequence_{}".format(numpy.random.randint(0, 10 ** 4))

    def make_fastq_entry(self, seq, seq_id=None, plus="+", quality=None, rnd_seed=None):
        """Make FASTQ entry."""
        if seq_id is None:
            seq_id = self.make_sequence_id(rnd_seed)

        if quality is None:
            quality = self.make_quality_scores(len(seq), rnd_seed=rnd_seed)

        return FastqEntry(seq_id=seq_id, seq=seq, plus=plus, quality=quality)

    def make_fastq(self, entries):
        """Make FASTQ file from entries."""
        filename = self.get_filename(extension="fastq")

        with open(filename, "wt") as ofile:
            for entry in entries:
                entry.write(ofile)

        return filename
