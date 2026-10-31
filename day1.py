data = {"Mabel":654, "Prince":456, "Aba":9876}

for name, det in data.items():
    print(name, det)

def average(num):
    return sum(num)/len(num)

print("Average:", average(data.values()))

max_val = float()
max_name = None
for name, num in data.items():
    if num>max_val:
        max_val=num
        max_name=name

print(max_val, max_name)
