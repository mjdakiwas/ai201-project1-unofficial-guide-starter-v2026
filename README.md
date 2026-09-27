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
| 1. Retrieved chunk contains the answer | 4 of 5 | 1/5 | 1/5 | 1/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks contains enough complete context to answer the question without having to rely on non-retrieved text | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 5. Answer rely on two or more source materials | 5 of 5 | 2/5 | 2/5 | 3/5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
### Criterion 1
* **File & Function:** `run_eval.py` -> `run_once()`
     * I ran `python run_eval.py --label before` to produced `results\run_2026-09-25_1918_before.md`, which evaluated whether the question failed or pass and the output for each questions for three different runs. I used the table that displays whether the question passed or failed to determine whether the question was answered or not by my system.
* **Questions:** Run 1
     * "Where in the region is suitable for an easy walk?"
          * **Retrieved Output:** 
               ```
               Based on the provided documents, easy walks in the region include the Brightwater river path, which runs four miles upstream on a made, flat surface, and the Kestrelford trackbed, which offers an easy gradient and good surface along an old railway line. Additionally, Thornby Wells has flat, formal gardens and level streets suitable for walking. 

               Source: `guide_walking.md`
               ```
     * "Where is the nearest full hospital?"
          * **Retrieved Output:** 
               ```
               The nearest full hospital is in Brightwater, as stated in `guide_halden_bay.md`, `guide_corry_vale.md`, `guide_kestrelford.md`, `guide_pellew_sands.md`, and `guide_marchwood.md`.
               ```
     * "When is the best time in the year to visit Brightwater to avoid huge crowds?"
          * **Retrieved Output:** 
               ```
               Late May is arguably the best week of the year in Brightwater because the days are long, everything is running, and the students are gone (*guide_seasons.md*). Additionally, June and July/August (before September when the term starts) are also mentioned as times when Brightwater goes quiet to the point of dullness with the university empty (*guide_seasons.md*).
               ```
     * "What areas in the region can I easily travel in?"
          * **Retrieved Output:** 
               ```
               Based on the documents, the easiest towns in the region for getting around with limited mobility are Thornby Wells (which is flat, compact, and level throughout the pump room and gardens) and Marchwood (which has a modern tram network with level boarding, and step-free city museum and covered market). Brightwater is also level along the river and through the centre, with a step-free mill museum. 

               Source: `guide_accessibility.md`
               ```
     * "When should I visit Kestrelford Saturday market?"
          * **Retrieved Output:**
               ```
               According to `guide_seasons.md`, the Kestrelford Saturday market builds back to full size through April, and `guide_eating.md` notes that the market is the region's best (though much reduced from November to February).
               ```

### Criterion 2
* **File & Function:** `run_eval.py` -> `run_once()`
     * I ran `python run_eval.py --label before` to produced `results\run_2026-09-25_1918_before.md`, which evaluated whether the question failed or pass and the output for each questions for three different runs. I evaluated the output for each questions' Run 2 whether it cites at least one source document.
* **Questions:** Run 2
     * "Where in the region is suitable for an easy walk?"
          * **Retrieved Output:** 
               ```
               Based on the provided documents, suitable locations for an easy walk include:
               - The **Brightwater river path**, which runs four miles upstream on a flat, made surface.
               - The **Kestrelford trackbed**, which follows a closed railway line for six miles on an easy gradient.
               - **Thornby Wells**, which features flat, formal gardens and level streets.

               Source: `guide_walking.md`
               ```
     * "Where is the nearest full hospital?"
          * **Retrieved Output:** 
               ```
               The nearest full hospital is in Brightwater, according to all the provided documents (`guide_halden_bay.md`, `guide_corry_vale.md`, `guide_kestrelford.md`, `guide_pellew_sands.md`, and `guide_marchwood.md`).
               ```
     * "When is the best time in the year to visit Brightwater to avoid huge crowds?"
          * **Retrieved Output:** 
               ```
               Late May is arguably the best week of the year in Brightwater, featuring long days, everything running, and the students gone (`guide_seasons.md`). Additionally, September is described as a sweet spot where everything is still open and it is quiet, before it gets busy in late September when term starts (`guide_seasons.md`).
               ```
     * "What areas in the region can I easily travel in?"
          * **Retrieved Output:** 
               ```
               Based on `guide_accessibility.md`, the easiest town in the region for limited mobility is Thornby Wells, as it is flat, compact, level throughout the pump room and gardens, and everything is within three minutes of everything else. Additionally, Marchwood has a modern tram network with level boarding on all four lines, and its city museum and covered market are step-free. Brightwater is also level along the river and through the centre, with a step-free mill museum.
               ```
     * "When should I visit Kestrelford Saturday market?"
          * **Retrieved Output:**
               ```
               According to `guide_seasons.md`, the Kestrelford Saturday market builds back to full size through April, and `guide_eating.md` notes that the market is the region's best (though much reduced from November to February).
               ```

### Criterion 3
* **File & Function:** `run_eval.py` -> `check_out_of_scope()`
     * I ran `python run_eval.py --label before` to produced `results\run_2026-09-25_1918_before.md`, which checks whether the question is in or out of scope. I used the table it produced to determine whether an out of scope question was refused. I ran `python app.py ask "[question]"` to get the system's explicit output for each out of scope question.
* **Questions:** Run 1
     * "What is the capital of Mongolia?"
          * **Retrieved Output:** `I don't have enough information about that.`
     * "How do I change the oil in a diesel engine?"
          * **Retrieved Output:** `I don't have enough information about that.`
     * "Who won the 1994 World Cup?"
          * **Retrieved Output:** `I don't have enough information about that.`
     * "What is the recommended dosage of ibuprofen for a headache?"
          * **Retrieved Output:** `I don't have enough information about that.`
     * "How do I write a for loop in Rust?"
          * **Retrieved Output:** `I don't have enough information about that.`

### Criterion 4
* **File & Function:** `app.py` -> `ask_pipeline()`
     * I explicitly ran `app.ask_pipeline("[question]")` to retrieve the sample chunks for each questions and evaluate whether the first chunk has enough complete context to answer the question without unretrieved context.
* **Questions:** Run 1
     * "Where in the region is suitable for an easy walk?"
          * **Retrieved Chunk:** [from guide_regional_transport.md]\ncar park is free and involves a\nsteep walk up.\n\n## Walking and cycling\n\nThe river path from Brightwater runs four miles upstream on a good surface. The\nold railway trackbed from Kestrelford runs six miles on an easy gradient and is\nthe best walking in the region for the effort involved. The coastal path from\nHalden Bay is more serious — exposed, and closed in high wind.\n\nCycling is pleasant on the river path and the trackbed, and unpleasant on Mill\nRoad and the coast road, neither of which has a shoulder.
     * "Where is the nearest full hospital?"
          * **Retrieved Chunk:** [from guide_halden_bay.md]\nn the centre and\npatchy on the outskirts. The nearest full hospital is in Brightwater; there is\na minor injuries unit locally with limited hours.
     * "When is the best time in the year to visit Brightwater to avoid huge crowds?"
          * **Retrieved Chunk:** [from guide_seasons.md]\n# When to visit the region\n\n## Spring, March to May\n\nDays lengthen quickly and businesses that closed for winter reopen through\nMarch and April. By May everything is open and the weather is reliable enough\nto plan around. Late May is arguably the best week of the year in Brightwater —\nlong days, everything running, and the students gone.\n\nThe Kestrelford Saturday market builds back to full size through April.\n\n## Summer, June to August\n\nJune is excellent everywhere. July and August split: Halden Bay becomes very\nbusy and the parking problem dominates, Kestrelford fills with walkers, and\nBrightwater goes quiet to the point of dullness with the university empty.\n\nIf you are going to Halden Bay in August, arrive before 10am or plan to use the\noverflow lot.\n\n## Autumn, September to November\n\nS
     * "What areas in the region can I easily travel in?"
          * **Retrieved Chunk:** [from guide_accessibility.md]\n# Getting around the region with limited mobility\n\nAn honest assessment rather than a promotional one. Some of these places are\ndifficult and it is better to know in advance.\n\n## Straightforward\n\n**Thornby Wells** is the easiest town in the region. It is flat, compact, and\neverything is within three minutes of everything else. Parking is free for two\nhours anywhere in town and the station is central. The pump room and gardens\nare level throughout.\n\n**Marchwood** has a modern tram network with level boarding on all four lines,\nrunning every 8 minutes on weekdays. The city museum and covered market are both\nstep-free. The distances between districts are the main consideration.\n\n**Brightwater** is level along the river and through the centre. The mill museum\nis step-free. The station is a 15-
     * "When should I visit Kestrelford Saturday market?"
          * **Retrieved Chunk:** [from guide_eating.md]\nurs\n\nThis catches visitors out more than anything else. Outside Marchwood, kitchens\nacross the region stop serving at 9pm and often earlier. Kestrelford's pubs\nserve 12 to 2 and 6 to 8:30 and there is nowhere to eat at all outside those\nwindows. Elder Ness has one pub, closed Mondays.\n\nSunday evening is the hardest meal to find anywhere except Marchwood and\nThornby Wells.\n\n## Markets\n\nKestrelford's Saturday market has run since the 1400s and is the region's best,\nthough much reduced from November to February. Brightwater's Tuesday market\nsets up at 7am in the square and is finished by 1pm. Marchwood's covered market\nhas operated since 1863, runs six days a week, and is at its best on a weekday\nmorning.\n\n## Local specifics\n\nHalden Bay's seafood is genuinely fresh — the two harbour restauran

### Criterion 5
* **File & Function:** `run_eval.py` -> `run_once()`
     * I ran `python run_eval.py --label before` to produced `results\run_2026-09-25_1918_before.md`, which has the output for each questions. I used the output to evaluate whether the answer referenced two or more material sources.
* **Questions:** Run 3
     * "Where in the region is suitable for an easy walk?"
          * **Retrieved Output:** 
               ```
               Based on the documents, the following places are suitable for an easy walk:

               * The **Brightwater river path** runs four miles upstream to a weir on a made, flat surface (also mentioned as a good surface in `guide_regional_transport.md`). 
               * The **Kestrelford trackbed** runs six miles along a closed railway line with an easy gradient and a good surface. 
               * **Thornby Wells** has flat, formal gardens and level streets.

               *(Sources: `guide_walking.md` and `guide_regional_transport.md`)*
               ```
     * "Where is the nearest full hospital?"
          * **Retrieved Output:** 
               ```
               The nearest full hospital is in Brightwater. This comes from `guide_halden_bay.md`, `guide_corry_vale.md`, `guide_kestrelford.md`, `guide_pellew_sands.md`, and `guide_marchwood.md`.
               ```
     * "When is the best time in the year to visit Brightwater to avoid huge crowds?"
          * **Retrieved Output:** 
               ```
               Late May is arguably the best week of the year in Brightwater, as it features long days, everything running, and the students gone (guide_seasons.md). Additionally, July and August are times when Brightwater goes quiet to the point of dullness with the university empty (guide_seasons.md).
               ```
     * "What areas in the region can I easily travel in?"
          * **Retrieved Output:** 
               ```
               Based on `guide_accessibility.md`, the easiest town in the region is **Thornby Wells**, which is flat, compact, and level throughout the pump room and gardens. 

               Additionally, **Marchwood** has a modern tram network with level boarding on all four lines, and its city museum and covered market are both step-free. **Brightwater** is also level along the river and through the centre, with a step-free mill museum.
               ```
     * "When should I visit Kestrelford Saturday market?"
          * **Retrieved Output:**
               ```
               According to `guide_seasons.md`, the Kestrelford Saturday market builds back to full size through April, and `guide_eating.md` notes that the market is the region's best (though much reduced from November to February).
               ```

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
