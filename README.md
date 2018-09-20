# Python-QuickTable
A Python API which creates tables quickly and easily

# Usage
Importing:
`from table import Table`

Making a new table:
```
t = Table()
t.initialize(['header1', 'header2', 'header3'])
```

Add a row:
`t.addrow(['data1', 'data2', 'data3'])` Length of array must match the amount of headers in the table.

Render the table:
`t.render(-1)`

Use -1 to render all rows or use a number to limit it.
