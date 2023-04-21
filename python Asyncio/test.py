# import asyncio


# async def c():
#     retrieved_data = None
#     previous_page_size = 10
#     while True:
#         page_size = retrieved_data
#         if page_size is None:
#             page_size = previous_page_size


# async def f():
#     try:
#         while True:
#             d = c()
#             await d
#     except asyncio.CancelledError:
#         print("I was canceeled!")
#     else:
#         return 111


# coro = f()
# print(coro.send(None))
# print(coro.send(5))
# print("hello")
# coro.throw(asyncio.CancelledError)


import asyncio


async def start_1():
    print("hello_1")


async def start_2():
    await start_1()
    print("hello_2")


async def main():
    await start_2()
    print("finish")


asyncio.run(main())