# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['autocensus']

package_data = \
{'': ['*'], 'autocensus': ['resources/*']}

install_requires = \
['Fiona>=1.8,<2.0',
 'aiohttp>=3.5,<4.0',
 'appdirs>=1.4,<2.0',
 'geopandas>=0.5.1,<0.6.0',
 'nest-asyncio>=1.2,<2.0',
 'pandas>=0.24.1,<0.25.0',
 'shapely>=1.6,<2.0',
 'socrata-py>=0.4.20,<0.5.0',
 'tenacity>=5.1,<6.0',
 'titlecase>=0.12.0,<0.13.0',
 'yarl>=1.3,<2.0']

setup_kwargs = {
    'name': 'autocensus',
    'version': '1.0.6',
    'description': 'A tool for collecting ACS and geospatial data from the Census API',
    'long_description': "# autocensus\n\nPython package for collecting American Community Survey (ACS) data from the [Census API], along with associated geospatial points and boundaries, in a pandas dataframe. Uses asyncio/aiohttp to request data concurrently.\n\nThis package is under active development and breaking changes to its API are expected.\n\n[Census API]: https://www.census.gov/developers\n\n## Contents\n\n* [Installation](#installation)\n* [Example](#example)\n* [Joining geospatial data](#joining-geospatial-data)\n  + [Caching](#caching)\n* [Publishing to Socrata](#publishing-to-socrata)\n  + [Credentials](#credentials)\n  + [Example: Create a new dataset](#example-create-a-new-dataset)\n  + [Example: Replace rows in an existing dataset](#example-replace-rows-in-an-existing-dataset)\n  + [Example: Create a new dataset from multiple queries](#example-create-a-new-dataset-from-multiple-queries)\n* [Troubleshooting](#troubleshooting)\n  + [Clearing the cache](#clearing-the-cache)\n  + [SSL errors](#ssl-errors)\n\n## Installation\n\nautocensus requires Python 3.7 or higher. Install as follows:\n\n```sh\npip install autocensus\n```\n\nTo run autocensus, you must specify a [Census API key] via either the `census_api_key` keyword argument (as shown in the example below) or by setting the environment variable `CENSUS_API_KEY`.\n\n## Example\n\n```python\nfrom autocensus import Query\n\n# Configure query\nquery = Query(\n    estimate=5,\n    years=[2014, 2015, 2016, 2017],\n    variables=['B01002_001E', 'B03001_001E', 'DP03_0025E', 'S0503_C02_077E'],\n    for_geo='tract:*',\n    in_geo=['state:08', 'county:005'],\n    # Fill in the following with your actual Census API key\n    census_api_key='Your Census API key'\n)\n\n# Run query and collect output in dataframe\ndataframe = query.run()\n```\n\nOutput:\n\n| name                                          | geo_id               | geo_type | year | date       | variable_code | variable_label     | variable_concept  | annotation | value | percent_change | difference | centroid  | internal_point | geometry         |\n|-----------------------------------------------|----------------------|----------|------|------------|---------------|--------------------|-------------------|------------|-------|----------------|------------|-----------|----------------|------------------|\n| Census Tract 151, Arapahoe County, Colorado   | 1400000US08005015100 | tract    | 2014 | 2014-12-31 | B01002_001E   | Median age - Total | Median Age by Sex |            | 45.7  |                |            | POINT (…) | POINT (…)      | MULTIPOLYGON (…) |\n| Census Tract 151, Arapahoe County, Colorado   | 1400000US08005015100 | tract    | 2015 | 2015-12-31 | B01002_001E   | Median age - Total | Median Age by Sex |            | 45.2  | -1.1           | -0.5       | POINT (…) | POINT (…)      | MULTIPOLYGON (…) |\n| Census Tract 151, Arapahoe County, Colorado   | 1400000US08005015100 | tract    | 2016 | 2016-12-31 | B01002_001E   | Median age - Total | Median Age by Sex |            | 45.9  | 1.6            | 0.7        | POINT (…) | POINT (…)      | MULTIPOLYGON (…) |\n| Census Tract 151, Arapahoe County, Colorado   | 1400000US08005015100 | tract    | 2017 | 2017-12-31 | B01002_001E   | Median age - Total | Median Age by Sex |            | 45.7  | -0.4           | -0.2       | POINT (…) | POINT (…)      | MULTIPOLYGON (…) |\n| Census Tract 49.51, Arapahoe County, Colorado | 1400000US08005004951 | tract    | 2014 | 2018-12-31 | B01002_001E   | Median age - Total | Median Age by Sex |            | 26.4  |                |            | POINT (…) | POINT (…)      | MULTIPOLYGON (…) |\n\n[Census API key]: https://api.census.gov/data/key_signup.html\n\n## Joining geospatial data\n\nautocensus will automatically join geospatial data (centroids, representative points, and geometry) for the following geography types for years 2013 and on:\n\n* Nation-level\n  + `nation`\n  + `region`\n  + `division`\n  + `state`\n  + `urban area`\n  + `zip code tabulation area`\n  + `county`\n  + `congressional district`\n  + `metropolitan statistical area/micropolitan statistical area`\n  + `combined statistical area`\n  + `american indian area/alaska native area/hawaiian home land`\n  + `new england city and town area`\n* State-level\n  + `alaska native regional corporation`\n  + `block group`\n  + `county subdivision`\n  + `tract`\n  + `place`\n  + `public use microdata area`\n  + `state legislative district (upper chamber)`\n  + `state legislative district (lower chamber)`\n\nFor queries spanning earlier years, these geometry fields will be populated with null values. (Census boundary shapefiles are not available for years prior to 2013.)\n\nIf you don't need geospatial data, set the keyword arg `join_geography` to `False` when initializing your query:\n\n```python\nquery = Query(\n    estimate=5,\n    years=[2014, 2015, 2016, 2017],\n    variables=['B01002_001E', 'B03001_001E', 'DP03_0025E', 'S0503_C02_077E'],\n    for_geo='tract:*',\n    in_geo=['state:08', 'county:005'],\n    join_geography=False\n)\n```\n\nIf `join_geography` is `False`, the `centroid`, `internal_point`, and `geometry` columns will not be included in your results.\n\n### Caching\n\nTo improve performance across queries, autocensus caches shapefiles on disk by default. The cache location varies by platform:\n\n* Linux: `/home/{username}/.cache/autocensus`\n* Mac: `/Users/{username}/Library/Application Support/Caches/autocensus`\n* Windows: `C:\\\\Users\\\\{username}\\\\AppData\\\\Local\\\\socrata\\\\autocensus`\n\nYou can clear the cache by manually deleting the cache directory or by executing the `autocensus.clear_cache` function. See the section [Troubleshooting: Clearing the cache] for more details.\n\n[Troubleshooting: Clearing the cache]: #clearing-the-cache\n\n## Publishing to Socrata\n\nIf [socrata-py] is installed, you can publish query results (or dataframes containing the results of multiple queries) directly to Socrata via the method `Query.to_socrata`.\n\n[socrata-py]: https://github.com/socrata/socrata-py\n\n### Credentials\n\nYou must have a Socrata account with appropriate permissions on the domain to which you are publishing. By default, autocensus will look up your Socrata account credentials under the following pairs of common environment variables:\n\n* `SOCRATA_KEY_ID`, `SOCRATA_KEY_SECRET`\n* `SOCRATA_USERNAME`, `SOCRATA_PASSWORD`\n* `MY_SOCRATA_USERNAME`, `MY_SOCRATA_PASSWORD`\n* `SODA_USERNAME`, `SODA_PASSWORD`\n\nAlternatively, you can supply credentials explicitly by way of the `auth` keyword argument:\n\n```python\nauth = (os.environ['MY_SOCRATA_KEY'], os.environ['MY_SOCRATA_KEY_SECRET'])\nquery.to_socrata(\n    'some-domain.data.socrata.com',\n    auth=auth\n)\n```\n\n### Example: Create a new dataset\n\n```python\n# Run query and publish results as a new dataset on Socrata domain\nquery.to_socrata(\n    'some-domain.data.socrata.com',\n    name='Average Commute Time by Colorado County, 2013–2017',  # Optional\n    description='5-year estimates from the American Community Survey'  # Optional\n)\n```\n\n### Example: Replace rows in an existing dataset\n\n```python\n# Run query and publish results to an existing dataset on Socrata domain\nquery.to_socrata(\n    'some-domain.data.socrata.com',\n    dataset_id='xxxx-xxxx'\n)\n```\n\n### Example: Create a new dataset from multiple queries\n\n```python\nfrom autocensus import Query\nfrom autocensus.socrata import to_socrata\nimport pandas as pd\n\n# County-level query\ncounty_query = Query(\n    estimate=5,\n    years=range(2013, 2018),\n    variables=['DP03_0025E'],\n    for_geo='county:*',\n    in_geo='state:08'\n)\ncounty_dataframe = county_query.run()\n\n# State-level query\nstate_query = Query(\n    estimate=5,\n    years=range(2013, 2018),\n    variables=['DP03_0025E'],\n    for_geo='state:08'\n)\nstate_dataframe = state_query.run()\n\n# Concatenate dataframes and upload to Socrata\ncombined_dataframe = pd.concat([\n    county_dataframe,\n    state_dataframe\n])\nto_socrata(\n    'some-domain.data.socrata.com',\n    dataframe=combined_dataframe,\n    name='Average Commute Time by Colorado County with Statewide Averages, 2013–2017',  # Optional\n    description='5-year estimates from the American Community Survey'  # Optional\n)\n```\n\n## Troubleshooting\n\n### Clearing the cache\n\nSometimes it is useful to clear the [cache directory] that autocensus uses to store downloaded shapefiles for future queries, especially if you're running into `BadZipFile: File is not a zip file` errors or other shapefile-related problems. Clear your cache like so:\n\n```python\nimport autocensus\n\nautocensus.clear_cache()\n```\n\n[cache directory]: #caching\n\n### SSL errors\n\nTo disable SSL verification, specify `verify_ssl=False` when initializing your `Query`:\n\n```python\nquery = Query(\n    estimate=5,\n    years=[2014, 2015, 2016, 2017],\n    variables=['B01002_001E', 'B03001_001E', 'DP03_0025E', 'S0503_C02_077E'],\n    for_geo='tract:*',\n    in_geo=['state:08', 'county:005'],\n    verify_ssl=False\n)\n```\n",
    'author': 'Christopher Setzer',
    'author_email': 'chris.setzer@socrata.com',
    'url': 'https://github.com/socrata/autocensus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
