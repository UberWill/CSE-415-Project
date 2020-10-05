
def testy(a1, a2):

    if (len(a2) % len(a1) != 0):
        return False


    for i in range(int(len(a2) / len(a1))):
            for j in range(len(a1)):
                if (a1[j] != a2[j + (len(a1) * i)]):
                    return False



    return True

print(testy([1,2], [1,2,1,2,1,2,1,2]))

