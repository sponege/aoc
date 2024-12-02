#!/bin/python3
import random
## make 1000 random integers from -100 to 100

a = [str(random.randint(-100, 100)) for _ in range(1000)]

## remove all zeroes from list
a = [x for x in a if x != '0']

## add one zero at a random position
a.insert(random.randint(0, len(a)), '0')

# write a file with those integers separated by newlines
open('20.gen-input.txt', 'w').write('\n'.join(a))
