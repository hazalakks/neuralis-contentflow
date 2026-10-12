# AI Usage Report

> Evaluation criterion: **Process Transparency (10 pts)**. Which tool was used for which task, why it was chosen, and what went wrong.
> This report lists **only the tools that were actually used** in this project.

## Toolchain

| Task | Tool actually used | Why this tool | Problems & how they were solved |
|---|---|---|---|
| Strategy, copy drafting, prompt design | **Google Gemini** (v1 draft) and **Anthropic Claude** (v2 revision), both used through the **Antigravity** AI agent IDE | Strong long-context reasoning. Follows structured prompt formulas (RTF / CO-STAR) reliably. | The v1 draft contained hallucinated or distorted statistics and overclaims (see [Review Log](04-content-review-log.md) T1–T9). Fixed through a second-pass fact-check against primary sources. |
| Fact-checking | Web search via the AI agent + manual reading of primary sources (DOIs) | Primary sources are the only reliable way to verify numbers | Found that a popular "23 minutes" figure doesn't match the peer-reviewed paper (T1), and a missing co-author in a citation (T11). |
| Image generation | **Antigravity built-in image generation** (Google image model) | Good prompt adherence for lighting, palette and composition. Integrated in the same workspace. | Hero v1 leaked a real brand name onto a monitor and rendered garbled HUD text. Regenerated with "no logos, no text" constraints (V1). |
| Text-to-speech | **Piper** neural TTS, voice `en_US-ryan-high` (open source, runs offline) | Free, local, reproducible from a script. A calm voice that fits the brand. | First choice (Microsoft Edge TTS via `edge-tts`) returned **HTTP 403** and couldn't be used. Switched to Piper. Voice dataset is CC BY-NC-SA 4.0, so the audio is non-commercial (A1). |
| Video editing & audio mix | **FFmpeg**, scripted in Python ([`build_media.py`](../scripts/build_media.py)) | Fully reproducible. Exact control over timing, palette and typography. No watermark. | Windows font paths broke FFmpeg filter syntax, so fonts are copied into a temp folder. Long VO lines are checked automatically so they fit each 5-second scene. |
| Calendar spreadsheet | Python + **openpyxl** ([`build_calendar.py`](../scripts/build_calendar.py)) | One source of truth produces both Excel and CSV | — |
| Showcase website | HTML + Tailwind CSS (CDN), drafted with the AI agent | Zero build step, so it can be hosted on GitHub Pages | v1 had broken image paths (timestamped filenames). Fixed after the asset rename. |

## Where AI helped most, and where it didn't

| ✅ Big time savers | ⚠️ Needed human judgement |
|---|---|
| Structuring strategy documents from a brief | Verifying **every** statistic. AI confidently invents plausible numbers. |
| Generating multiple on-brand copy variants quickly | Judging what's *fair* to say about competitors |
| Producing on-palette visuals in minutes | Spotting brand marks and artefacts in images |
| Writing the media-build and calendar scripts | Licence checks (voice dataset, music) |

## Human-in-the-loop decisions
- Chose the brand concept (NEURALIS) out of several AI-proposed options.
- Asked for the whole project to be in English for GitHub publication.
- Approved the switch from demo-only storyboards to **real** video and audio files after checking the brief.
- Final review and approval of every piece listed in the [Review Log](04-content-review-log.md).

## Estimated effort

| Phase | Approx. time |
|---|---|
| Brand strategy & voice guide | ~45 min |
| Calendar + content drafting | ~60 min |
| Images (incl. 1 regeneration) | ~15 min |
| Video + voiceover pipeline | ~45 min |
| Fact-check & review log | ~45 min |

*These are rough estimates for this project, not benchmarked measurements.*
