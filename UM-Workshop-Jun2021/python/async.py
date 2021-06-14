#!/usr/bin/env python

import asyncio
from doit_async import proc

async def main():
    print(await asyncio.gather(*[proc(i) for i in range(3)]))

if __name__ == "__main__":
   asyncio.run(main())
