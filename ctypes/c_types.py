from ctypes import *

msvcrt = cdll.msvcrt 
message = "Hello from ctypes"
msvcrt.printf(" ss", message)