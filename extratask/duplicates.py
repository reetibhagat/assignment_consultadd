assignments = {"Monday" : ["Jeh", "Ben", "Chinmay", "Rachel"],
               "Tuesday" : ["Rachel", "Samuel", "Evan", "Raghav"],
               "Wednesday" : ["Evan", "Samuel", "Michael", "Chinmay"],
               "Thursday" : ["Jeh", "Michael", "Ben", "Evan"],
               "Friday" : ["Rachel", "Shishir", "Samuel", "Ben"],
               "Saturday" : ["Yandi", "Michael", "Chinmay", "Samuel"],
               "Sunday" : ["Evan", "Chinmay", "Jeh", "Rachel"]
               }

from collections import defaultdict
def invert_dict(d):
    l = []
    for k, v in d.items():
        l.append(v)
    flatten_l = [i for e in l for i in e]
    flatten_l = set(flatten_l)
    d_inv = defaultdict(list)
    for e in flatten_l:
        for k, v in d.items():
            if e in v:
                d_inv[e].append(k)
    return dict(d_inv)

print(invert_dict(assignments))