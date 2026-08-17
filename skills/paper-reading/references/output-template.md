# Output template + writing style

The complete skeleton the lead writes to disk after QC merges the two producer chunks.

## File skeleton

```markdown
# [Paper Title]

**Authors:** ...  **Venue:** ...  **Organization(s):** ...
**arXiv:** [link]  **Code:** [link or "not released"]  **Project page:** [link or "none"]

## TL;DR and contributions
[2–3 sentences: what the paper does, in plain language.]

**Main contributions:** [specific one-line bullets]
**Compared against:** [named baselines]
**On datasets:** [names, with a note on what kind of data if non-obvious]
**Headline improvements:** [specific numbers, e.g., "+4.2 mIoU on ADE20K vs. Method X"]

## What matters, what doesn't

[The Pareto callout. 3–6 short bullets signaling where to focus and where to skim. Use these labels explicitly:

- **🎯 Core idea (read carefully):** the 20% of the paper that carries most of the value — usually the key insight and one or two technical moves.
- **🔧 Useful in practice:** parts that matter for anyone implementing or building on the work.
- **📎 Nice to know:** context or ablations worth a glance but not essential.
- **⚠️ Deprecated / superseded:** anything later work has replaced or improved on — name the replacement.
- **🔕 Skippable:** standard boilerplate, exhaustive comparison tables, minor ablations.

Only include categories that apply. Reader should absorb in 30 seconds.]

## Context and prerequisites

[**Teach, don't list.** For each concept the reader needs to know, write a short paragraph (3–5 sentences) that *explains* it — what it is, how it works intuitively, and specifically why it matters for *this* paper. Avoid bullet-list-of-definitions format; prefer connected prose that builds the reader's mental model. Pick only concepts that are load-bearing for the Method section. If the paper is about diffusion models, don't explain what a neural network is.]

## Method

### The big picture (layman version)

[**Always start the Method section with this paragraph.** Before any equations, jargon, or prior-work briefs — write a 5–8 sentence explanation that a smart undergraduate from a different field could follow. Cover three things: **what** the method does (concrete, everyday language), **how** it does it (the core mechanism, stripped of notation), and **why** it works / what problem it solves (which challenge from the earlier section this actually cracks, and the intuition for why the approach is the right shape for the problem). Use analogies when they help — "this is like caching the part that doesn't change" or "think of it as rearranging the math so the GPU's fast lane can be used". No symbols, no jargon the Context section didn't already introduce. After reading this paragraph, a reader should be able to predict roughly what the detailed walkthrough will say.]

### The walkthrough

[**Teach the method, don't recap it.** Imagine you're a professor introducing this as a textbook topic. That means: work from the simplest version of the idea to the full version, building one piece at a time. Motivate each step before showing it — "we want X, but the obvious approach fails because Y, so we do Z instead". When you introduce an equation, say what each symbol *means* in words before (or right after) the math. When the method makes a design choice that could have gone differently, briefly note the alternative and why the paper chose what it did. When you hit a load-bearing prior work, insert the brief inline exactly where the student would be asking "wait, what's that?" — not in a separate section at the end. The test for a good walkthrough: a reader who skipped the paper entirely should be able to reconstruct the method from this section alone, and moreover understand *why* it's built the way it is, not just what it does.]

## Challenges in the field — and what this work addresses

[2–3 challenges (4 only if genuinely distinct). For each, **explain why the challenge is hard** (not just state it), then explain why this paper's approach is the right shape to address it (not just state that it does). The reader should come away understanding the problem structure, not just a challenge→solution pairing. Close with one "what this work does NOT address" bullet — often the most useful content in this section, and it sets up the limitations discussion.]

## Experiments and results

[Brief — contributions already covered the headline. Add nuance: ablations that matter, settings where the method struggled, surprises.]

## Code highlights

[Only if a repo exists. Otherwise write "Code not released" and omit this section.]

[**Be explicit about access depth** — label this section with one of three tiers:
- *Reviewed* — you actually read the key files, either from an uploaded archive/files or from a successful fetch. Describe what you saw: paths, function names, specific choices.
- *Inferred from paper* — repo is linked but you couldn't read source. Describe what it *likely* contains and flag clearly: *"Inferred from the paper; I couldn't read the source directly."*
- *User-provided* — a specific sub-case of *Reviewed*: the user uploaded the repo or key files.]

[**If you hit access blockers, ASK** — don't silently degrade to inference.
1. *Ask for upload* (preferred): "Can you clone the repo and zip it, or attach the key file(s)? That unblocks me immediately and gives full-fidelity access."
2. *Ask to fetch*: "The repo is at [URL]. I can try fetching the key files — may or may not succeed depending on rate limits. Proceed, or would you prefer to upload?"]

[Once you have access, identify: repo structure (1–2 sentences), the entry point, the key file(s) implementing the contribution, non-obvious implementation choices (custom kernels, unusual data pipeline, hyperparameters differing from the paper), unusual dependencies/hardware requirements.

**Look for mismatches between the paper and the code.** Papers simplify; code is ground truth. If the paper says "we use the tile's top-left corner as reference" but the code uses the tile center, flag that. These small deltas are often where implementation trade-offs live, and the reader usually wants to know.]

## Open questions and limitations

[2–4 bullets. What the paper doesn't answer, acknowledged or apparent limitations, what a follow-up might investigate.]
```

## Writing style

- **Concrete, not vague.** "+1.7% Top-1 on ImageNet over ResNet-50", not "improves performance".
- **Explain, don't just name.** One-sentence parenthetical for terms the reader may only vaguely know ("contrastive loss", "diffusion model").
- **Equations: sparingly.** A single key loss, the paper's central reformulation, or a canonical definition earns a `$$...$$` block. Multi-line derivations almost never do — describe in prose. Prose survives being copied into plain-text contexts where math doesn't render. See `math-rendering.md` for delimiter rules.
- **Don't hedge when the paper is clear**, but **do hedge when it overclaims** (thin ablations, cherry-picked baselines) — briefly note in limitations.
- **Don't produce a section-by-section recap** ("Section 3 discusses…"). Users want a *taught explanation*, not a table of contents. The Method section in particular should teach the idea as a professor would — building up from intuition to detail — not narrate what the paper says in order.
- **Don't give every part of the paper equal weight.** If exhaustive related work eats 20% of your words and the core method gets 25%, the Pareto balance is wrong — trim related work to a few sentences and give the method room to breathe.
- **Don't skip the layman paragraph** at the top of the Method section. It's the thing that makes the detailed walkthrough land.
- **Don't skip the "What matters, what doesn't" callout.** Readers rely on it.
- **Don't turn Prerequisites into a list of definitions.** Teach each concept in connected prose.
- **Don't copy figures or long quotes.** Paraphrase.
- **Don't chase every citation.** Be strategic about which are load-bearing.

## Discipline tone tweaks

The skill works across fields; tweak section names and emphasis to fit the discipline:

- **CS / ML / systems / engineering papers** — default. "Experiments and results" / "Code highlights" / equations + numbers.
- **Theory papers** — rename "Experiments and results" → "Theorems and proofs". The Method walkthrough becomes the proof structure with intuition for each lemma. Code highlights typically omitted.
- **Empirical-science papers (biology, physics, economics)** — "Experiments and results" stays; "Code highlights" becomes "Data + code highlights" if datasets/scripts are public, with explicit access tier on each. Emphasize study design + statistical caveats in Open questions.
- **Survey papers** — the Pareto callout becomes critical (which sections of the survey are load-bearing for the field, which are exhaustive enumeration). Method section becomes "Taxonomy" with the survey's organizing principle.
