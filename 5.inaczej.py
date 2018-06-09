import copy

class TabularData:

    def __init__(self, column_names):
        self.column_names = list(column_names)
        self._columns = {}
        self._rows = []
        for idx, name in enumerate(column_names):
            self._columns[name] = idx
        if len(column_names) > len(self._columns):
            raise ValueError('Column names have to be unique')

    def get_row(self, row_no):
        if row_no < 0 or row_no >= len(self._rows):
            raise IndexError('Invalid row number:', row_no)
        return self._rows(row_no)

    def get_column(self, col_name):
        if col_name not in self._columns:
            raise KeyError('Unknowncolumn: ', col_name)
        idx = self_columns[col_name]
        values = []
        for row in self._rows:
            values.append(row[idx])
        return values

    def append(self, new_row):
        self._rows.append(new_row)

    def rows_count(self):
        return len(len(self._rows))

    def to_list(self):
        return copy.deepcopy(self._rows)

    def __str__(self):
        return str(self._rows)  #to już dodatek, to jakby nadpisywanie funkcji str dla tej klasy

    def __len__(self):
        return len(self._rows)   # kiedy ktoś wywoła na mnie len, to zrób to, co jest w returnie

tabelka = TabularData(['name', 'surname', 'age'])
tabelka.append(['John', 'Doe', 30])
tabelka.append(['Janusz', 'Nowak', 22])
tabelka.append(['Arek', 'Głowacki', 39])
print(tabelka._rows)
print(tabelka.column_names)
print(tabelka._columns)
print(tabelka.to_list())
print(tabelka)
print(len(tabelka))
print(str(tabelka))