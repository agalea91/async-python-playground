import asyncio
import aiohttp
import time
import pandas as pd

delay_per_request = 0.5
urls = [
    'https://gist.github.com/agalea91/4cc329a1a1a13960c6d0e1df6a179f60',
    'https://www.reddit.com/',
    'https://www.ikea.com/ca/en/catalog/categories/departments/hallway/10456/',
    'https://github.com/pandas-dev/pandas/issues/11166',
    'https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04',
    'https://www.nike.com/language_tunnel',
]

def main():
    # loop = asyncio.get_event_loop()
    # results = loop.run_until_complete(app())
    results = asyncio.run(app())
    print(pd.DataFrame(results, columns=['url', 'status_code', 'text', 'text_length']))

async def app():
    tasks = []
    for url in urls:
        tasks.append(asyncio.ensure_future(make_request(url)))
        await asyncio.sleep(delay_per_request)

    results = await asyncio.gather(*tasks)
    return results

def get_length(text):
    print(f'Text length = {len(text)}')
    return len(text)

async def make_request(url):
    print('$$$ making request')
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as resp:
            status = resp.status
            text = await resp.text()
            length = get_length(text)
            return url, status, text, length

if __name__ == '__main__':
    main()