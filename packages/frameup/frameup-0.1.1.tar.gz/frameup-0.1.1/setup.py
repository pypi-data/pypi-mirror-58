# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['frameup']

package_data = \
{'': ['*'], 'frameup': ['templates/*']}

install_requires = \
['pandas>=0.23.0,<0.24.0']

entry_points = \
{'console_scripts': ['frameup = frameup.serve:main']}

setup_kwargs = {
    'name': 'frameup',
    'version': '0.1.1',
    'description': 'DataFrames all up in your web applications',
    'long_description': "# DataFrameup\n\nFrameup is the easiest way to get your Pandas DataFrame up into a Python-based web application. Simply `import frameup` and your DataFrames will become URL query parameter, and pagination aware.\n\nZero dependencies, except Pandas of course.\n\n## Quick look\n\nServe a csv as a frameup dataframe on localhost\n\n```\n $ python -m frameup.serve <path-to-csv-file>\n```\n\nThen navigate to http://localhost:8000/. Use the [Pandas DataFrame query syntax](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) in the query box.\n\n... or, get a JSON payload:\n\n```\n $ curl 'http://localhost:8000/?query=&limit=10&page=1' | python -m json.tool\n```\n\n\n## Use it in your web application\n\n### Flask example\n\nGiven a template similar to example.js.html\n\n```\nfrom flask import Flask, jsonify, render_template, request, url_for\nimport pandas as pd\nimport frameup\n\napp = Flask(__name__)\n\ndf = pd.read_csv(YOUR_CSV_FILE)\n\n@app.route('/mydataframe')\ndef main():\n    data = df.frameup.data(path=url_for('mydataframe'), **request.args)\n    return render_template('example.j2.html', **data)\n```\n\nFor something ajaxy, just replace the return with:\n\n```\nreturn jsonify(**data)\n```\n\n## Other projects\n\nProjects to review / learn from / use instead\n\n * [Datasette](https://github.com/simonw/datasette)\n * [Workbench](https://workbenchdata.com/)\n",
    'author': 'Scott Bradley',
    'author_email': 'scott@codeslick.com',
    'url': 'https://github.com/scott2b/DataFrameup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
