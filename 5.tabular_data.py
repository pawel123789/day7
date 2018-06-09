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
        return self._rows(row_no)

    def get_column(self, col_name):
        return self._columns[self.column_names[0:3]]

    def append(self, new_row):
        self._rows.append(new_row)

    def rows_count(self):
        for idx, values in row_no:




tabelka = TabularData(['name', 'surname', 'age'])
tabelka.append(['John', 'Doe', 30])
tabelka.append(['Janusz', 'Nowak', 22])
tabelka.append(['Arek', 'Głowacki', 39])
print(tabelka._rows)
print(tabelka.column_names)
print(tabelka._columns)

