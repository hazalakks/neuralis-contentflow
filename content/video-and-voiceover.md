# Video & Voiceover

## 1. 18-second vertical teaser

▶️ **[neuralis-teaser-9x16.mp4](../assets/video/neuralis-teaser-9x16.mp4)** · 1080×1920 · 30 fps · 18.0 s · H.264 + AAC
*Calendar day 5 (Fri) · Reels / Shorts / TikTok · Pillar 4: Sustainable Performance*

[![Teaser poster frame](../assets/video/neuralis-teaser-poster.jpg)](../assets/video/neuralis-teaser-9x16.mp4)

### Storyboard

| Time | Visual | On-screen text | Voiceover |
|---|---|---|---|
| 0–5 s | `hero-workspace.jpg`, slow pan | **YOUR FOCUS / ISN'T BROKEN.** · *It's overloaded.* | "Your focus isn't broken. It's overloaded." |
| 5–10 s | `brainwave-synapses.jpg`, slow pan | **SILENCE / THE NOISE.** · *One rhythm. One thought.* | "Silence the noise. Give your mind one thing to hold." |
| 10–15 s | `product-mobile-concept.jpg`, slow pan | **SOUND THAT / ADAPTS TO YOU.** · *Neuro-adaptive focus audio* | "Neuralis shapes sound around the way you work." |
| 15–18 s | Obsidian end card | **NEURALIS** · *Focus, by design.* | "Neuralis. Focus, by design." |

**Sound:** generated low ambient pad (A2 + E3 + A3 sine tones with slow tremolo), mixed under the voiceover. It's synthesised in FFmpeg, so no music licensing is involved.
**Design rules applied:** ≤ 8 words on screen per scene · brand palette only · cross-fades of 0.4 s · watermark top-left.

### How it was made
All three visuals were AI-generated (see [prompt library](../docs/06-prompt-library.md#images)). The voice is Piper neural TTS. The edit, motion, typography and audio mix are fully scripted in [`scripts/build_media.py`](../scripts/build_media.py), so the video can be rebuilt with one command.

---

## 2. TTS voiceover: "The One-Minute Neural Reset"

🔊 **[neural-reset-voiceover.mp3](../assets/audio/neural-reset-voiceover.mp3)** · 49.6 s · 192 kbps
*Calendar day 6 (Sat) · Spotify / website audio · Pillar 4: Sustainable Performance*

| Setting | Value | Why |
|---|---|---|
| Engine | Piper neural TTS (offline, open source) | Free and reproducible. Runs locally. |
| Voice | `en_US-ryan-high` | Warm, calm male voice that fits "calm, precise, never hype" |
| Speed | `length_scale 1.12` (~12% slower) | The voice guide asks for a slow, intimate delivery |
| Sentence pause | 0.6 s | Room to breathe between ideas |
| Background | Generated ambient pad, low-pass 900 Hz | Calm bed that doesn't compete with speech |
| Licence | Voice dataset CC BY-NC-SA 4.0 | OK for portfolio and education. Would need a commercial voice for a real launch. |

### Script
> Wherever you are right now… let your shoulders drop. Unclench your jaw. Take one slow breath in… and let it go.
>
> All day, your attention has been pulled in a hundred directions. Every alert, every open tab, every quick question asks your brain to switch tracks. And every switch has a cost.
>
> You are not failing at focus. You are carrying too much at once.
>
> So for the next minute… carry less. Let the sound around you settle into one steady rhythm. Nothing to answer. Nothing to catch up on. Just one thought… and the space to finish it.
>
> When you are ready, come back to your work. Slower. Clearer. On your own terms.
>
> This is Neuralis. Focus, by design.

**Voice-guide check:** no medical claims ✅ · no unsourced numbers ✅ · calm, humane tone ✅ · signature line ✅
