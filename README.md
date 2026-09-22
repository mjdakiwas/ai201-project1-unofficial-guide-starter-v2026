# The Unofficial Guide

Marlette Jessa Dakiwas - city_guide Corpus

---

# Unit 1

## What This Does

     The corpus I picked is city_guides. The corpus provides guidal information about multiple cities in a region: Brightwater, Corry Vale, Elder Ness, Givens Mill, Halden Bay, Kestrelford, Marchwood, Pellew Sands, and Thornby Wells. My system answers questions like geographic proximity, localized activities, and cultural recommendations.

## Chunking Strategy

**Chunk size:** 350
**Overlap:** 50

The structural format of the documents is a section for a specific context. Each section's length, including their headers, average around 350-400 characters. My strategy is to chuck by each section with the lower end of each section's average characters and account for the remaining characters that may get cut off as overlap with the neighboring chunk to ensure to retain as much relevant context as possible.

## Sample Chunks

**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```
Getting around the region with limited mobility — Overview

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.
```

**Chunk 2** — source: `guide_corry_vale.md#4` — produced by: `chunker.py::split_documents`

```
Corry Vale — What to see

The valley itself is the attraction. The footpath network is dense and well marked, and a circuit taking in three of the four villages is about nine miles with 500 metres of ascent. The chapel in the second village is 12th century and always unlocked.
```

**Chunk 3** — source: `guide_givens_mill.md#2` — produced by: `chunker.py::split_documents`

```
Givens Mill — Getting around

Everything is on one street along the river. The mill is at one end and the church at the other, eight minutes apart. The riverside path continues in both directions for as far as you want to walk.
```

**Chunk 4** — source: `guide_marchwood.md#0` — produced by: `chunker.py::split_documents`

```
Marchwood — Overview

Marchwood is the regional hub — 180,000 people, the junction everyone changes trains at, and a city most visitors pass through rather than stop in. That is a mistake, though an understandable one, since almost nothing of interest is near the station.
```

**Chunk 5** — source: `guide_regional_transport.md#5` — produced by: `chunker.py::split_documents`

```
Getting around the region — Driving

Parking is the constraint rather than driving. Both Halden Bay lots fill by
10am on summer weekends. Kestrelford's lower car park is free and involves a
steep walk up.
```

## Sample Answer

**Question:** Where is the nearest full hospital?

**Answer:** The nearest full hospital is in Brightwater. This information comes from all of the provided documents (`guide_halden_bay.md`, `guide_corry_vale.md`, `guide_kestrelford.md`, `guide_pellew_sands.md`, and `guide_marchwood.md`).

```
Sources retrieved: guide_corry_vale.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md
```

**My relevance cutoff:** 0.635

| Question | In corpus? | Best distance |
|---|---|---|
| Where in the region is suitable for an easy walk? | Yes | 0.4552 |
| Where is the nearest full hospital? | Yes | 0.2792 |
| When is the best time in the year to visit Brightwater to avoid huge crowds? | Yes | 0.3749 |
| What areas in the region can I easily travel in? | Yes | 0.5445 |
| When should I visit Kestrelford Saturday market? | Yes | 0.3317 |
| What is the capital of Mongolia? | No | 0.8874 |
| How do I change the oil in a diesel engine? | No | 0.8969 |
| Who won the 1994 World Cup? | No | 0.9026 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8293 |
| How do I write a for loop in Rust? | No | 0.8529 |

## How I Used AI

**1.** I asked Gemini to review my acceptance criteria. I asked it whether they were testable without context. It provided me suggestions on what directions I can frame myself when thinking about writing acceptance criteria.

**2.** I asked Claude (specifically Claude Code extension in VSCode) to write the chunking function based on my chunking strategy I wrote in README.md. My specific prompt was "Help me write the split_documents function based on my chunking strategy in README.md." It was thorough in verifying the function it wrote, and I didn't need to add anything else myself.

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
