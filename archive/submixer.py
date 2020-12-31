#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import sys


def main():
    print(sys.argv)
    if not len(sys.argv) > 2:
        print("failed due to insufficent inputs")
        return
    if sys.argv[1].endswith(".srt"):
        subtitle = sys.argv[1]
        main_file = sys.argv[2]
    elif sys.argv[2].endswith(".srt"):
        subtitle = sys.argv[2]
        main_file = sys.argv[1]
    if len(sys.argv) == 4:
        outfile = sys.argv[3]
    else:
        outfile = main_file.rsplit(".", 1)
        outfile.insert(1, "-sub.")
        outfile = "".join(outfile)
    print(outfile)
    subprocess.Popen(
        [
            "ffmpeg",
            "-i",
            main_file,
            "-i",
            subtitle,
            "-c",
            "copy",
            "-c:s",
            "mov_text",
            outfile,
        ],
    )
    print("muxed successfully")


if __name__ == "__main__":
    main()
