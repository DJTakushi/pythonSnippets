#!/usr/bin/python

import sys
print('Number of arguments:'+str(len(sys.argv))+'arguments.')
print('Argument List:'+str(sys.argv))

failCount = int(sys.argv[1])
passCount = int(sys.argv[2])
product = failCount/(failCount+passCount)

print("product = ", product)