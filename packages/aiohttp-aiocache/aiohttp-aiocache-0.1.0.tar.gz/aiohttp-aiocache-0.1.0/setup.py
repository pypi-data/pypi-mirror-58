# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohttp_aiocache']

package_data = \
{'': ['*']}

install_requires = \
['aiocache>=0.11.1,<0.12.0']

setup_kwargs = {
    'name': 'aiohttp-aiocache',
    'version': '0.1.0',
    'description': 'Caching middleware for aiohttp server with aiocache under the hood',
    'long_description': '# aiohttp-aiocache\n\n[![Maintainability](https://api.codeclimate.com/v1/badges/4b6f49c9d1e4e1e9963d/maintainability)](https://codeclimate.com/github/nobbynobbs/aiohttp-aiocache/maintainability)\n[![Test Coverage](https://api.codeclimate.com/v1/badges/4b6f49c9d1e4e1e9963d/test_coverage)](https://codeclimate.com/github/nobbynobbs/aiohttp-aiocache/test_coverage)\n\nCaching middleware for [aiohttp](https://github.com/aio-libs/aiohttp) server\nwith [aiocache](https://github.com/argaen/aiocache) under the hood.\nInspired by [aiohttp-cache](https://github.com/cr0hn/aiohttp-cache).\n\n## Installation\n\n```bash\npip install aiohttp-aiocache\n```\n\nor \n\n```bash\npoetry add aiohttp-aiocache\n```\n\nOptional `aiocache` dependencies for redis, memcached and msgpack support\nwill not be installed. Install them manually if required.\n\n## Usage\n```python\nimport asyncio\n\nimport aiohttp.web as web\nfrom aiocache import Cache\nfrom aiocache.serializers import PickleSerializer\n\nfrom aiohttp_aiocache import cached, register_cache\n\n\n@cached  # mark handler with decorator\nasync def handler(_: web.Request) -> web.Response:\n    await asyncio.sleep(1)\n    return web.Response(text="Hello world")\n\napp = web.Application()\napp.router.add_route("GET", "/", handler)\n\n# create aiocache instance\ncache = Cache(\n    Cache.MEMORY,\n    serializer=PickleSerializer(),\n    namespace="main",\n    ttl=60,\n)\n\n# register cache backend in appplication\nregister_cache(app, cache)\n\nweb.run_app(app)\n```\n\n## Limitations\n\nSupport caching for GET requests only.\n\n## License\n\nMIT',
    'author': 'Roman Bolkhovitin',
    'author_email': 'rbolkhovitin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nobbynobbs/aiohttp-aiocache',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
