with open("input1.txt", "r") as f:
    years = list(f)
    for i in range(len(years)):
        for j in range(i + 1, len(years)):
            if (int(years[i]) + int(years[j]) == 2020):
                print(years[i], years[j])
                print(int(years[i]) * int(years[j]))

    for i in range(len(years)):
        for j in range(i + 1, len(years)):
            for k in range(j + 1, len(years)):
                if (int(years[i]) + int(years[j]) + int(years[k]) == 2020):
                    print(years[i], years[j], years[k])
                    print(int(years[i]) * int(years[j]) * int(years[k]))

