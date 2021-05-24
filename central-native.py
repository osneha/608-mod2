from typing import Counter


values = [47, 95, 88, 73, 88, 84]

values.sort()
count = (len(values))
print("Count = ", count)

print("Sum = ",sum(values))

print("Mean = ", sum(values)/len(values) )

if (count % 2==0):
    median1 = values[count//2]
    median2 = values[count//2 - 1]
    median = (median1+median2)/2

else:
    median = values[count//2]

print("Median = ", str(median))

data = Counter(values)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == count:
    get_mode = "No mode found"
else:
    get_mode = "Mode = " + ', '.join(map(str, mode))

    print(get_mode)