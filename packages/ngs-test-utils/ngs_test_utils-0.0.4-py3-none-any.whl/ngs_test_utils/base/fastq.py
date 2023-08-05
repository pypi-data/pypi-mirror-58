"""Fastq objects."""


class FastqEntry:
    """A FASTQ entry."""

    def __init__(self, seq_id, seq, plus, quality):  # pylint: disable=redefined-builtin
        """Initialize attributes."""
        self.seq_id = seq_id
        self.seq = seq
        self.plus = plus
        self.quality = quality

    def write(self, handle):
        """Write single FASTQ entry to handle."""
        content = [self.seq_id, self.seq, self.plus, self.quality]
        handle.write("\n".join(map(str, content)) + "\n")


class FastqFile:
    """FASTQ file."""

    def __init__(self, file_name, mode="rt"):
        """Open file handle in desired mode."""
        self.file_name = file_name
        self.handle = open(file_name, mode=mode)

    def parse(self):
        """Parse FASTQ file."""
        for seq_id in self.handle:
            seq = next(self.file).rstrip("\n")
            plus = next(self.file).rstrip("\n")
            quality = next(self.file).rstrip("\n")
            yield FastqEntry(seq_id.rstrip("\n"), seq, plus, quality)

    def write(self, entries):
        """Write single FASTQ entry."""
        for entry in entries:
            entry.write(self.handle)

    def close(self):
        """Close file if it is stil open."""
        if self.handle and not self.handle.closed:
            self.handle.close()
