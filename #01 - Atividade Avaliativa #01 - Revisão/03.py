
from findnonce import *

string = "Olá, mundo!"

dataToHash = string.encode("utf-8")
BitsToBeZero = 3

findnonce(dataToHash, BitsToBeZero)