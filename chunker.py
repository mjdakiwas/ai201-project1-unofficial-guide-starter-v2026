"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


_HEADING = re.compile(r"^##\s+(.*)$", re.M)
_TITLE = re.compile(r"^#\s+(.*)$", re.M)
_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


def _document_title(text: str) -> str:
    """The `# Heading` a guide opens with, e.g. "Brightwater"."""
    match = _TITLE.match(text.lstrip())
    return match.group(1).strip() if match else ""


def _sections(text: str) -> list[tuple[str, str]]:
    """
    Break one guide into (heading, body) pairs at its `##` headings.

    Anything before the first heading — the title line and the paragraph of
    scene-setting most guides open with — comes back as "Overview" rather than
    being dropped. That paragraph carries population and history, which some
    questions ask about.
    """
    headings = list(_HEADING.finditer(text))
    sections: list[tuple[str, str]] = []

    preamble = text[: headings[0].start()] if headings else text
    preamble = _TITLE.sub("", preamble, count=1).strip()
    if preamble:
        sections.append(("Overview", preamble))

    for i, heading in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        body = text[heading.end() : end].strip()
        if body:
            sections.append((heading.group(1).strip(), body))

    return sections


def _overlap_tail(window: str, overlap: int) -> str:
    """
    The last `overlap` characters of a window, trimmed forward to a whole word.

    This is what gets repeated at the start of the next window, so a sentence
    the section split landed on top of still reads as continuous somewhere.
    """
    if overlap <= 0 or len(window) <= overlap:
        return ""
    tail = window[-overlap:]
    space = tail.find(" ")
    return tail[space + 1 :].strip() if space != -1 else tail.strip()


def _windows(body: str, chunk_size: int, overlap: int) -> list[str]:
    """
    Cut one over-long section down to windows of at most `chunk_size`.

    Most sections in this corpus are already under the limit and come straight
    back out whole. The rest get packed sentence by sentence, so a window ends
    on a full stop instead of mid-clause.
    """
    if len(body) <= chunk_size:
        return [body]

    sentences = [s.strip() for s in _SENTENCE_END.split(body) if s.strip()]
    windows: list[str] = []
    current = ""

    for sentence in sentences:
        # One sentence longer than the whole window can't be packed. Rare, but
        # without this the loop would never place it.
        if len(sentence) > chunk_size:
            if current:
                windows.append(current)
                current = ""
            step = chunk_size - overlap
            for start in range(0, len(sentence), step):
                windows.append(sentence[start : start + chunk_size])
            continue

        candidate = f"{current} {sentence}".strip()
        if current and len(candidate) > chunk_size:
            windows.append(current)
            current = f"{_overlap_tail(current, overlap)} {sentence}".strip()
        else:
            current = candidate

    if current:
        windows.append(current)

    return windows


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split each guide at its `##` headings, one chunk per section.

    The corpus is 14 city guides, every one of them a `# Title` followed by
    `##` sections that each answer a different question — getting there,
    eating, when to go. Sections run 173 to 708 characters, median 294, so the
    starter's 800-character window was routinely gluing two unrelated topics
    into one chunk and cutting a third in half. Splitting on the headings the
    documents already have keeps one topic per chunk.

    CHUNK_SIZE (350) is the ceiling on a section's own text, picked at the low
    end of the section average. About a quarter of sections run past it and get
    packed into sentence-bounded windows with CHUNK_OVERLAP (50) characters
    carried across each boundary.

    Every chunk is prefixed with "Title — Heading". Six guides describe the
    same handful of topics, so a bare paragraph about bus routes is ambiguous
    about which town it belongs to; the prefix is not counted against
    CHUNK_SIZE because it is context, not content.
    """
    chunk_size = config.CHUNK_SIZE
    overlap = config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        title = _document_title(doc.text)
        index = 0

        for heading, body in _sections(doc.text):
            prefix = f"{title} — {heading}" if title else heading

            for window in _windows(body, chunk_size, overlap):
                chunks.append(
                    Chunk(
                        text=f"{prefix}\n\n{window}",
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::split_documents",
                    )
                )
                index += 1

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
