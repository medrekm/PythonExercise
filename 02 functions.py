#function testing
def noValue(param):
    return param.__len__()

def maxValue(param):
    max=param[0]
    for i in range(len(param)):
        if max<param[i]:
            max=param[i]
    return(max)

x=[1,2,3,2,1,22]

print("liczba elementów w tablicy: ",noValue(x))
print("maksymalny element w tablicy: ",maxValue(x))