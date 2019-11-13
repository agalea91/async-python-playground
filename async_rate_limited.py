import click
import asyncio
import time
import numpy as np

max_requests_per_second = 0.5

def main():
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(app())
    print(results)

async def app():
    data = np.random.randn(20)

    tasks = []
    for x in data:
        tasks.append(asyncio.ensure_future(async_request_analogue()))
        await asyncio.sleep(0.1)

    results = await asyncio.gather(*tasks)
    return results


def process():
    print('### processing response (0.3 second cpu time)')
    time.sleep(0.3)

async def async_request_analogue():
    print('$$$ making request')
    await asyncio.sleep(3)
    print('@@@ done request')
    return True


if __name__ == '__main__':
    main()