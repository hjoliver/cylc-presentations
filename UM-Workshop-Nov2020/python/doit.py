
from time import sleep
from gilsleep import compute

# If read_file ties up the GIL time to completion is 21sec.

# Otherwise it is 10 sec, not 11, because 
# some of the compute can execute during the
# GIL-releasing time.sleep().

def _pre(arg):
   print("PRE", arg)
   compute(1)

def _post(arg):
   print("POST", arg)
   compute(1)

def _read_file(arg):
   print("READ", arg)
   #compute(5)
   sleep(5)

def proc(arg):
   _pre(arg)
   _read_file(arg)
   _post(arg)
   return f"[{arg}]"
