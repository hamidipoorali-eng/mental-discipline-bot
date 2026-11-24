import os
import sys
import shutil
import subprocess

# ==============================================================================
# اسکریپت برش خودکار ۱۵ کلیپ قسمت ۶ پپا پیگ (The Playgroup)
# شامل: ۵ جمله کلیدی قسمت ۶ + ۱۰ کلیپ اتصال به مرور شبکه‌ای
# خروجی: پوشه audio/ با فرمت MP3، بیت‌ریت 64kbps و مونو
# ==============================================================================

OUTPUT_DIR = "audio"
PADDING_START = 0.20  # ثانیه حاشیه تنفس قبل از جمله
PADDING_END = 0.25    # ثانیه حاشیه تنفس بعد از جمله

EP6_KEYWORDS = ["playgroup", "play group", "episode 6", "ep6", "6."]
MEDIA_EXTENSIONS = (".mp4", ".mp3", ".m4a", ".wav", ".mkv", ".webm", ".mov", ".ogg")

CLIPS_EP6 = [
    ("ep6_01.mp3", "00:00:30.510", "00:00:33.690"),  # [کلیدی ۱] looking forward to
    ("ep6_02.mp3", "00:00:35.070", "00:00:39.810"),  # [شبکه ۹] too small to...
    ("ep6_03.mp3", "00:00:41.030", "00:00:42.390"),  # [شبکه ۱۰] He'll be fine
    ("ep6_04.mp3", "00:00:42.890", "00:00:46.050"),  # [کلیدی ۲] keep him company
    ("ep6_05.mp3", "00:00:55.930", "00:00:56.610"),  # [شبکه ۵] Oh dear
    ("ep6_06.mp3", "00:01:07.980", "00:01:11.280"),  # [شبکه ۱۲] are you sure
    ("ep6_07.mp3", "00:01:59.130", "00:02:01.030"),  # [شبکه ۱۰] It's just a toy
    ("ep6_08.mp3", "00:02:18.530", "00:02:20.570"),  # [کلیدی ۳] That's brilliant
    ("ep6_09.mp3", "00:02:37.610", "00:02:39.250"),  # [شبکه ۸] not very good at painting
    ("ep6_10.mp3", "00:02:39.910", "00:02:41.970"),  # [شبکه ۸ و ۱۳] maybe you could help him
    ("ep6_11.mp3", "00:02:48.990", "00:02:53.030"),  # [کلیدی ۴] teach you how to paint
    ("ep6_12.mp3", "00:03:50.030", "00:03:54.450"),  # [شبکه ۴] I think ... should
    ("ep6_13.mp3", "00:03:58.190", "00:04:02.070"),  # [شبکه ۱] you must be very proud
    ("ep6_14.mp3", "00:04:12.670", "00:04:14.370"),  # [شبکه ۱۲] Can George come next time?
    ("ep6_15.mp3", "00:04:28.130", "00:04:30.890"),  # [کلیدی ۵] show us all how to paint
]


def to_seconds(ts: str) -> float:
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def find_ep6_file():
    all_files = [
        f for f in os.listdir(".")
        if os.path.isfile(f) and f.lower().endswith(MEDIA_EXTENSIONS)
    ]
    for fname in all_files:
        low = fname.lower()
        if any(k in low for k in EP6_KEYWORDS):
            return fname
    return None


def main():
    if not shutil.which("ffmpeg"):
        print("ERROR: برنامه ffmpeg روی سیستم شما نصب نیست یا در PATH قرار ندارد.")
        print("در ویندوز: winget install Gyan.FFmpeg")
        print("در مک:     brew install ffmpeg")
        sys.exit(1)

    src = find_ep6_file()
    if not src:
        print("فایل ویدیو یا صوت قسمت ۶ در این پوشه پیدا نشد!")
        print("اسم فایل را مثلاً ep6.mp4 بگذارید و دوباره اجرا کنید.")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"فایل شناسایی‌شده: {src}")
    print("=== شروع برش ۱۵ کلیپ قسمت ۶ ===")

    for out_name, start_ts, end_ts in CLIPS_EP6:
        start_sec = max(0.0, to_seconds(start_ts) - PADDING_START)
        end_sec = to_seconds(end_ts) + PADDING_END
        duration = max(0.2, end_sec - start_sec)

        out_path = os.path.join(OUTPUT_DIR, out_name)
        cmd = [
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-ss", f"{start_sec:.3f}",
            "-i", src,
            "-t", f"{duration:.3f}",
            "-vn",
            "-ac", "1",
            "-b:a", "64k",
            "-ar", "44100",
            out_path
        ]
        subprocess.run(cmd, check=True)
        print(f"  [OK] {out_name}  ({duration:.1f}s)")

    print(f"\nتمام شد! هر ۱۵ کلیپ قسمت ۶ به پوشه '{OUTPUT_DIR}/' اضافه شدند.")


if __name__ == "__main__":
    main()
