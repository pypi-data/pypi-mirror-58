# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marshmallow_toplevel']

package_data = \
{'': ['*']}

install_requires = \
['marshmallow>=3.0.0,<4.0.0', 'pytest>=5.3.2,<6.0.0']

setup_kwargs = {
    'name': 'marshmallow-toplevel',
    'version': '0.1.1',
    'description': 'Validate top-level lists with all the power of marshmallow',
    'long_description': '# marshmallow-toplevel\nLoad and validate top-level lists with all the power of\n[marshmallow](https://github.com/marshmallow-code/marshmallow).\n\n## Installation\n\n```sh\npip install marshmallow-toplevel\n```\n\n## Usage\n\n```python\nfrom marshmallow import fields\nfrom marshmallow_toplevel import TopLevelSchema\n\n\nclass BatchOfSomething(TopLevelSchema):\n    _toplevel = fields.Nested(\n        SomethingSchema,\n        required=True,\n        many=True,\n        validate=any_validation_logic_applied_to_list\n    )\n```\n\n## Rationale\n\nImagine that you have an API endpoint (or any other program that\naccepts user input), which is intended to accept multiple blog articles\nand save them to a database. Semantically, your data is a list of dictionaries:\n\n```python\n[\n    {"id": 1, "title": "Hello World!"},\n    {"id": 2, "title": "Yet another awesome article."},\n    ...\n]\n```\n\nYou describe article object schema and put constraints on your data:\n\n```python\nfrom marshmallow import Schema, fields, validate\n\n\nclass ArticleSchema(Schema):\n    id = fields.Int(required=True)\n    title = fields.Str(required=True, validate=validate.Length(min=2, max=256))\n```\n\nBut you also want to put some constraints onto outer list itself, for example,\nyou want it to have length between 1 and 10. How do you describe it in\nterms of `marshmallow`?\n\n### Obvious solution: nest your data\n\n```python\nclass BatchOfArticles(Schema):\n    articles = fields.Nested(\n        ArticleSchema,\n        required=True,\n        many=True,\n        validate=validate.Length(1, 10)\n    )\n```\n\nBut now a client have to send data this way, with this extra dictionary around:\n\n```python\n{\n    "articles": [\n        {"id": 1, "title": "Hello World!"},\n        {"id": 2, "title": "Yet another awesome article."},\n        ...\n    ]\n}\n```\n\nIt makes your API not so beautiful and user-friendly.\n\n### Good solution: use marshmallow-toplevel\n\nWith `marshmallow-toplevel` you can describe you data this way:\n\n```python\nfrom marshmallow_toplevel import TopLevelSchema\n\n\nclass BatchOfArticles(TopLevelSchema):\n    _toplevel = fields.Nested(\n        ArticleSchema,\n        required=True,\n        many=True,\n        validate=validate.Length(1, 10)\n    )\n```\n\nNotice that schema inherits from `TopLevelSchema` and uses this\nspecial `_toplevel` key. It means that the field under this key\ndescribes top level object. You can define any constrains that\nyou can define in `marshmallow` and it will just work:\n\n```python\nschema = BatchOfArticles()\n\n# validation should fail\nerrors = schema.validate([])\nassert errors  # length < 1\nerrors = schema.validate([{"id": i, "title": "title"} for i in range(100)])\nassert errors  # length > 10\n\n# validation should succeed\nerrors = schema.validate([{"id": i, "title": "title"} for i in range(5)])\nassert not errors\n```\n\nYou can also use `load` for this schema as usual:\n\n```python\ndata = schema.load([{"id": "10", "title": "wow!"}])\nprint(data)\n# [{"id": 10, "title": "wow!"}]\n```\n\nNow a client can send data as a list without redundancy.\n',
    'author': 'Andrey Semakin',
    'author_email': 'and-semakin@ya.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/and-semakin/marshmallow_toplevel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
