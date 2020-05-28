#top 3 itemy

items = {"item 1": 45.50, "item 2":35, "item 3": 41.30, "item 4":55, "item 5 ": 24}

posortowane = sorted(items.items(), key=lambda x: (-x[1],x[0]))

for i in range(0,3):
    print(posortowane[i])
