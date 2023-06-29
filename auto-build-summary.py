# -*- coding: utf-8 -*-
# Author WhaleFall / ChatGPT
# Mdbook auto summary
# summary all .md files in a Mdbook folder

import os


def generate_summary(directory, ignore_dirs):
    with open("SUMMARY.md", "w", encoding="utf-8") as f:
        f.write("# 落落的Notes\n\n")

        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]

            level = root.replace(directory, "").count(os.sep)
            indent = "  " * level

            if level == 0:
                title = "落落的Notes"
            else:
                title = os.path.basename(root)

            f.write("{}- [{}]({}/README.md)\n".format(indent, title, root))

            for file in files:
                if file.endswith(".md") and file != "README.md":
                    filename = os.path.splitext(file)[0]
                    f.write("{}  - [{}]({}/{})\n".format(indent, filename, root, file))


if __name__ == "__main__":
    directory = "."  # 指定要生成 SUMMARY.md 的目录
    ignore_dirs = [
        ".obsidian",
        ".git",
        ".trash",
        ".vscode",
        "src",
        ".src",
        ".github",
        "book",
        "assets",
        "templates",
    ]  # 指定要忽略的目录列表

    generate_summary(directory, ignore_dirs)
