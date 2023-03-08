import time
import asyncio


def sleep_two_seconds():
    print("sleep")
    time.sleep(1)
    print("wake up")


async def main():
    print("start")
    await sleep_two_seconds()
    print("end")


asyncio.run(main())
