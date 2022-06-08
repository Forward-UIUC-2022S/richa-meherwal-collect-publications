# richa-meherwal-collect-publications
Code to collect publications matching a keyword, author or affiliation. Collects data by sending requests to publication databases APIs.

[Click here for list of sources surveyed](https://docs.google.com/spreadsheets/d/18v4DyHw-1LIWCnyu05NFzqGjirpl0nutvFSXWB4xwzw/edit#gid=1627084748)

Usage

```
python main.py --term <query_term> --author <author_name> --sources [comma seperated list of sources] --affiliation <affiliation_name> --filename <filename.json>
```

Example


```
python main.py --sources europemc,hal --term medical --filename medical.json
```
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
