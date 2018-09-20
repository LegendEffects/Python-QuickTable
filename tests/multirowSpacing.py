from table import Table

t = Table()

t.initialize(['ID', 'Name', 'Email'])
t.addrow(['1', 'Test', 'Test@test.com'])
t.addrow(['2', 'Test2', 'Test@test.net'])
t.addrow(['3', 'Test3', 'Test@test.org'])
t.addrow(['4', 'Test4', 'Test@tester.com'])

t.render(-1)
