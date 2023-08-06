import random
import json


def sampler(file: str, prefix: str = "sample", cnt: int = 5):
    """json sampler
    :param file:
    :param prefix:
    :return:
    """
    raw_data = json.load(open(file))
    if isinstance(raw_data, list):
        #         random choice 50 pieces of data
        assert len(raw_data) > cnt, f"Cannot provide enough data! Total " \
                                    f"{len(raw_data)}in json, but cnt is {cnt}"
        raw_data = random.shuffle(raw_data)
        tar = random.sample(raw_data, cnt)
        json.dump(tar, open(f"{file.split('.')[0]}-{prefix}.json", 'w'))
    else:
        print("Only list like json can be sampled")


def analyzer(file: str, prefix="ana"):
    """Analyze json key and value
    :param file: json file
    """
    data = json.load(open(file))
    target = open(f"{file.split('.')[0]}-{prefix}.txt", 'w')
    if isinstance(data, list):
        line = f"------file type\tlist------"
        item = data[0]
        print(line, file=target)
        line = f"------One item type\t{item.__class__}------"
        print(line, file=target)
        if isinstance(item, dict):
            line = "key_type\tkey\tvalue_type\tvalue"
            print(line, file=target)
            for k in item.keys():
                line = f"{k.__class__}\t{k}\t{item[k].__class__}\t{item[k]}"
                print(line, file=target)
    target.close()
