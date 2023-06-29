# -*- coding: utf-8 -*-
# Author WhaleFall / ChatGPT
# Mdbook auto summary
# summary all .md files in a Mdbook folder

import argparse
import os
import re
from pathlib import Path

import os


import os


def generate_summary(root_dir, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = []

    summary = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 排除指定的目录
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]

        # 获取当前目录相对于根目录的层级
        level = dirpath.replace(root_dir, "").count(os.sep)
        dirpath = dirpath.replace("\\", "/")

        # 添加当前目录到摘要
        if level == 0:
            # summary.append(f"- [{os.path.basename(dirpath)}]({dirpath}/)")
            pass
        else:
            summary.append(
                f"{'    ' * (level-1)}- [{os.path.basename(dirpath)}]({dirpath}/)"
            )

        # 添加当前目录下的文件到摘要
        for filename in filenames:
            if level == 0:
                break
            if filename.endswith(".md"):
                summary.append(
                    f"{'    ' * (level + 1)}- [{os.path.splitext(filename)[0]}]({os.path.join(dirpath, filename)})"
                )

    return "\n".join(summary)


if __name__ == "__main__":
    # 设置根目录和要排除的目录
    root_dir = "."
    except_dirs = [".obsidian", ".git", ".trash", ".vscode", "src", ".src", ".github"]

    # 生成 SUMMARY.md 文件内容
    summary_content = generate_summary(root_dir, except_dirs)

    # 将内容写入 SUMMARY.md 文件
    with open(os.path.join(root_dir, "SUMMARY.md"), "w", encoding="utf8") as f:
        f.write("# 落落的Notes\n\n")
        f.write(summary_content)
