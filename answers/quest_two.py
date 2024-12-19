import json

if __name__ == '__main__':
    with open("assets/addresses.json", "r") as f:
        data = json.load(f)
    list1 = data.get("addresses")
    assert list1 is not None, "file could not be read, check with os.path.exists()"
    arranged = dict()
    for i in list1:
        if i[1][0:2] == "新疆" or i[1][0:2] == "宁夏":
            if i[1][0:2] in arranged:
                arranged[i[1][0:2]].append(i)
            else:
                arranged[i[1][0:2]] = [i]
        else:
            if i[1][0:3] in arranged:
                arranged[i[1][0:3]].append(i)
            else:
                arranged[i[1][0:3]] = [i]

    with open("output/res.json", "w") as fp:
        json.dump(arranged, fp, ensure_ascii=False, indent=4)
    # print(dict1)
