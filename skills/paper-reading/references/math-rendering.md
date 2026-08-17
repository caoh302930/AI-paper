# Math rendering — cross-renderer compatibility

These rules make the equations in your paper-reading output render correctly across the major Markdown surfaces: GitHub, KaTeX/MathJax viewers, popular Markdown editors, Markdown-aware note-takers. The cost of getting them wrong is silent breakage on the surface the user actually reads on.

## Rule 1 — Inline math: plain `$...$`

```markdown
The contrastive loss minimizes $-\log \frac{\exp(\text{sim}(z_i, z_j)/\tau)}{\sum_k \exp(\text{sim}(z_i, z_k)/\tau)}$.
```

Renders correctly in most modern Markdown editors and KaTeX/MathJax-based viewers.

**Known caveat — GitHub:** GitHub's GFM emphasis pass runs *before* the math pass, which means inline math containing `_{...}` (subscripts) renders mangled — GFM eats the `_` for emphasis. Inline math without subscripts renders fine on GitHub. There is **no inline form that wins on every renderer**: backtick `` $`...`$ `` fixes GitHub but breaks editors; `\_`-escapes fix GitHub only; `\sb` fails everywhere. We accept the GitHub-with-subscripts loss; it's the least-bad equilibrium.

If your output's primary surface is GitHub-only and inline subscripts matter, use display blocks instead (next rule) — they render universally.

## Rule 2 — Display math: always multi-line with blank lines

Opening `$$` on its own line, content, closing `$$` on its own line. Blank line before and after. **Blank line between consecutive blocks.** Verified across all major renderers.

```markdown
The KL divergence between two Gaussians is:

$$
D_{KL}(\mathcal{N}_0 \| \mathcal{N}_1) = \frac{1}{2} \left( \mathrm{tr}(\Sigma_1^{-1} \Sigma_0) + (\mu_1 - \mu_0)^T \Sigma_1^{-1} (\mu_1 - \mu_0) - k + \ln \frac{\det \Sigma_1}{\det \Sigma_0} \right)
$$

When $\Sigma_0 = \Sigma_1$, this simplifies to:

$$
D_{KL} = \frac{1}{2} (\mu_1 - \mu_0)^T \Sigma^{-1} (\mu_1 - \mu_0)
$$
```

**Do NOT use single-line `$$...$$`** (e.g. `$$x = y$$`). Some editors (Cursor and others) break on the single-line form.

## Rule 3 — `<` and `>` inside math: always `\lt` / `\gt`

Never write `\prod_{k<i}` or `\sum_{t>0}`. GitHub's Markdown preprocessor runs HTML sanitization *before* MathJax/KaTeX:

- `<i` looks like the start of an HTML tag.
- The sanitizer chews through the matching `>`.
- The math engine sees a broken expression — typical error: *"Extra open brace or missing close brace"*.

`\lt` and `\gt` render identically and dodge the preprocessor entirely.

```markdown
Wrong (breaks on GitHub):

$$
P(x) = \prod_{k<i} (1 - p_k) \cdot p_i
$$

Right (works everywhere):

$$
P(x) = \prod_{k\lt i} (1 - p_k) \cdot p_i
$$
```

This applies inside both `$...$` and `$$...$$`. It does NOT apply outside math (regular Markdown text uses `<` and `>` normally).

## Rule 4 — Avoid LaTeX features common renderers don't support

KaTeX is more permissive than MathJax in some places, less in others; GitHub uses MathJax under the hood. Safe choices:

- `\mathbb{R}`, `\mathcal{N}`, `\mathbf{x}`, `\mathrm{tr}` — universal.
- `\frac`, `\sum`, `\prod`, `\int`, `\sqrt` — universal.
- `\begin{aligned}...\end{aligned}` — works in display blocks; better than `eqnarray`.
- `\text{...}` — for words inside math.

Avoid:

- `\eqref`, `\label`, `\tag` — inconsistent across renderers.
- Custom `\newcommand` definitions in mid-document — render only in some viewers.
- Multi-line equations split with raw `\\` outside an `aligned` environment — fragile.

## Rule 5 — Symbols in words

Even when you render an equation correctly, accompany it with a one-line decode of every symbol the reader hasn't seen yet:

> The cosine similarity in the loss is $\text{sim}(z_i, z_j) = z_i^\top z_j / (\|z_i\|\|z_j\|)$, where $z_i$ and $z_j$ are the L2-normalized embeddings of the anchor and positive sample, and $\tau$ is a learned temperature.

This is *especially* important for inline math on GitHub-rendered surfaces, where subscripts may render mangled — the prose decode is the fallback.

## Quick reference

| Want | Write | Avoid |
|---|---|---|
| Inline math | `$x = y$` | `\(x = y\)` (LaTeX-only); single backticks |
| Display math | `$$\n...\n$$` (multi-line, blanks around) | `$$x=y$$` (single-line) |
| Less-than in math | `\lt` | `<` |
| Greater-than in math | `\gt` | `>` |
| Aligned multi-line | `\begin{aligned}...\end{aligned}` inside `$$` | bare `\\` |
| Two display blocks back-to-back | blank line between `$$` blocks | adjacent `$$ \n $$` |
