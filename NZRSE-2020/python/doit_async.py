
import asyncio
from gilsleep import compute

async def _pre(arg):
   print("PRE>", arg)
   compute(1)
   print("<PRE", arg)

async def _post(arg):
   print("POST>", arg)
   compute(1)
   print("<POST", arg)

async def _read_file(arg):
   print("READ>", arg)
   await asyncio.sleep(5)
   print("<READ", arg)

async def proc(arg):
   await _pre(arg)
   await _read_file(arg)
   await _post(arg)
   return f"[{arg}]"
