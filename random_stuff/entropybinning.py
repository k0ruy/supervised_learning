import math as m

import numpy as np


def entropy(ds, dim=0):
    classes = {}
    probabilities = []
    if dim == 1:
        ds = ds.transpose()
    num_elements = len(ds[1, :])
    for val in ds[1, :]:
        key = int(val)
        if key not in classes.keys():
            classes[key] = 1
        else:
            classes[key] += 1
    for val in classes.values():
        probabilities.append(val / num_elements)
    ntrpy = 0.0
    for p in probabilities:
        ntrpy -= (p * (m.log2(p) if p > 0.0 else 0.0))
    return ntrpy


def entropy_bin(ds, split, dim=0):
    if dim == 1 or ds.shape[1] == 2:
        ds = ds.transpose()
    num_elements = len(ds[1, :])
    ds_split = ds[:, ds[0, :] < split[0]]
    n1, e = len(ds_split[1, :]), entropy(ds_split)
    ntrpy_bin = (len(ds_split[1, :]) / num_elements) * entropy(ds_split)
    for i in range(len(split)):
        upper_split = split[i + 1] if i + 1 < len(split) else float('inf')
        m1, m2 = ds[0, :] >= split[i], ds[0, :] < upper_split
        ds_split = ds[:, np.array([(b1 and b2) for b1, b2 in zip(m1, m2)])]
    n1, e = len(ds_split[1, :]), entropy(ds_split)
    ntrpy_bin += (len(ds_split[1, :]) / num_elements) * entropy(ds_split)
    return ntrpy_bin


def spliff(sparr, splits, indices, offset, n_splits):
    nsplits = n_splits - 1
    if nsplits == 0:
        return [((indices + (offset + i,)), (splits + (s,))) for i, s in enumerate(sparr)]
    lx0 = []
    for i in range(len(sparr) - (nsplits)):
        for s in spliff(sparr[i + 1:], splits + (sparr[i],), indices + (offset + i,), offset + i + 1, nsplits):
            lx0.append(s)
    return lx0


if __name__ == "__main__":
    x = input(
        "Insert the x-values (the ones to be splitted)\n[either comma or whitespace separated, but not both: 1.2 3.5 4.6 2.4]:\n")
    # x = "53 56 57 63 66 67 67 67 68 69 70 70 70 70 72 73 75 75 76 76 78 79 80 81"
    x = x.split(',' if ',' in x else ' ')
    y = input("Insert the y-values\n[either comma or whitespace separated, but not both: 1.2 3.5 4.6 2.4]:\n")
    # y = "Y Y Y N N N N N N N N Y Y Y N N N Y N N N N N N"
    y = y.upper()
    y = y.split(',' if ',' in x else ' ')
    x = [float(xval) for xval in x]
    ykeys = list(set(y))
    y = [float(ykeys.index(yval)) for yval in y]
    dataset = np.array(sorted(zip(x, y), key=lambda t: t[0], reverse=False)).transpose()

    entropy_ds = entropy(dataset)
    print(dataset)

    splits = [(dataset[0, i] + dataset[0, i + 1]) / 2.0 for i in range(len(dataset[1, :]) - 1) if
              dataset[0, i] != dataset[0, i + 1]]
    splits = np.array((splits, [entropy_ds] * len(splits)))
    i_max, entropy_gain_max = 0, 0.0
    split_permutations = spliff(splits[0, :], (), (), 0, len(ykeys) - 1)
    for si, st in split_permutations:
        new_entropy = entropy_ds - entropy_bin(dataset, st)
        splits[1, si[0]] = new_entropy
        if new_entropy > entropy_gain_max:
            i_max, entropy_gain_max = si, new_entropy

    print("Total Entropy:", entropy_ds)

    print(f"ideal split is at: {splits[0, i_max]}  with an entropy of: {entropy_gain_max}\n\n")
    print("\n\nEntropy Gain of all bins:")
    print(splits.transpose())
