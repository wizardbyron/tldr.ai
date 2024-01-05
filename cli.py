#!/usr/bin/env python3
import fire
import time

from tldr.tldr import tldr_from_url

def cli(url: str) -> None:

    start_time = time.time()
    output = tldr_from_url(url)
    end_time = time.time()
    duration = end_time - start_time

    print(f"{output}\n[生成结果用时：{duration:.2f}秒]")


if __name__ == "__main__":
    fire.Fire(cli)
