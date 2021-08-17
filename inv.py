zones = "abcdefghijklmnopqr"

inv = "invariant "

import os

print(len(zones))

with open('inv.txt','w') as ofile:
    for y in range(len(zones)):
        for z in range(y+1,len(zones)):
            print(zones[y] + " with " + zones[z])
            inv = inv + "(zone(" + zones[y] + ").ok & zone(" + zones[z] + ").ok) -> ("
            for i in range(1,18):
                inv = inv + "zone(" + zones[y] + ").c" + str(i).zfill(2) + " ~= zone(" + zones[z] + ").c" + str(i).zfill(2) + " | "
            inv = inv + "zone(" + zones[y] + ").c18 ~= zone(" + zones[z] + ").c18) "
            # print(inv)
            ofile.write(inv + "\n")
            inv = "invariant "
        
        # invariant (zone(test).ok & zone(b).ok) -> (zone(test).c01 ~= zone(b).c01 | zone(test).c02 ~= zone(b).c02 | zone(test).c03 ~= zone(b).c03 | zone(test).c04 ~= zone(b).c04 | zone(test).c05 ~= zone(b).c05 | zone(test).c06 ~= zone(b).c06 | zone(test).c07 ~= zone(b).c07 | zone(test).c08 ~= zone(b).c08 | zone(test).c09 ~= zone(b).c09 | zone(test).c10 ~= zone(b).c10 | zone(test).c11 ~= zone(b).c11 | zone(test).c12 ~= zone(b).c12 | zone(test).c13 ~= zone(b).c13 | zone(test).c14 ~= zone(b).c14 | zone(test).c15 ~= zone(b).c15 | zone(test).c16 ~= zone(b).c16)
