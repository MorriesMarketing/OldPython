import asyncio
import time
import tracemalloc
from time import sleep
import requests
from bs4 import BeautifulSoup

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def soups():

    Domain = 'https://www.jmlexus.com/'
    page = requests.get(f'{Domain}sitemap.xml')
    soup = BeautifulSoup(page.content, 'xml')
    pages = []
    for div in soup.find_all('loc'):
        try:
            string = str(div)
            string = string.split('<loc>')
            string = string[1].split('</loc>')
            string = string[0]
            if f'{Domain}new' in string or f'{Domain}used' in string or f'{Domain}inventory/' in string or f'{Domain}VehicleDetails/' in string:
                pages.append(string)
        except:
            pass
    print(f'{Domain} - VDPs Found: {len(pages)}')
    return f'    {Domain} - VDPs Found: {len(pages)}'

async def worlds(letter):
    #worlds = ['World1','World2','World3','World4','World5','World6','World7']
    #for x in worlds:
    #    
    #    print(f'{letter} {x}')
    #    if x == 'World4':
    task = asyncio.create_task(soups())
    print(await task)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")
    letters = range(0,100)
    #await asyncio.gather(map_list)
    print(f"started at {time.strftime('%X')}")
    for future in asyncio.as_completed(map(worlds,letters)):        
        await future
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
