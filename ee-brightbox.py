# The EE Brightbox uses a 6 character lower alpha numeric password
# 36^6 = 2,176,782,336 permutations.
# At 1 byte per character a wordlist will be ~12GiB
# Source: http://e-gain.s3.amazonaws.com/external/content/Internet/Broadband/Images/Arcadyan2_030.gif

charset = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
        '1', '2', '3', '4', '5', '6', '7', '8', '9'])

from itertools import product
result = product(charset, repeat=6)

f = open('ee-brightbox.txt', 'w')
for r in result:
    f.write(''.join(r) + '\n')
f.close

