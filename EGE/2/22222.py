print("w y x z ")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (((x or y) <= z) or ((y==w) or z)) == 0:
                    print( w,y,x,z)



