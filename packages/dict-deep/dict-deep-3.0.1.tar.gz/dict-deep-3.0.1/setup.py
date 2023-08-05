# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dict_deep']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dict-deep',
    'version': '3.0.1',
    'description': "Very simple deep_set and deep_get functions to access nested dicts (or any object) using 'dotted strings' as key.",
    'long_description': '## Description\n\nSimple functions to set or get values from a nested dict structure or in fact a deep structure of any object, because\nsince version 2 we no longer assume we are dealing with dicts.\n\nAlthough we make your life easier if working with dicts (see the default argument that was left for this purpose),\nwe now let you use custom getter, setter, deleter callables so that you can traverse a nested structure of any kind of \nobject.\n\nThis module DOES NOT implement dotted notation as an alternative access method for dicts.\nI generally do not like changing python dicts to enable dot notation, hence no available\npackage fitted my needs for a simple deep accessor.\n\n\n## Functions\n\n*deep_get* accepts:\n- d: required. Any object, usually a dictionary.\n- key: required. A string or anything accepted by the list() constructor.\n- default: optional, callable: a callable to be used as default for the dict .setdefault function. If d is not a dict, use a custom getter instead.\n- getter: optional, callable. If getter is set, default is ignored. Must be a callable that accepts an object and a key as arguments. (ex. lambda o, k: o[k])\n- sep: optional, string: by default it is a dot \'.\', you can use anything the string function split will accept\n\nReturns the value corresponding to \'key\' on \'d\'\n\n\n*deep_set* accepts:\n- d: same as above\n- key: same as above\n- value: required, self explanatory\n- default: optional, callable: If set, will use setdefault to traverse the nested dict structure. See comments from deep_get.\n- getter: same as above.\n- setter: optional, callable. A callable that takes 3 parameters: o, k, v - where o = any object, k = key, v = value  \n- sep: same as above\n\nNo return value\n\n\n*deep_del* accepts:\n- d: same as above\n- key: same as above\n- sep: same as above\n- getter: same as above. However, make your getter return None if you want to avoid exceptions being raised.\n- deleter: optional callable: A callable that takes 2 parameters: o, k (object and key). By default we call \'del o[k]\'\n\nReturns a tuple:\n(True, <value of the entry that was deleted>) or\n(False, None)\n\n\n## Usage\n\n    from dict_deep import deep_get, deep_set, deep_del\n    \n    \n    i = 1\n    \n    \n    # Alternative 1\n    d = {\'a\': {\'b\': {}}}\n    deep_set(d, "a.b.c", "Hello World")\n    print("{}: {}".format(i, deep_get(d, "a.b.c")))\n    i += 1\n\n\n    # Alternative 2\n    d = {}\n    deep_set(d, [\'a\', \'b\', \'c\'], "Hello World", default=lambda: dict())\n    print("{}: {}".format(i, deep_get(d, "a.b.c")))    \n    i += 1\n    \n    \n    # Alternative 3\n    d = {}\n    deep_set(d, "a->b->c", "Hello World", default=lambda: dict(), sep="->")\n    print("{}: {}".format(i, deep_get(d, "a->b->c", sep="->")))\n    i += 1\n    \n    \n    # Alternative 4\n    d = {}\n    deep_set(d, "a->b->c", "Hello World", getter=lambda o, k: o.setdefault(k, dict()), sep="->")\n    print("{}: {}".format(i, deep_get(d, "a->b->c", sep="->")))\n    i += 1\n    \n    \n    # Alternative 5\n    d = {}\n    keys = \'a.b.c\'\n    keys = keys.split()\n    _ = deep_get(d=d, key=keys[0:-1], default=lambda: dict(), sep=".")\n    _[keys[-1]] = "Hello World"\n    print("{}: {}".format(i, deep_get(d, keys)))\n    i += 1\n    \n    \n    # deep_del\n    d = {}\n    deep_set(d, "1.1.1", \'a\', default=lambda: dict())\n    deep_set(d, "1.1.2", \'Hello World\')\n    deep_set(d, "1.1.3", \'c\')\n    print("{}: {}".format(i, deep_del(d, "1.1.2")[1]))\n    print(d)',
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
