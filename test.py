import asyncio
import aiohttp
import time

max_requests_per_second = 0.5
urls = [[
    'https://gist.github.com/agalea91/4cc329a1a1a13960c6d0e1df6a179f60',
    'https://www.reddit.com/',
    'https://www.ikea.com/ca/en/catalog/categories/departments/hallway/10456/',
],
[
    'https://github.com/pandas-dev/pandas/issues/11166',
    'https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04',
    'https://www.nike.com/language_tunnel',
]]

async def make_request(url):
    print('$$$ making request')
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as resp:
            status = resp.status
            text = await resp.text()
            print('### got page data')
            return url, status, text


async def app():
    results = []
    for i, batch in enumerate(urls):
        t_0 = time.time()
        print(f'batch {i}')
        tasks = [asyncio.ensure_future(make_request(url)) for url in batch]
        for t in tasks:
            d = await t
            results.append(d)
        t_1 = time.time()

        # Throttle requests
        batch_time = (t_1 - t_0)
        batch_size = len(batch)
        wait_time = (batch_size / max_requests_per_second) - batch_time
        if wait_time > 0:
            print(f'Too fast! Waiting {wait_time} seconds')
            time.sleep(wait_time)

    return results


if __name__ == '__main__':
    results = asyncio.run(app())
    print(results)