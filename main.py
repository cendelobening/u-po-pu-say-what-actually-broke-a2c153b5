import os

LINE = "Your session timed out while you typed, so your entire form just went to the great unsaved draft in the sky. Log back in and retype it — shorter this time."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
