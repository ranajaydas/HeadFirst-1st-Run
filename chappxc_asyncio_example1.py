"""A program I found on YouTube about asyncio."""
import asyncio
import random


async def my_coroutine(num: int):
    process_time = random.randint(1, 5)     # Create a random delay between 1s to 5s
    await asyncio.sleep(process_time)
    print('Co-routine {} completed after {} second(s)'.format(num, process_time))


async def main():
    tasks = [asyncio.ensure_future(my_coroutine(i)) for i in range(10)]
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
