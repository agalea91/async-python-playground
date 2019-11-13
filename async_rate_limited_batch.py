import click
import asyncio
import time
import numpy as np

batch_size = 5
max_requests_per_second = 0.5

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_batches())

async def run_batches():
    data = np.random.randn(batch_size, 20)

    for i, batch in enumerate(data):
        t_0 = time.time()
        print('batch {}'.format(i))
        tasks = [asyncio.ensure_future(async_request_analogue()) for x in data]
        for t in tasks:
            await t
            process()
        t_1 = time.time()
        batch_time = (t_1 - t_0)
        wait_time = (batch_size / max_requests_per_second) - batch_time
        if wait_time > 0:
            print('Too fast! Waiting {} seconds'.format(wait_time))
            time.sleep(wait_time)

def process():
    print('### processing response (0.3 second cpu time)')
    time.sleep(0.3)


async def async_request_analogue():
    print('$$$ making request')
    await asyncio.sleep(3)
    return True


if __name__ == '__main__':
    main()