"""
NEURALIS · CONTENTFLOW — media build pipeline
=============================================

Generates the two multimedia deliverables of the content set:

  1. assets/audio/neural-reset-voiceover.mp3   (~55 s TTS voiceover + ambient bed)
  2. assets/video/neuralis-teaser-9x16.mp4     (18 s vertical teaser, 1080x1920)
     assets/video/neuralis-teaser-poster.jpg   (poster frame for the README)

Requirements
------------
  pip install piper-tts
  FFmpeg + FFprobe available on PATH

Usage
-----
  python scripts/build_media.py

Voice: Piper neural TTS (offline, open source) · voice "en_US-ryan-high".
Chosen for a warm, calm, mid-tempo male delivery that matches the brand voice
guide ("calm, precise, never hype"). Voice model is downloaded on first run
into ./voices (git-ignored). Dataset licence: CC BY-NC-SA 4.0, so this audio
is for non-commercial / portfolio use only.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "images"
AUDIO_OUT = ROOT / "assets" / "audio"
VIDEO_OUT = ROOT / "assets" / "video"

VOICE = "en_US-ryan-high"
VOICE_DIR = ROOT / "voices"
LENGTH_SCALE = "1.12"   # >1 = slower, calmer delivery

# --------------------------------------------------------------------------
# 1) Long-form voiceover: "One-Minute Neural Reset" (calendar day 6)
# --------------------------------------------------------------------------
NEURAL_RESET_SCRIPT = (
    "Wherever you are right now... let your shoulders drop. "
    "Unclench your jaw. Take one slow breath in... and let it go. "
    "All day, your attention has been pulled in a hundred directions. "
    "Every alert, every open tab, every quick question asks your brain to switch tracks. "
    "And every switch has a cost. "
    "You are not failing at focus. You are carrying too much at once. "
    "So for the next minute... carry less. "
    "Let the sound around you settle into one steady rhythm. "
    "Nothing to answer. Nothing to catch up on. "
    "Just one thought... and the space to finish it. "
    "When you are ready, come back to your work. Slower. Clearer. On your own terms. "
    "This is Neuralis. Focus, by design."
)

# --------------------------------------------------------------------------
# 2) Teaser video: 4 scenes, each with its own VO line and on-screen text
# --------------------------------------------------------------------------
SCENES = [
    {   # 0–5 s  · hook
        "image": "hero-workspace.jpg",
        "vo": "Your focus isn't broken. It's overloaded.",
        "vo_start": 0.4,
        "lines": ["YOUR FOCUS", "ISN'T BROKEN."],
        "sub": "It's overloaded.",
    },
    {   # 5–10 s · reset
        "image": "brainwave-synapses.jpg",
        "vo": "Silence the noise. Give your mind one thing to hold.",
        "vo_start": 5.3,
        "lines": ["SILENCE", "THE NOISE."],
        "sub": "One rhythm. One thought.",
    },
    {   # 10–15 s · product
        "image": "product-mobile-concept.jpg",
        "vo": "Neuralis shapes sound around the way you work.",
        "vo_start": 10.3,
        "lines": ["SOUND THAT", "ADAPTS TO YOU."],
        "sub": "Neuro-adaptive focus audio",
    },
]
END_CARD_VO = ("Neuralis. Focus, by design.", 15.3)
SCENE_LEN = 5.0
END_LEN = 3.0
TOTAL = SCENE_LEN * len(SCENES) + END_LEN  # 18 s

BRAND_CYAN = "0x00F2FE"
BRAND_BG = "0x0B0F14"


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print("  $", " ".join(cmd[:6]), "...")
    subprocess.run(cmd, check=True, cwd=cwd)


def duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(out.stdout.strip())


def tts(text: str, out: Path, sentence_silence: float = 0.45) -> None:
    model = VOICE_DIR / f"{VOICE}.onnx"
    if not model.exists():
        VOICE_DIR.mkdir(exist_ok=True)
        run([sys.executable, "-m", "piper.download_voices", "--download-dir", str(VOICE_DIR), VOICE])
    subprocess.run(
        [sys.executable, "-m", "piper", "-m", str(model), "-f", str(out),
         "--length-scale", LENGTH_SCALE, "--sentence-silence", str(sentence_silence), "--", text],
        check=True, capture_output=True,
    )


def ambient_bed(seconds: float) -> str:
    """Soft low pad (A2 + E3 + A3) with slow tremolo — generated, royalty-free."""
    return (
        f"aevalsrc='(0.05*sin(2*PI*110*t)+0.03*sin(2*PI*164.81*t)+0.02*sin(2*PI*220*t))"
        f"*(0.75+0.25*sin(2*PI*0.1*t))':s=44100:d={seconds:.2f}"
    )


# --------------------------------------------------------------------------
def build_voiceover(tmp: Path) -> None:
    print("[1/2] Neural Reset voiceover")
    vo = tmp / "reset_raw.wav"
    tts(NEURAL_RESET_SCRIPT, vo, sentence_silence=0.6)
    d = duration(vo)
    total = d + 4.0
    AUDIO_OUT.mkdir(parents=True, exist_ok=True)
    run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(vo),
        "-f", "lavfi", "-i", ambient_bed(total),
        "-filter_complex",
        "[0:a]adelay=1500|1500,apad[v];"
        "[1:a]lowpass=f=900,volume=0.55[b];"
        f"[v][b]amix=inputs=2:duration=shortest:normalize=0,"
        f"afade=t=in:d=1.5,afade=t=out:st={total-2.5:.2f}:d=2.5[out]",
        "-map", "[out]", "-t", f"{total:.2f}",
        "-c:a", "libmp3lame", "-b:a", "192k",
        str(AUDIO_OUT / "neural-reset-voiceover.mp3"),
    ])
    print(f"      -> {total:.1f} s")


def build_video(tmp: Path) -> None:
    print("[2/2] 18 s vertical teaser")
    # fonts copied locally so FFmpeg filter paths need no escaping on Windows
    fonts = Path("C:/Windows/Fonts") if sys.platform == "win32" else Path("/usr/share/fonts")
    shutil.copy(fonts / "segoeuib.ttf", tmp / "bold.ttf")
    shutil.copy(fonts / "segoeui.ttf", tmp / "regular.ttf")

    # VO clips
    vo_lines = [(s["vo"], s["vo_start"]) for s in SCENES] + [END_CARD_VO]
    vo_files = []
    for i, (text, start) in enumerate(vo_lines):
        f = tmp / f"vo{i}.wav"
        tts(text, f, sentence_silence=0.25)
        d = duration(f)
        assert d < SCENE_LEN, f"VO line {i} too long ({d:.2f}s)"
        vo_files.append((f, start))

    # text files (avoid quote escaping inside drawtext)
    def txt(name: str, value: str) -> str:
        (tmp / name).write_text(value, encoding="utf-8")
        return name

    inputs: list[str] = []
    for s in SCENES:
        inputs += ["-loop", "1", "-framerate", "30", "-t", str(SCENE_LEN), "-i", str(IMG / s["image"])]
    inputs += ["-f", "lavfi", "-i", f"color=c={BRAND_BG}:s=1080x1920:r=30:d={END_LEN}"]
    for f, _ in vo_files:
        inputs += ["-i", str(f)]
    inputs += ["-f", "lavfi", "-i", ambient_bed(TOTAL)]

    n_img = len(SCENES)
    fc: list[str] = []
    # slow horizontal pan on each image, cropped to 9:16
    for i in range(n_img):
        fc.append(
            f"[{i}:v]scale=-2:2112,crop=1080:1920:'(in_w-1080)/2-80+32*t':96,setsar=1,"
            f"format=yuv420p,fade=t=in:st=0:d=0.4,fade=t=out:st={SCENE_LEN-0.4}:d=0.4[v{i}]"
        )
    fc.append(f"[{n_img}:v]format=yuv420p,fade=t=in:st=0:d=0.5,setsar=1[v{n_img}]")
    fc.append("".join(f"[v{i}]" for i in range(n_img + 1)) + f"concat=n={n_img+1}:v=1:a=0[vc]")

    draw = ["[vc]drawbox=x=0:y=1180:w=1080:h=740:color=black@0.5:t=fill:enable='lt(t,15)'"]
    draw.append(
        f"drawtext=fontfile=bold.ttf:textfile={txt('wm.txt','NEURALIS')}:fontsize=34:"
        f"fontcolor={BRAND_CYAN}:x=64:y=120:enable='lt(t,15)'"
    )
    for i, s in enumerate(SCENES):
        a, b = i * SCENE_LEN + 0.4, (i + 1) * SCENE_LEN - 0.3
        en = f"enable='between(t,{a},{b})'"
        for j, line in enumerate(s["lines"]):
            draw.append(
                f"drawtext=fontfile=bold.ttf:textfile={txt(f's{i}l{j}.txt', line)}:fontsize=92:"
                f"fontcolor=white:x=(w-text_w)/2:y={1330 + j*112}:{en}"
            )
        draw.append(
            f"drawtext=fontfile=regular.ttf:textfile={txt(f's{i}sub.txt', s['sub'])}:fontsize=50:"
            f"fontcolor={BRAND_CYAN}:x=(w-text_w)/2:y=1600:{en}"
        )
    end_en = f"enable='gte(t,{TOTAL-END_LEN+0.3})'"
    draw.append(f"drawtext=fontfile=bold.ttf:textfile={txt('e1.txt','NEURALIS')}:fontsize=128:"
                f"fontcolor={BRAND_CYAN}:x=(w-text_w)/2:y=820:{end_en}")
    draw.append(f"drawtext=fontfile=regular.ttf:textfile={txt('e2.txt','Focus, by design.')}:fontsize=58:"
                f"fontcolor=white:x=(w-text_w)/2:y=990:{end_en}")
    draw.append(f"drawtext=fontfile=regular.ttf:textfile={txt('e3.txt','Concept brand  ·  CONTENTFLOW portfolio project')}:"
                f"fontsize=30:fontcolor=0x94A3B8:x=(w-text_w)/2:y=1760:{end_en}[vout]")
    fc.append(",".join(draw))

    # audio: VO lines placed on the timeline + ambient bed
    first_vo = n_img + 1
    for k, (_, start) in enumerate(vo_files):
        ms = int(start * 1000)
        fc.append(f"[{first_vo+k}:a]adelay={ms}|{ms}[a{k}]")
    bed = first_vo + len(vo_files)
    fc.append(f"[{bed}:a]lowpass=f=900,volume=0.5[bed]")
    fc.append(
        "".join(f"[a{k}]" for k in range(len(vo_files))) + "[bed]"
        f"amix=inputs={len(vo_files)+1}:duration=longest:normalize=0,"
        f"afade=t=in:d=0.5,afade=t=out:st={TOTAL-1.2}:d=1.2[aout]"
    )

    VIDEO_OUT.mkdir(parents=True, exist_ok=True)
    out = VIDEO_OUT / "neuralis-teaser-9x16.mp4"
    run([
        "ffmpeg", "-y", "-loglevel", "error", *inputs,
        "-filter_complex", ";".join(fc),
        "-map", "[vout]", "-map", "[aout]", "-t", str(TOTAL),
        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
        str(out.resolve()),
    ], cwd=tmp)
    run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "2.5", "-i", str(out),
         "-frames:v", "1", "-q:v", "3", str(VIDEO_OUT / "neuralis-teaser-poster.jpg")])
    print(f"      -> {duration(out):.1f} s")


def main() -> None:
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        build_voiceover(tmp)
        build_video(tmp)
    print("Done.")


if __name__ == "__main__":
    main()
