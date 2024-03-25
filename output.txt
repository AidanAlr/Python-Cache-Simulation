/usr/local/bin/python3.12 /Users/aidanalrawi/PycharmProjects/Python-Cache-Simulation/main.py
Cache initialized
Read address 5 -> tag=0, slot=0, offset=5 (Cache miss)
Retrieving block starting at 0 from memory...
Data:  5


Read address 6 -> tag=0, slot=0, offset=6 (Cache hit)
Data:  6


Read address 7 -> tag=0, slot=0, offset=7 (Cache hit)
Data:  7


Read address 14c -> tag=1, slot=4, offset=c (Cache miss)
Retrieving block starting at 140 from memory...
Data:  4c


Read address 14d -> tag=1, slot=4, offset=d (Cache hit)
Data:  4d


Read address 14e -> tag=1, slot=4, offset=e (Cache hit)
Data:  4e


Read address 14f -> tag=1, slot=4, offset=f (Cache hit)
Data:  4f


Read address 150 -> tag=1, slot=5, offset=0 (Cache miss)
Retrieving block starting at 150 from memory...
Data:  50


Read address 151 -> tag=1, slot=5, offset=1 (Cache hit)
Data:  51


Read address 3a6 -> tag=3, slot=a, offset=6 (Cache miss)
Retrieving block starting at 3a0 from memory...
Data:  a6


Read address 4c3 -> tag=4, slot=c, offset=3 (Cache miss)
Retrieving block starting at 4c0 from memory...
Data:  c3


-------------------------------Displaying cache------------------------------
   slot  valid tag  dirty                                          block_data
0     0      1   0      0    0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
1     1      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
2     2      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
3     3      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
4     4      1   1      0    40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f
5     5      1   1      0    50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f
6     6      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
7     7      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
8     8      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
9     9      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
10    a      1   3      0    a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af
11    b      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
12    c      1   4      0    c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 ca cb cc cd ce cf
13    d      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
14    e      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
15    f      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0


Write 99 to address 14c -> tag:  1 slot:  4 offset:  c
Cache hit
Data: 99 written to cache


Write 7 to address 63b -> tag:  6 slot:  3 offset:  b
Cache miss
Retrieving block starting at  630  from memory...
Data: 7 written to cache


Read address 582 -> tag=5, slot=8, offset=2 (Cache miss)
Retrieving block starting at 580 from memory...
Data:  82


-------------------------------Displaying cache------------------------------
   slot  valid tag  dirty                                          block_data
0     0      1   0      0    0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
1     1      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
2     2      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
3     3      1   6      1    30 31 32 33 34 35 36 37 38 39 3a 7  3c 3d 3e 3f
4     4      1   1      1    40 41 42 43 44 45 46 47 48 49 4a 4b 99 4d 4e 4f
5     5      1   1      0    50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f
6     6      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
7     7      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
8     8      1   5      0    80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f
9     9      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
10    a      1   3      0    a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af
11    b      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
12    c      1   4      0    c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 ca cb cc cd ce cf
13    d      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
14    e      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
15    f      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0


Read address 348 -> tag=3, slot=4, offset=8 (Cache miss)
Dirty bit found in slot:  4
Writing block 140 to memory...
Retrieving block starting at 340 from memory...
Data:  48


Read address 3f -> tag=0, slot=3, offset=f (Cache miss)
Dirty bit found in slot:  3
Writing block 630 to memory...
Retrieving block starting at 30 from memory...
Data:  3f


-------------------------------Displaying cache------------------------------
   slot  valid tag  dirty                                          block_data
0     0      1   0      0    0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
1     1      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
2     2      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
3     3      1   0      0    30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f
4     4      1   3      0    40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f
5     5      1   1      0    50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f
6     6      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
7     7      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
8     8      1   5      0    80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f
9     9      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
10    a      1   3      0    a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af
11    b      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
12    c      1   4      0    c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 ca cb cc cd ce cf
13    d      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
14    e      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
15    f      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0


Read address 14b -> tag=1, slot=4, offset=b (Cache miss)
Retrieving block starting at 140 from memory...
Data:  4b


Read address 14c -> tag=1, slot=4, offset=c (Cache hit)
Data:  99


Read address 63f -> tag=6, slot=3, offset=f (Cache miss)
Retrieving block starting at 630 from memory...
Data:  3f


Read address 83 -> tag=0, slot=8, offset=3 (Cache miss)
Retrieving block starting at 80 from memory...
Data:  83


-------------------------------Displaying cache------------------------------
   slot  valid tag  dirty                                          block_data
0     0      1   0      0    0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
1     1      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
2     2      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
3     3      1   6      0    30 31 32 33 34 35 36 37 38 39 3a 7  3c 3d 3e 3f
4     4      1   1      0    40 41 42 43 44 45 46 47 48 49 4a 4b 99 4d 4e 4f
5     5      1   1      0    50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f
6     6      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
7     7      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
8     8      1   0      0    80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f
9     9      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
10    a      1   3      0    a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af
11    b      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
12    c      1   4      0    c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 ca cb cc cd ce cf
13    d      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
14    e      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
15    f      0   0      0    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0



Process finished with exit code 0
