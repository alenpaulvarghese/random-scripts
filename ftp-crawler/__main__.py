from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import List
import aiohttp
import asyncio


__link__ = ""


async def link_generator(link: str, session: aiohttp.ClientSession) -> list:
    primary, tasks = [], []
    async with session.get(link) as response:
        soup = BeautifulSoup(await response.text(), "lxml")
    a_tags: List[Tag] = soup.find_all("a")
    for tags in a_tags:
        href: str = tags.get("href")
        if href is None:
            continue
        if not href.endswith("/"):
            primary.append(link + href)
        else:
            tasks.append(link_generator(link + href, session))
    if len(tasks) != 0:
        finished_task = await asyncio.gather(*tasks)
        if len(finished_task) != 0:
            primary.append(finished_task)
    return primary


async def main():
    async with aiohttp.ClientSession() as session:
        with open("links.txt", "a") as writer:
            writer.writelines(str(x)+"\n" for x in await link_generator(__link__, session))


if __name__ == "__main__":
    asyncio.run(main())
