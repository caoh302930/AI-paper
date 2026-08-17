---
name: paper-reading
description: Produce a teaching-grade deep reading of a research paper — not a surface summary, but a Feynman-style walkthrough with prerequisites taught from first principles, contributions framed against named baselines and datasets, an equation-by-equation method explanation with symbols decoded, brief on-demand explanations of the load-bearing prior work the paper assumes you already know, field-level challenges and how this work addresses them, experiments with concrete numbers, and code highlights when a repo is available. Works across fields — ML, systems, biology, economics, physics, theory — adjust tone for the discipline. Triggers on "/paper-reading <link | arxiv-id | title>", or phrases like "read this paper deeply", "walk me through this paper", "study this paper with me", "help me understand this paper from scratch", "teach me this paper", or whenever the user shares a paper expecting deep study rather than a casual summary.
license: MIT
version: 1.0.1
allowed-tools:
  - Task
  - WebFetch
  - WebSearch
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---

# Paper Reading

Deeply read a research paper and produce a structured markdown write-up that is genuinely educational — something the user could return to in six months and re-learn the paper from, without re-reading the original.

The goal is **teaching, not summarization**. Output should read like notes from a thoughtful senior PhD student who took the time to look up the things the paper assumed you already knew. Target: **15–20 minutes of reading, ~2500–4000 words**, scaling modestly with complexity (lighter for short papers, up to ~4500 for dense theory or systems papers).

## Three guiding principles

Hold these as you work; they matter more than any individual rule below.

**1. Feynman: teach, don't list.** Every section is *teaching the reader an idea*, not cataloguing what the paper mentions. Prefer explanation over enumeration; plain language over borrowed jargon; "here's why this works" over "here's what the paper says". When you catch yourself writing a list, try to turn it into an explanation — usually possible, usually better. This applies especially to **Prerequisites**, **Method**, and **Challenges**.

**2. Pareto: 20% of the paper carries 80% of the value.** Identify the core idea, the load-bearing technique, and the one or two results that matter — and spend 80% of your word budget there. Always surface this prioritization explicitly with a short "What matters, what doesn't" callout near the top, telling the reader which parts to read carefully, which to skim, and which are deprecated or superseded by later work. The paper itself can't do this — it has to cover everything for review. You can, and should.

**3. Don't silently degrade.** If you can't fetch the paper, can't read the repo, or couldn't confirm a claim, say so in the output. A clearly-flagged gap is much more useful than a confident fabrication. See `references/edge-cases.md` for handling paywalled / non-arXiv / multi-match / no-public-code cases.

## Workflow — orchestrate, then synthesize

The default workflow runs as **lead + 2 producers + 1 QC**. The lead (you) coordinates; producers and QC are dispatched as Task subagents with isolated context. This pattern catches a single agent's blind spots and produces a noticeably stronger reading at modest extra cost.

1. **Resolve the paper** (lead). Confirm the paper with the user if input is title-only — one search, one confirmation, no long candidate lists. Normalize arXiv URLs (`abs/{id}`, `html/{id}`, `e-print/{id}`, `pdf/{id}`).
2. **Gather context** (lead, ~1 minute, parallel searches): code repo, project page, venue, author affiliations, supplementary. Note "not found" and move on if elusive.
3. **Dispatch Producer A and Producer B in parallel** (single message with two Task calls). See `references/orchestration.md` for full producer + QC prompts. Lanes:
   - **Producer A — Math & Method.** Sections 3–4: method, experiments, ablations. Reproduces equations precisely, explains symbols in words, traces and briefly explains load-bearing prior work the paper doesn't re-explain (the key differentiator — see "tracing prior work" below), names actual losses, blocks, datasets, hyperparameters, numbers.
   - **Producer B — Context & Code.** Abstract, intro, related-work, conclusion; reads the code repo if accessible and reports paper↔code mismatches; framing, impact, what's deprecated/superseded, broader landscape (strictly bounded — don't drift into survey).
4. **Dispatch QC** with both producer outputs verbatim + the source paper. QC verifies math, formatting, depth/compactness balance, prior-work briefs, code-tier label, and writes the merged final artifact + a Critical / Important / Minor issue list.
5. **Act on QC feedback** (lead). Critical → re-dispatch the relevant producer with QC's feedback. Important + Minor → log to a `<!-- QC notes -->` block at the tail.
6. **Write the final file** (lead — single point of control for path + git). Default output: `./<short-name>-reading.md` in the user's working directory, where `<short-name>` is a 1–3 word memorable slug (the paper's acronym if available — `clip`, `dinov3`, `pi-zero` — otherwise 2–3 keywords).

Check in with the user only after step 1. After that, run end-to-end.

## Tracing prior work — the key differentiator

Most summarizers recap. This skill *explains*. When the paper says *"we use [X] features"* or *"following [Y], we…"* and doesn't re-explain X or Y, **flag it** and write a 3–5 sentence brief on **the specific part this paper is leveraging** — not a general summary. Be selective: usually 2–5 briefs, only for *load-bearing* references. A paper that cites 40 works doesn't need 40 briefings.

Producer A is responsible for these briefs. Insert each brief inline in the Method walkthrough, exactly where the reader would be asking *"wait, what's that?"* — not in a separate section at the end.

## Output structure

The final artifact follows this skeleton; full template + writing style live in `references/output-template.md`.

1. **Header** — title, authors, venue, organizations, links (arXiv, code, project page).
2. **TL;DR and contributions** — 2–3 plain-language sentences + bullet contributions + named baselines + datasets + headline numbers.
3. **What matters, what doesn't** — the Pareto callout (3–6 bullets using 🎯 core / 🔧 useful / 📎 nice-to-know / ⚠️ deprecated / 🔕 skippable, scannable in 30 seconds; full legend in `references/output-template.md`).
4. **Context and prerequisites** — connected prose teaching each load-bearing concept; not a list of definitions.
5. **Method** — opens with a jargon-free big-picture paragraph (what / how / why); then a walkthrough that motivates each step ("we want X, but Y, so Z"), introduces equations with symbols explained in words, inlines prior-work briefs where needed.
6. **Challenges in the field — and what this work addresses** — explain *why* each challenge is hard before pairing with the solution.
7. **Experiments and results** — brief; nuance the headline (ablations that matter, settings where the method struggled, surprises).
8. **Code highlights** — only if a repo exists. Label the access tier explicitly: *Reviewed* (read the source), *Inferred from paper* (couldn't read source — flag), or *User-provided* (user uploaded). Look for paper↔code mismatches; flag them.
9. **Open questions and limitations** — 2–4 bullets.

## Self-check before saving

- [ ] I identified the 20% that matters most and gave it 80% of the space.
- [ ] The "What matters, what doesn't" callout tells the reader where to focus and what's deprecated.
- [ ] The Method opens with a jargon-free big-picture paragraph (what / how / why).
- [ ] The Method walkthrough motivates each step — not a recap.
- [ ] Prerequisites *teach* in connected prose, not list definitions.
- [ ] Load-bearing prior work has 3–5-sentence briefs inserted inline where they're needed.
- [ ] Every concrete claim is verified from a source I can read, or clearly flagged as inferred.
- [ ] The code section has an explicit access-tier label.
- [ ] Headline numbers are specific (datasets, baselines, deltas) — no "improves performance".
- [ ] Math follows `references/math-rendering.md` (inline `$...$`, multi-line `$$`, `\lt`/`\gt` not `<`/`>`).

## Reading order — non-linear is faster

LLM attention degrades over long inputs. Read: (1) abstract + intro, (2) conclusion/discussion, (3) figures 1–2 with captions, (4) experiments intro + main results table, (5) method in depth (prior-work tracing happens here), (6) related work (skim for names from step 5), (7) appendix (only if method referenced it).

**Source format preference:** uploaded PDF (use `pdf-reading` skill if available) → arXiv HTML → arXiv LaTeX source → arXiv PDF (last resort, chunk by section). When fetches fail (arXiv rate-limits aggressively), do other useful work, try sibling URLs, **ask the user to upload the PDF**, fall back to search snippets only as last resort, and **flag the fallback in the output** so the reader knows trust level.

## References

- `references/orchestration.md` — full Producer A / Producer B / QC prompt templates. Read at step 3.
- `references/output-template.md` — complete output skeleton + writing-style rules.
- `references/math-rendering.md` — math delimiter rules for cross-renderer compatibility.
- `references/edge-cases.md` — non-arXiv venues, paywalls, ambiguous matches, missing code, short papers, flawed papers.
