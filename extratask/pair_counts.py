def count_pairs(L1):
    assert type(L1)==list

    ### BEGIN SOLUTION
    # For one approach, see the "reference" in CPSol.py, included in this repo.

    # Here is a faster method:
    from collections import Counter
    counts = Counter(L1)
    print(counts)
    unique_items = sorted(counts.keys())
    print(unique_items[:-1])
    unique_pairs = zip(unique_items[1:], unique_items[:-1])
    print(unique_pairs)
    unit_diff_combos = [counts[b]*counts[a] for b, a in unique_pairs if (b-a) == 1]
    print(unit_diff_combos )
    # return sum(unit_diff_combos)

L1=[1,2,3,4,5,6,7,8,9]
print(count_pairs(L1))