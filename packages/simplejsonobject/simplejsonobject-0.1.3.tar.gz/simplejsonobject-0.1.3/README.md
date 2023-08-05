# simplejsonobject
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version](https://img.shields.io/pypi/v/simplejsonobject)](https://pypi.org/project/simplejsonobject/)
[![PyPI - Downloads](https://pepy.tech/badge/simplejsonobject)](https://pepy.tech/project/simplejsonobject)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/simplejsonobject)](https://pypi.org/project/simplejsonobject/)
[![pipeline status](https://gitlab.com/mozgurbayhan/simplejsonobject/badges/master/pipeline.svg)](https://gitlab.com/mozgurbayhan/simplejsonobject/commits/master)
[![pylint status](https://gitlab.com/mozgurbayhan/simplejsonobject/-/jobs/artifacts/master/raw/pylint/pylint.svg?job=pylint)](https://gitlab.com/mozgurbayhan/simplejsonobject/commits/master)
[![coverage report](https://gitlab.com/mozgurbayhan/simplejsonobject/badges/master/coverage.svg)](https://gitlab.com/mozgurbayhan/simplejsonobject/commits/master)

A simple python object which can easily transform to and from json with compression support

## Install

```bash
pip install simplejsonobject
```

## Usage 

```python
from simplejsonobject import JsonObject


class Sample(JsonObject):
    def __init__(self):
        self.a = "8"
        self.b = 3
        self.c = None

        
def main():
	smp=Sample()
	smp.to_dict() # {"a": tdata, "b": 3, "c": None}
	smp.to_dict_compressed() # {"a": tdata, "b": 3}
	smp.to_json() # '{\n    "a": 8,\n    "b": 3,\n    "c": null\n}'
	smp.to_json_compressed() # '{"a": 8, "b": 3}'
	
	# or you can import from any compressed/notcompressed json/dict
	# all below results same object
	tsmp.from_dict({"a": tdata, "b": 3, "c": None}
	tsmp.from_dict({"a": tdata, "b": 3})
	tsmp.from_json('{\n    "a": "8",\n    "b": 3,\n    "c": null\n}')
	tsmp.from_json('{"a": "8", "b": 3}')


if __name__ == '__main__':
    main()

```