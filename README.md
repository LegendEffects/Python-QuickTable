# Python-QuickTable
A Python API which creates tables quickly and easily

Example Output:
```
 ID | Name  | Email           |
 1  | Test  | Test@test.com   |
 2  | Test2 | Test@test.net   |
 3  | Test3 | Test@test.org   |
 4  | Test4 | Test@tester.com |
```

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
