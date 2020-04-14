import yaml
import importlib

def from_spec(fname):
    spec = yaml.load(open(fname))
    print(spec)
    parse_spec(spec)

def parse_spec(spec):
    for mod in spec:
        mod = importlib.import_module(mod)
        print(mod.TEST)
