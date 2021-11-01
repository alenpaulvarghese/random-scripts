# (c) AlenPaulVarghese
# -*- coding: utf-8 -*-

from http.client import BadStatusLine
from pyppeteer.browser import Browser
from pyppeteer import launch
import asyncio


async def launch_browser(retry=False) -> Browser:
    try:
        browser = await launch(
            headless=False,
            logLevel=50,
            handleSIGINT=False,
            args=[
                "--no-sandbox",
                "--single-process",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--no-zygote",
            ],
        )
        return browser
    except BadStatusLine as e:
        if not retry:
            await asyncio.sleep(1.5)
            return await launch_browser(True)
        elif retry:
            print("Launching browser failed due to {}, exiting...".format(e))


async def play(link: str, points: int):
    browser = await launch_browser()
    page = await browser.newPage()
    await page.goto(link)
    await page.click("div.icon_play")
    print("X\t OP\tY\tGUESS\tANSWER".center(28))
    for _ in range(points):
        answer = False
        x, op, y, guess = await asyncio.gather(
            page.querySelectorEval("span#task_x", "node => node.innerText"),
            page.querySelectorEval("span#task_op", "node => node.innerText"),
            page.querySelectorEval("span#task_y", "node => node.innerText"),
            page.querySelectorEval("span#task_res", "node => node.innerText"),
        )
        if op == "+":
            answer = int(guess) == int(x) + int(y)
        elif op == "–":
            answer = int(guess) == int(x) - int(y)
        elif op == "/":
            answer = int(guess) == int(x) / int(y)
        elif op == "×":
            answer = int(guess) == int(x) * int(y)
        print(
            "{} {} {} {} {}".format(
                x.center(7),
                op.center(7),
                y.center(7),
                guess.center(7),
                ("✅" if answer else "❌").center(7),
            )
        )
        await (
            page.click("div.button_correct")
            if answer
            else page.click("div.button_wrong")
        )
        # uncomment below code to watch it slow
        # await asyncio.sleep(1)

    await asyncio.sleep(10)
    await page.close()
    await browser.close()
