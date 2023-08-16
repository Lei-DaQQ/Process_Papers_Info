# Readme
提取每一个<hit>里author、title、venue、year、ee，如果有多个作者，放在excel里放在一个单元格中.

# Usage

```shell
pip install -r requires.txt
```

23/July/2023

## xml to excel
```python
python xml2excel.py
```
recommend you create a directory `papers` in which you store the `.xml` files.

## merge duplicate bibtex refs
```
python merge_dupli_bib.py
```

recommend you create a directory `bibs` in which you store the `.bib` files.
and the program will create directory `merged001` `merged002` etc, to store the merged bib refs.

# Record
## 13/Aug/2023
add config.json, in which you should fill the output excel file't columns name.
if there are some columns you have, but the dblp don't offer, you should fill them with no.
for example:
```json
{
  "columns": [
      {"name": "title", "title": "Title"},
      {"name": "no", "title": "ID"},
      {"name": "venue", "title": "Conference"},
      {"name": "no", "title": "CCF-Level"},
      {"name": "year", "title": "Year"},
      {"name": "no", "title": "Relevance"},
      {"name": "no", "title": "devices"},
      {"name": "ee", "title": "ref"},
      {"name": "no", "title": "Abstraction"},
      {"name": "no", "title": "KeyWords"},
      {"name": "no", "title": "Type"},
      {"name": "no", "title": "whichUse"},
      {"name": "no", "title": "Stauts"},
      {"name": "authors", "title": "Author"},
      {"name": "no", "title": "Organization"},
      {"name": "no", "title": "E-mail"}
  ]
}
																
```

