"""Test utilities for BED files."""
import pybedtools as pbt


class BedTestCaseMixin:
    """Mixin for manipulation of GTF files in tests."""

    def make_bed_interval(self, seqname="chr1", start=1, end=1000, name=".", score=0, strand="+"):
        """Create BED interval."""
        return pbt.create_interval_from_list([seqname, start, end, name, score, strand])

    def make_bed(self, intervals):
        """Create GTF file from a list of intervals.

        Data should be a list of pbt.Interval objects or dicts or lists.
        """
        fname = self.get_filename(extension="bed")

        if isinstance(intervals[0], list):
            intervals = [self.make_bed_interval(*interval) for interval in intervals]
        if isinstance(intervals[0], dict):
            intervals = [self.make_bed_interval(**interval) for interval in intervals]

        pbt.BedTool(interval for interval in intervals).saveas(fname)

        return fname
