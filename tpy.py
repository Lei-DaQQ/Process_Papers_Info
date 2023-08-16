import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
# 创建一个包含条目的列表
entries = [
    {
        'ENTRYTYPE': 'article',
        'ID': 'article1',
        'author': 'Author A',
        'title': 'Title of the Article',
        'journal': 'Journal Name',
        'year': '2023',
    },
    {
        'ENTRYTYPE': 'book',
        'ID': 'book1',
        'author': 'Author B',
        'title': 'Title of the Book',
        'publisher': 'Publisher Name',
        'year': '2022',
    },
]

db = BibDatabase() 
db.entries = entries
# 使用 bibtexparser.dumps 将条目列表转换为 BibTeX 字符串
bibtex_str = bibtexparser.dumps(db)

# 打印生成的 BibTeX 字符串
print(bibtex_str)
