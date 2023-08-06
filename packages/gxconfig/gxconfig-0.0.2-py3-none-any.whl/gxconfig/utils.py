from typing import NamedTuple
import types
import toml

__all__ = ['load_toml', 'save_toml']


def nt2d(nt: NamedTuple, key_mapping: dict = None) -> dict:
    """
    :param key_mapping: key is from name_tuple,val is from dict key
    :param nt: name tuple

    """
    res = dict()
    od = nt._asdict()  # order dict
    if key_mapping is not None:
        for k in od.keys():
            if isinstance(od[k], tuple):
                key = type(od[k]).__name__
                if key in key_mapping.keys():
                    res[key_mapping[key]] = nt2d(od[k])
                else:
                    res[key] = nt2d(od[k])
            else:
                if k in key_mapping.keys():
                    key = key_mapping[k]
                    res[key] = od[k]
                else:
                    res[k] = od[k]
    else:
        #     key_map is none
        for k in od.keys():
            if isinstance(od[k],tuple):
                res[k] = nt2d(od[k])
            else:
                res[k] = od[k]
    return res


def save_toml(cfg: NamedTuple, file_name: str = "", key_mapping: dict = None):
    d = nt2d(cfg, key_mapping=key_mapping)
    toml.dump(d, open(file_name, 'w'))


def load_toml(file_name: str, nt, key_mapping: dict = None) -> NamedTuple:
    """
    :param file_name: load from file
    :param nt: Nametuple type
    :param key_mapping toml to NameTuple
    :return: Nametuple Object
    """
    d = toml.load(open(file_name))
    if key_mapping is None:
        return nt(**d)
    else:
        for key in d.keys():
            if key in key_mapping.keys():
                k = key_mapping[key]
                d[k] = d.pop(key)
        return nt(**d)


class Data(NamedTuple):
    root: str = "/home/gawainx/data"
    chkp: str = "chkp"


class Model(NamedTuple):
    embd_dim: int = 768
    hidden_dim: int = 5


class Config(NamedTuple):
    data: Data = Data()
    model: Model = Model()


if __name__ == '__main__':
    # key_map = dict()
    # key_map["Model"] = "model"
    # key_map["Data"] = "data"
    # res = load_toml("config.toml", Config)
    c = Config()
    save_toml(c,"cfg.toml")

    cfg = load_toml("cfg.toml", Config)
    print(cfg)
    # print(res)
