# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dict_deep']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dict-deep',
    'version': '3.1.1',
    'description': "Very simple deep_set and deep_get functions to access nested dicts (or any object) using 'dotted strings' as key.",
    'long_description': '## Description\n\nSimple functions to set or get values from a nested dict structure or in fact a deep structure of any object, because\nsince version 2 we no longer assume we are dealing with dicts.\n\nYou may use a custom accessor or pass your own getter, setter, deleter callables so that you can traverse a nested structure of any kind of \nobject.\n\nThis module DOES NOT implement dotted notation as an alternative access method for dicts.\nI generally do not like changing python dicts to enable dot notation, hence no available\npackage fitted my needs for a simple deep accessor.\n\nNotes:\nOften, you could use \'lambda o, k: o[k]\' as either the getter or the accessor. The only \'special\' thing about the \'getter\' function is that when it is\ninvoked with \'o\' being a list and \'k\' being a string, it will instead iterate over the list and call the accessor for each item in the list.\n\nIn a simplified way, this is how it works:\n\n1. The key is broken down into a list of keys: "customer.address.city" -> [\'customer\', \'address\', \'city\'] \n\n2. The list of keys is iterated over calling the getter for each key and the last value retrieved is returned.\n```\nfor k in keys:\n   o = getter(o, k)\n\nreturn o\n```\n\nYou see that getter could be as simple as \'lambda o, k: o[k]\'. However, by default the code uses a smarter getter as defined below,\nwhich tries to deal properly with lists.\n\n```\ndef default_getter(o, k):\n    if isinstance(o, list):\n        if isinstance(k, str) and not k.isdigit():\n            r = []\n            for i in o:\n                r.append(accessor(i, k))\n            return r\n        elif isinstance(k, str) and k.isdigit():\n            k = int(k)\n    \n    return accessor(o, k)\n```\n\n## Functions\n\n*deep_get* accepts:\n- o: required. Any object, usually a dictionary\n- k: required. The key or keys, must be a string or anything accepted by the list() constructor\n- accessor: optional, callable: Takes o, k (object and key) and returns the value. Default accessor is \'lambda: o, k: o[k]\'\n- getter: optional, callable. If getter is set, default is ignored. Takes an object and a key as arguments and returns a value\n- sep: optional, string: by default it is a dot \'.\', you can use anything the string function split will accept\n\nReturns o[k]\n\n\n*deep_set* accepts:\n- o: see \'deep_get\'\n- k: see \'deep_get\'\n- v: required, the value that will be set\n- accessor: optional, callable: see \'deep_get\'\n- getter: optional, callable: see \'deep_get\'\n- setter: optional, callable. A callable that takes 3 parameters: o, k, v - where o = any object, k = key, v = value\n- sep: optional, string: see \'deep_get\'\n\nNo return value\n\n\n*deep_del* accepts:\n- o: required: see \'deep_get\'\n- k: required: see \'deep_get\'\n- sep: optional, string: see \'deep_get\'\n- accessor: optional, callable: see \'deep_get\'\n- deleter: optional, callable: Takes 2 parameters: o, k (object and key). By default \'del o[k]\' is used.\n\nReturns a tuple:\n(True, <value of the entry that was deleted>) or\n(False, None)\n\n\n## Usage\n\n```\ni = 0\n\n# Alternative 1\ni += 1\no = {\'a\': {\'b\': {}}}\ndeep_set(o, "a.b.c", "Hello World")\nprint("{}: {}".format(i, deep_get(o, "a.b.c")))\n\n# Alternative 2\ni += 1\no = {}\ndeep_set(o, [\'a\', \'b\', \'c\'], "Hello World", accessor=lambda o, k: o.setdefault(k, dict()))\nprint("{}: {}".format(i, deep_get(o, "a.b.c")))\n\n# Alternative 3\ni += 1\no = {}\ndeep_set(o, "a->b->c", "Hello World", accessor=lambda o, k: o.setdefault(k, dict()), sep="->")\nprint("{}: {}".format(i, deep_get(o, "a->b->c", sep="->")))\n\n# Alternative 4\ni += 1\no = {}\ndeep_set(o, "a->b->c", "Hello World", getter=lambda o, k: o.setdefault(k, dict()), sep="->")\nprint("{}: {}".format(i, deep_get(o, "a->b->c", sep="->")))\n\n# Alternative 5\ni += 1\no = {}\nkeys = \'a.b.c\'\nkeys = keys.split()\n_ = deep_get(o=o, k=keys[0:-1], accessor=lambda o, k: o.setdefault(k, dict()), sep=".")\n_[keys[-1]] = "Hello World"\nprint("{}: {}".format(i, deep_get(o, keys)))\n\n# deep_del\ni += 1\no = {}\ndeep_set(o, "1.1.1", \'a\', accessor=lambda o, k: o.setdefault(k, dict()))\ndeep_set(o, "1.1.2", \'Hello World\')\ndeep_set(o, "1.1.3", \'c\')\nprint("{}: {}".format(i, deep_del(o, "1.1.2")[1]))\nprint(o)\n```\n',
    'author': 'mbello',
    'author_email': 'mbello@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mbello/dict-deep',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
