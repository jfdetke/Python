import asyncio

import aiohttp
async def fetch(url, session):
    async with session.get(url) as response:
        resp =  await response.text()
        return (response.status, response.text())

async def main():
    url_list=["http://google.com","http://yahoo.com","http://groupon.com"]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in url_list:
            task = asyncio.ensure_future(fetch(i,session))
            tasks.append(task)
        print ("Tasks :: {}".format(len(tasks)))
        responses = await asyncio.gather(*tasks)
    for i in responses:
        print ("status code {}".format(i[0]))
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
