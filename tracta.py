__copyright__ = "Copyright (C) 2019 Roc Erro"
__license__ = "All Rights Reserved"

import re

def split_html(tag, html):
    """Serch on the html code what's on a certain tag and returns it on a list.
    Example:
    html = 
    "
    <td>2
    <td>1</td>
    "
    split_html(td, html)
    Returns:
    [2,1]
    """
    pieces = re.split("(?i)<"+tag+"[^<]*>", html)
    pieces.pop(0)
    ret = []
    for piece in pieces:
        piece = re.split("(?i)</"+tag+">", piece)
        ret.append(piece[0])
    return ret
    
def get_tables(html):
    """Use split_html function to return a list of the tables from the code"""
    return split_html("table", html)
        
def get_rows(table):
    """Use split_html function to return a list of the rows from a table"""
    return split_html("tr", table)

def get_datas(row):
    """Use split_html function to return a list of the datas from a row (including header datas)"""
    return split_html("t[dh]", row)

def get_dict(html):
    """Get the headers and datas of an specific table and returns a dictionari of them"""
    tables = get_tables(html)
    rows = get_rows(tables[0])
    datas1 = get_datas(rows[0])
    datas2 = get_datas(rows[2])
    return dict( zip(datas1, datas2) )
    
