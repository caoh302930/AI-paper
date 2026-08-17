# Orchestration — Producer A / Producer B / QC prompts

The default `/paper-reading` workflow runs as **lead + 2 producers + 1 QC**. Each producer works in an isolated context window from a non-overlapping lane; QC sees both outputs simultaneously (not one-then-the-other) and merges them into the final artifact.

Pattern from Anthropic's [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — lead + parallel subagents with isolated context — combined with verification-before-completion (evidence before claims).

## Why two producers + QC

- A single agent reading a paper end-to-end tends to drift toward what's easiest to summarize (abstract, intro, conclusion) and short-change what's hardest (the math). Splitting Math & Method from Context & Code keeps each producer focused.
- QC's job is *not* to summarize the producers. It's to verify against the source paper, fix divergences, enforce format, and write the merged artifact.
- Lane independence + simultaneous QC review prevents anchoring: QC doesn't trust either producer; it re-checks against the paper.

## Lead orchestration recipe

After resolving the paper (Step 1) and gathering context (Step 2):

1. **Dispatch Producer A and Producer B in parallel** — single message, two `Task` calls. Each prompt must be self-contained (the subagent has no conversation history): paper title, link/ID, output format expectations, lane scope, length cap, an explicit "do not stray into the other lane" instruction, and the verbatim contents of `references/math-rendering.md` appended for math formatting.
2. **When both return**, dispatch QC with both outputs verbatim + the source paper link/ID + this skill's output-template reference + a pointer back to the paper so QC can re-verify.
3. **Act on QC feedback.** Critical issues → re-dispatch the relevant producer with QC's specific feedback, then loop QC once more. Important + Minor → log to a `<!-- QC notes -->` block at the tail of the artifact.
4. **The lead writes the final file.** Do not let QC write directly — single point of control for path / git / hooks.

## Producer A — Math & Method

```
You are Producer A on a deep-paper-reading task. Your scope:
- Sections 3–4 of the paper (method, experiments, ablations) and any appendix the method points at.
- Reproduce equations precisely; explain symbols in words BEFORE or right after the math.
- Identify load-bearing prior work the paper assumes you already know but doesn't re-explain.
  For each: read just the cited paper's abstract + intro, then write 3–5 sentences on the
  SPECIFIC PART this paper is leveraging — not a general summary. Be selective: 2–5 briefs total.
- Name actual losses, blocks, datasets, hyperparameters, numbers. Specifics over generalities.

Stay strictly inside Sections 3–4 + appendix. Do NOT cover abstract, intro, related-work,
conclusion, code, or framing — Producer B handles those.

Output format: a single markdown chunk with these subsections (in this order):
- "Method — big picture (layman version)" — 5–8 sentences, no symbols, no jargon.
- "Method — walkthrough" — motivate each step ("we want X, but Y, so Z"); introduce equations
  with symbol meanings in words; insert prior-work briefs INLINE exactly where the reader
  would be asking "wait, what's that?".
- "Experiments and results" — brief. Nuance the headline (key ablations, surprises, regimes
  where the method struggled).

Math formatting: follow the rules in `references/math-rendering.md` (the lead will include its content with this prompt).

Length cap: 1500–2200 words for this chunk.
```

## Producer B — Context & Code

```
You are Producer B on a deep-paper-reading task. Your scope:
- Abstract, introduction, related work, conclusion, broader-impact section.
- The paper's code repository if accessible — actually read README + the file(s) implementing
  the contribution. Look for paper↔code MISMATCHES (papers simplify; code is ground truth).
  Label the code section with one of: "Reviewed" (you read the source), "Inferred from paper"
  (linked but couldn't fetch), or "User-provided" (user uploaded the repo).
- Framing, impact, what's been deprecated/superseded by later work, the broader landscape —
  strictly bounded; do NOT drift into a survey.

Stay outside Sections 3–4 method content. Producer A is handling all the math.

Output format: a single markdown chunk with these subsections (in this order):
- "Header" — title, authors, venue, organizations, arXiv link, code link, project page link.
- "TL;DR and contributions" — 2–3 plain-language sentences; bullet contributions; named
  baselines; datasets; headline numbers (specific deltas, not "improves performance").
- "What matters, what doesn't" — Pareto callout. 3–6 bullets with explicit labels:
  🎯 Core idea (read carefully) / 🔧 Useful in practice / 📎 Nice to know /
  ⚠️ Deprecated or superseded (name the replacement) / 🔕 Skippable.
  Only include categories that apply. A reader should absorb this in 30 seconds.
- "Context and prerequisites" — connected prose teaching each load-bearing concept;
  NOT a list of definitions. Pick only concepts load-bearing for the Method.
- "Challenges in the field — and what this work addresses" — 2–3 challenges (4 if genuinely
  distinct). For each: WHY the challenge is hard, then WHY this approach is the right shape.
  Close with one "what this work does NOT address".
- "Code highlights" — only if a repo exists; label the access tier explicitly. Identify the
  entry point, key file(s), non-obvious choices (custom kernels, unusual data pipeline,
  hyperparameter deltas vs paper). Flag any paper↔code mismatches you find.
- "Open questions and limitations" — 2–4 bullets.

Math formatting: same rules as Producer A.

Length cap: 1200–1800 words for this chunk.
```

## QC

```
You are QC on a deep-paper-reading task. Two producers wrote separate chunks of a paper
reading (Math & Method; Context & Code). Your job:

1. Re-read the source paper (link/ID provided) — do NOT just trust the producers.
2. Verify factual claims against the paper. If a producer cited a number, check it.
3. Verify equation correctness — symbol definitions, indexing, summation bounds.
4. Verify the code section's access-tier label is honest (Reviewed / Inferred / User-provided).
5. Check the depth/compactness balance — the vital 20% should get ~80% of the space.
6. Check format: math delimiters per the rules, headline numbers specific, prior-work briefs
   inline (not appended), Method opens with the jargon-free big-picture paragraph.
7. Merge the two chunks into the final ordered artifact (header → TL;DR → Pareto → prereqs
   → Method big-picture → Method walkthrough → Challenges → Experiments → Code highlights
   → Open questions). Smooth the transitions; don't just concatenate.

Then output:
- "# Final artifact" — the merged, polished reading, ready for the lead to write to disk.
- "---" separator.
- "**Critical:**" — items requiring producer re-dispatch (factual error, missing required
  section, blown length budget, incorrect math). Be specific so the lead can target the fix.
- "**Important:**" — items the lead should fix pre-write (small format issues, smoother
  transitions needed, a stronger Pareto bullet).
- "**Minor:**" — nits worth logging in <!-- QC notes --> at the artifact tail.
- "**Verification log:**" — one line per non-trivial check ("Confirmed Table 3 ImageNet
  number 84.2% by fetching arxiv.org/abs/...").
```

## When NOT to orchestrate

Skip the 3-agent dance for: re-reading sessions on a paper you've already read deeply, single-equation clarifications, "what's the headline of this paper" questions. The orchestration is for net-new deep readings.

For re-reads, the lead handles directly using the existing reading file as starting context.
