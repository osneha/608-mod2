import statistics

values = [13, 16, 14, 18, 13, 10, 15, 15, 22, 9, 18, 18, 13, 17, 14, 10, 18, 16, 15, 18, 12, 16, 13, 12, 12, 9, 13, 17, 14, 13, 25, 16, 20, 23, 15, 10, 23, 14, 16, 18, 19, 22, 13, 16, 20, 16, 15, 12, 12, 13, 17, 15, 18, 13, 13, 17, 15, 15, 20, 15, 13, 16, 14, 18, 15, 15, 19, 17, 16, 21, 17, 20, 19, 14, 16, 16, 17, 19, 17, 23, 14, 20, 17, 13, 15, 21, 21, 23, 17, 22, 9, 11, 21, 12, 20, 15, 22, 15, 20, 15]

count = len(values)

print("Count = ", count)
print("Sum = ",sum(values))

mean = statistics.mean(values)
print("Mean = ", mean )

median = statistics.median(values)
print("Median = ", median )

mode = statistics.mode(values)
print("Mode = ", mode )

