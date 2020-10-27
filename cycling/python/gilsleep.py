import ctypes

def compute(n):
    # Use libc in ctypes "PyDLL" mode, which prevents CPython from
    # releasing the GIL during procedure calls (unlike time.sleep()).
    libc_py = ctypes.PyDLL("libc.so.6")
    libc_py.usleep(n*1000000)
