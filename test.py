__author__ = 'student'

dic = {1: [10, 11, 12], 2: [10, 11, 13]}

print dic

for value in dic.itervalues():
    print value

    for cell in value:
        print cell


import sys

class CrossTab(object):

    def __init__(
        self,
        missing=0, # what to return for an empty cell. Alternatives: '', 0.0, None, 'NULL'
        ):
        self.missing = missing
        self.col_key_set = set()
        self.cell_dict = {}
        self.headings_OK = False

    def add_item(self, row_key, col_key, value):
        self.col_key_set.add(col_key)
        try:
            self.cell_dict[row_key][col_key] += value
        except KeyError:
            try:
                self.cell_dict[row_key][col_key] = value
            except KeyError:
                self.cell_dict[row_key] = {col_key: value}

    def _process_headings(self):
        if self.headings_OK:
            return
        self.row_headings = list(sorted(self.cell_dict.iterkeys()))
        self.col_headings = list(sorted(self.col_key_set))
        self.headings_OK = True

    def get_col_headings(self):
        self._process_headings()
        return self.col_headings

test = CrossTab(dic)
print test