# Prompt Library

> Optional practice 04: every important prompt used in the project, **with its result**.
> Formulas: **RTF** (Role · Task · Format) for short-form content · **CO-STAR** (Context · Objective · Style · Tone · Audience · Response) for long-form.

| ID | Output | Formula | Result |
|---|---|---|---|
| P-01 | Brand strategy | CO-STAR | [01-brand-strategy.md](01-brand-strategy.md) |
| P-02 | Brand voice guide | CO-STAR | [02-brand-voice-guide.md](02-brand-voice-guide.md) |
| P-03 | SEO blog post | CO-STAR | [blog-post.md](../content/blog-post.md) |
| P-04–06 | 3 social posts | RTF | [social-posts.md](../content/social-posts.md) (prompts are shown inline with each post) |
| P-07–09 | 3 brand images | Image formula | [assets/images/](../assets/images/) |
| P-10 | Video script | RTF | [video-and-voiceover.md](../content/video-and-voiceover.md) |
| P-11 | Voiceover script | RTF | [video-and-voiceover.md](../content/video-and-voiceover.md#2-tts-voiceover-the-one-minute-neural-reset) |
| P-12 | Fact-check pass | RTF | [04-content-review-log.md](04-content-review-log.md) |

---

## P-01 · Brand strategy (CO-STAR)
```text
CONTEXT:   Final project for an AI content-production course. The brand is NEURALIS, a fictional
           software company making neuro-adaptive focus audio for knowledge workers. The course
           scenario: a software company wants to cut its marketing team's weekly content
           workload and keep its brand voice consistent across channels.
OBJECTIVE: Produce a 1–2 page brand strategy: sector definition, 3–5 competitors with gaps,
           identity card (values, hex palette, typography, visual style), Why-Who-What-How,
           2 personas, 3–4 content pillars with share %.
STYLE:     Strategy-consultancy brief. Tables over prose.
TONE:      Confident, factual. Fair to competitors.
AUDIENCE:  Course evaluators and portfolio reviewers (marketing and tech hiring managers).
RESPONSE:  Markdown, H2 per section, ≤ 900 words.
```
**Result notes:** v1 described a competitor unfairly (Review Log T10). Fixed in v2.

## P-02 · Brand voice guide (CO-STAR)
```text
CONTEXT:   NEURALIS brand strategy (attached).
OBJECTIVE: A ONE-PAGE voice guide that works as the control layer for blog, social, image,
           video and voice content.
STYLE:     Practical style-guide (like Mailchimp's content style guide). We/never tables.
TONE:      Calm, precise.
AUDIENCE:  Content creators and AI prompts. It will be pasted into every generation prompt.
RESPONSE:  Personality line · 4 traits (we sound like / never like) · use/avoid vocabulary
           · 5 hard rules (incl. no medical claims, no unsourced stats) · per-format tone table
           · 3 signature lines.
```

## P-03 · SEO blog post (CO-STAR)
```text
CONTEXT:   NEURALIS, a focus-audio app (fictional). Brand Voice Guide attached. Verified sources
           you MAY use: Mark et al. 2005 (≈11 min per task, ≈25 min to resume after
           interruption); Rubinstein et al. 2001 (task-switch costs); Garcia-Argibay et al. 2019
           (meta-analysis, binaural beats, moderate but variable effects); Woods et al. 2024
           (amplitude-modulated music & sustained attention). Do NOT introduce other statistics.
OBJECTIVE: Rank for "cognitive fatigue" and move readers to a free trial.
STYLE:     Explanatory long-form, like a well-edited science-journalism piece.
TONE:      Calm, evidence-based, honest about uncertainty. Never hype.
AUDIENCE:  Software engineers and startup founders with afternoon brain fog.
RESPONSE:  Front-matter (title ≤ 70 chars, meta ≤ 160 chars, slug, keywords) · H1 · 5–6 H2s
           · 1 table · 1 pull-quote · 3 actionable habits · medical disclaimer · soft CTA
           · numbered sources with DOIs · ~1,000 words.
```
**Result notes:** the first-draft version of this prompt had no source whitelist, and the draft invented statistics (T2, T3). Adding the *"Verified sources you MAY use… do NOT introduce other statistics"* line fixed it. **This is the single most effective prompt change in the project.**

## Images

Formula: `[subject + action] + [environment + light] + [palette hex] + [camera/render style] + [exclusions]`

### P-07 · Hero workspace → [hero-workspace.jpg](../assets/images/hero-workspace.jpg)
```text
A sleek, futuristic, minimalist dark-mode workspace designed for deep focus, seen from behind
a person wearing matte black over-ear headphones. Obsidian dark room (#0B0F14), soft glowing
synapse-cyan (#00F2FE) and bio-emerald (#10B981) accent light strips. A curved unbranded
ultra-wide monitor shows a single clean abstract cyan-to-emerald soundwave on a dark interface,
no readable text. Matte black keyboard, minimal desk, rainy night city bokeh through window.
Moody volumetric cinematic lighting, photorealistic, cyber-minimalist aesthetic.
No logos, no brand names, no text on devices or bezels.
```
**Result notes:** v1 of this prompt had no exclusions, and the image showed a real hardware brand name (Review Log V1). The final line fixed it.

### P-08 · Brainwave synapses → [brainwave-synapses.jpg](../assets/images/brainwave-synapses.jpg)
```text
An artistic and scientific 3D visualization of human brainwaves transitioning into deep focus.
Obsidian black background, luminous glowing abstract neural network synapses pulsing in
electric cyan (#00F2FE) and bio-emerald green (#10B981). Elegant smooth holographic soundwave
ripples flowing across the center. Minimalist typography faintly visible in background reading
'ALPHA FREQUENCY 8-12Hz'. Cyber-minimalist, sleek, editorial aesthetic, award-winning
scientific graphic design.
```

### P-09 · Product concept → [product-mobile-concept.jpg](../assets/images/product-mobile-concept.jpg)
```text
A luxury conceptual tech product presentation of NEURALIS. A sleek matte black smartphone
resting on a minimalist dark volcanic stone surface, screen displaying a glowing dark-mode UI
with 'NEURALIS' logo, an active cyan and emerald biometric soundwave visualizer, and a focus
score metric '94% FLOW STATE'. Next to the phone are premium matte black wireless audio
earbuds with subtle glowing cyan indicator lights. Minimalist, premium dark aesthetic,
studio lighting, depth of field, 8k render.
```
**Result notes:** the phone resembles a real flagship (V2), and the wordmark font is off-brand (V4). Next iteration should add *"generic custom-designed phone, no recognisable manufacturer design, wordmark in geometric sans-serif"*.

## P-10 · Video script (RTF)
```text
ROLE:   You are a short-form video copywriter for NEURALIS (Brand Voice Guide attached).
TASK:   Write an 18-second vertical teaser in 4 scenes (5 s, 5 s, 5 s, 3 s end card) using the
        three brand images in order: hero, brainwave, product. Calm, not urgent. No numbers,
        no outcome claims.
FORMAT: Table: time · visual · on-screen text (≤ 8 words, 2 lines max) · voiceover (≤ 4 s
        when read aloud) · end with the signature line "Focus, by design."
```

## P-11 · Voiceover script (RTF)
```text
ROLE:   You are a meditation-app scriptwriter who also understands cognitive science.
TASK:   Write a ~50-second "One-Minute Neural Reset" voiceover for NEURALIS. Acknowledge
        attention fatigue, guide one breath, invite a return to work. No medical claims, no
        frequencies, no statistics.
FORMAT: ~110 words · short sentences · pauses marked with "…" · end with
        "This is Neuralis. Focus, by design."
```

## P-12 · Fact-check pass (RTF)
```text
ROLE:   You are a skeptical science fact-checker.
TASK:   List every factual claim and number in the attached content. For each, find the primary
        source (DOI or official URL), state whether the claim matches the source exactly, and
        propose a fix: keep / rephrase / hedge / remove. Flag medical claims and claims about
        competitors separately.
FORMAT: Table: # · claim · location · source · verdict · fix.
```
