import json
import os
import random

__all__ = ['Jsoner']


class Jsoner:
    def __init__(self, fn: str):
        assert os.path.exists(fn), f"{fn} not exist"
        self._obj = json.load(open(fn))

    def Type(self, display: bool = True):
        if display:
            print(f"Type of json object is {type(self._obj)}")
        return type(self._obj)

    def first(self, display: bool = True):
        assert isinstance(self._obj, list), f"first method must be used for list, but got {type(self._obj)}"
        return self._obj[0]

    def keys(self) -> list:
        assert isinstance(self._obj, dict), f"keys method must be used for dict, but got {type(self._obj)}"
        return list(self._obj.keys())

    def sample(self, k=10):
        """
        k is length
        """
        if isinstance(self._obj, list):
            return random.sample(self._obj, k)
        elif isinstance(self._obj, dict):
            sampler_keys = random.sample(list(self._obj.keys()), 10)
            sampler_vals = [self._obj[k] for k in sampler_keys]
            sampler = dict(zip(sampler_keys, sampler_vals))
            return sampler


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
