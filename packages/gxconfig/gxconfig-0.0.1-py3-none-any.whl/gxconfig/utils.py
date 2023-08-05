from typing import NamedTuple
import types
import toml


def nt2d(nt: NamedTuple) -> dict:
    """
    NamedTuple to dict
    Args:
        nt: Namedtuple type object

    Returns:

    """
    res = dict()
    od = nt._asdict()  # order dict
    for k in od.keys():
        if isinstance(od[k], tuple):
            res[type(od[k]).__name__] = nt2d(od[k])
        else:
            res[k] = od[k]
    return res


def save_toml(cfg: NamedTuple, file_name: str = ""):
    d = nt2d(cfg)
    toml.dump(d, open(file_name, 'w'))


def load_toml(file_name: str, nt) -> NamedTuple:
    """

    :param file_name: load from file
    :param nt: Nametuple type
    :return: Nametuple Object
    """
    d = toml.load(open(file_name))
    return nt(**d)

