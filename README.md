# richa-meherwal-collect-publications
This module is responsible for collecting academic publications matching a keyword, author or affiliation. It does so by collecting data from publication databases APIs.

## Setup 
- Use python version 3.8.3 and pip version 21.0.1
- Download this repo
- Install requirements.txt

```
pip install -r requirements.txt
```

- Run commands such as :
```
python main.py --term <query_term> --author <author_name> --sources [comma seperated list of sources] --affiliation <affiliation_name> --filename <filename.json>
```

Example

```
python main.py --sources europemc,hal --term medical --filename medical.json
```

## Overall Code Breakdown

```
- richa-meherwal-collect-publications/
  - utils.py 
  - source.py
  - main.py 
  - survey/
    - README.md
  - examples/
    - author.json
```

- utils.py : Contains utils functions to extract attributes from JSON or XML data for the given source
- sources.py : Contains Source class and methods that call source APIs
- main.py : Contains main function that parses arguments and calls the Source class from sources.py

## Functional Design 

If you want to use this module by integrating it in your code. Use Source class from sources.py. An example to use this class is available in main.py. Source class gives access to methods that call indvidual source APIs. For instance, if you want to call CrossRef Works API to collect publications data, you can import Source class as:
```
from source import Source
```
initialize object from class

```
source = Source(q, author, inst)
```
And then call crossref method with arguments keyword, author_name, affiliation_name

```
source.crossref_works()
```
This should return a list of publications based on the arguments given


## Surveyed APIs 

[Click here for list of sources surveyed](https://docs.google.com/spreadsheets/d/18v4DyHw-1LIWCnyu05NFzqGjirpl0nutvFSXWB4xwzw/edit#gid=1627084748)

Sources available

- europemc
- scopus
- semanticscholar
- ieee
- arxiv
- hal
- openalex
- crossref_works
- google_scholar
- doaj

## Issues and Future work 

For future work, the module can be expanded to include more APIs. There could also be functions that can filter the data retrieved from APIs by date, venue. Tests can be added to check individual modules
