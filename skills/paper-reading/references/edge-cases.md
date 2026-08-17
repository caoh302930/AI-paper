# Edge cases

How to handle the situations that don't fit the default arXiv-paper happy path.

## Not on arXiv

Try in order:
- **CV venues** — `openaccess.thecvf.com` (CVPR / ICCV / ECCV / WACV).
- **ML venues** — `openreview.net` (NeurIPS / ICLR / ICML workshops).
- **Bio / chem** — `biorxiv.org`, `chemrxiv.org`.
- **Social science / econ** — `ssrn.com`, NBER working papers.
- **Theory / physics** — `arxiv.org` covers most; `inspirehep.net` for high-energy.
- **Systems** — Usenix proceedings (`usenix.org/publications/proceedings`), ACM DL.

If only a PDF is available (no HTML/LaTeX source), warn the user that equation reading may be shallower than ideal — PDF text extraction loses some math fidelity. Offer to try anyway.

## Paywalled

Tell the user. Ask for: an open-access preprint version (search `<title> arxiv` or `<title> preprint`), an institutional PDF the user can attach, or the author's webpage (often hosts a preprint).

Don't try to pirate. Don't pretend to read what you didn't read.

## Multiple papers match the title

Present 2–3 candidates with author + venue + year, ask the user to confirm. Don't guess. The wrong-paper failure mode is the most embarrassing one this skill has — a confident reading of the wrong paper looks completely correct to a reader who doesn't know the field.

## No public code

Write *"Code not released"* in the Code highlights section header and omit the section body. Don't speculate. Don't write *"the code likely…"* — it's not useful.

If the paper says "code coming soon" but the date has passed, note that in Open questions and limitations.

## Code exists but is inaccessible

Ask the user, in order of preference:

1. **Upload preferred:** *"Can you clone the repo and either zip the whole thing or just attach the key file(s) (e.g. the model definition + the loss)? Uploads beat fetches — no rate limits, no sandbox restrictions."*
2. **Fetch fallback:** *"The repo is at [URL]. I can try fetching the key files — may or may not succeed depending on rate limits. Proceed, or would you prefer to upload?"*

If the user declines both, label the section *"Inferred from paper"* and describe what the repo *likely* contains — but flag every claim. Don't silently degrade.

## Outside ML / CS

The skill works across disciplines; the tone shifts:

- **Theory papers** (TCS, math) — "Experiments and results" → "Theorems and proofs". The Method walkthrough becomes the proof structure with intuition for each lemma.
- **Empirical-science papers** (biology, physics, economics, neuroscience) — "Code highlights" → "Data + code highlights" with explicit access tier on each. Emphasize study design, controls, statistical caveats in Open questions. Equations are rarer; data dictionaries and protocol details replace them.
- **Survey papers** — the Pareto callout becomes the most important section: which parts of the survey are load-bearing for the field, which are exhaustive enumeration. The Method section becomes "Taxonomy" — explain the survey's organizing principle.
- **Position papers / opinion pieces** — Method → "Argument structure". Acknowledge that experiments may be absent.

## Short paper (workshop, tech report)

Scale output to 1500–2000 words. A 4-page paper doesn't need a 4000-word summary; the Pareto principle still applies, just compressed. Skip the layman big-picture paragraph if the method itself is a single trick.

## Paper has obvious flaws

Write the reading straight — describe the method as the paper presents it. Note the flaws in **Open questions and limitations**, with specifics (cherry-picked baselines, missing ablations, unsupported claims, statistical issues). Don't editorialize in the main body — the reader forms their own view from your evidence, not from your opinion.

If the paper has been formally retracted or the field has rejected it: say so prominently in the header, with a citation.

## Paper where the math is the contribution (not the method)

For papers whose contribution is a theorem, a bound, a hardness result, or a new mathematical formulation:

- Producer A still does the math, but the walkthrough becomes proof structure with intuition for each lemma — not a method walkthrough.
- "Experiments and results" becomes "Implications" — what does this theorem unlock, what does it close off, what conjectures does it support or refute.
- Skip the layman big-picture if it would lose the point. Replace with a 3–5 sentence "Why this theorem matters" framing.

## Paper has been superseded

If a much better follow-up exists (often the case for fast-moving fields):

- Note this in the **What matters, what doesn't** Pareto callout: ⚠️ tier with the replacement named.
- The reading is still useful as historical context — many papers are cited because they introduced an idea that subsequent work refined. Frame accordingly.
- In Open questions: note what the follow-up addressed and what's still open.
