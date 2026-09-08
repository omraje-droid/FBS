1. # 1.Convert the time entered in hh,min and sec into seconds.
h = int(input("Enter hours :"))
m = int(input("Enter minits :"))
s = int(input("Enter second :"))
# convert hours minits into seconds
sec_1 = h * 60 * 60
sec_2 = m * 60
sec_3 = s

total = sec_1 + sec_2 + sec_3

print(f"Converting time {h} hours {m} minutes {s} seconds into seconds : {total} .")
