# Team Playbook: How to Run CONTENTFLOW Every Week

> Optional practice 04: a step-by-step guide so any marketer on the team can repeat the system.

## Weekly cycle (~1 working day)

| Step | Who | What | Tool / file |
|---|---|---|---|
| **1. Plan** (Mon AM) | Content lead | Copy last week's rows in the calendar. Pick 7 topics, balance the 4 pillars, assign channels. | [content-calendar.xlsx](content-calendar.xlsx) |
| **2. Collect sources** | Writer | For every topic, add 1–3 primary sources (DOI or official URL) **before** drafting. | Source list in the brief |
| **3. Draft text** | Writer + LLM | Paste the [Brand Voice Guide](02-brand-voice-guide.md) and the source list into the prompt. Use **CO-STAR** for blog, **RTF** for social. | [Prompt Library](06-prompt-library.md) |
| **4. Generate visuals** | Designer + image model | Use the image formula. Always include palette hex codes and *"no logos, no text on devices"*. Generate 2–3 variants, keep 1. | P-07 to P-09 |
| **5. Video & voice** | Anyone | Edit scene text and VO lines in `build_media.py`, then run `python scripts/build_media.py`. | [build_media.py](../scripts/build_media.py) |
| **6. Review** | Editor (not the writer) | Run the 4 checks: tone · keyword · copyright · sources. Log every fix. | [Review Log](04-content-review-log.md) |
| **7. Approve & schedule** | Content lead | Only "Ready" items get scheduled. | Buffer / Meta Business Suite |

## Setup (one time)

```bash
git clone <this-repo>
cd neuralis-contentflow
pip install -r requirements.txt     # piper-tts, openpyxl
# FFmpeg must be on PATH: https://ffmpeg.org/download.html
python scripts/build_calendar.py    # -> docs/content-calendar.xlsx / .csv
python scripts/build_media.py       # -> assets/audio/*.mp3, assets/video/*.mp4
```

## Review checklist (copy into each piece)

- [ ] **Tone:** reads like the voice guide? No banned words (miracle, hack, 10x, grind…)
- [ ] **Keyword:** primary keyword in title / first paragraph / meta (blog) or hook (social)
- [ ] **Copyright:** no artist/brand names in prompts · no logos in images · licences noted for voice/music
- [ ] **Sources:** every number has a DOI/URL · emerging science is hedged · no medical claims
- [ ] **Format:** platform limits respected (characters, slides, seconds)

## Rules of thumb learned in this project
1. Give the model a **source whitelist**. It's the best defence against invented statistics.
2. Add **exclusions** to image prompts by default.
3. Keep media builds **scripted**. Editing one line and re-running beats re-editing a timeline.
4. The reviewer is never the person who wrote the prompt.
