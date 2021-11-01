from browser import play
import asyncio

if __name__ == "__main__":
    link = input("Enter the link > ")
    points = input("Enter the points > ")
    asyncio.run(play(link, int(points)))
