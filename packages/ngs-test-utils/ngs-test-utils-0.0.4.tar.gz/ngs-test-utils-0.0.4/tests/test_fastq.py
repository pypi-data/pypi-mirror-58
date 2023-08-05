from ngs_test_utils import testcase


class TestFastqTestCase(testcase.NgsTestCase):
    def test_make_quality_scores(self):
        seq = self.make_quality_scores(10, rnd_seed=42)
        self.assertEqual(len(seq), 10)
        self.assertEqual(seq, "G=/(5G37++")

    def test_make_sequence_id(self):
        seq = self.make_sequence_id()
        self.assertTrue(seq.startswith("random_sequence_"))
        seq = self.make_sequence_id(rnd_seed=42)
        self.assertEqual(seq, "random_sequence_7270")

    def test_make_fastq_entry(self):
        entry = self.make_fastq_entry(seq="ACTG", rnd_seed=2)
        self.assertEqual(entry.seq_id, "random_sequence_7336")
        self.assertEqual(entry.seq, "ACTG")
        self.assertEqual(entry.plus, "+")
        self.assertEqual(entry.quality, "I0)7")

    def test_make_fastq_file(self):
        entry = self.make_fastq_entry(seq="ACTG", rnd_seed=2)
        filename = self.make_fastq([entry])
        self.assertEqual(self.tsv_to_list(filename), [["random_sequence_7336"], ["ACTG"], ["+"], ["I0)7"]])
