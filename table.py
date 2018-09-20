class Table:
    headers = [] # Stores header data
    totalheaders = 0 # Amount of headers

    rows = [] # Rows in the table
    totalrows = 0 # Amount of rows

    datalengths = [] # Stores the longest length of data in that column

    def initialize(self, headers):
        self.headers = headers
        self.totalheaders = len(headers)

        # Initialize the datalengths array
        for i in range(len(headers)):
            self.datalengths.insert(i, len(headers[i]))

        return True

    def addrow(self, row):
        # Check for incorrect amount of data slots for the amount of headers
        if len(row) != self.totalheaders:
            return False

        self.rows.append(row)
        self.totalrows += 1

        # Compare the data lengths to see if its longer
        for i in range(len(row)):
            if len(row[i]) > self.datalengths[i]:
                self.datalengths[i] = len(row[i])

    def render(self, rows):
        if rows < -1 or rows > self.totalrows:
            return False

        if rows == -1:  # Render all rows
            rows = self.totalrows

        print(self.__renderheaders())

        for i in range(rows):
            row = self.rows[i] # Current Row

            compiler = ""

            for c in range(len(row)):
                compiler += " " + self.__renderspaces(row[c], self.datalengths[c]) + " |"

            print(compiler)

    def __renderheaders(self):
        headercompiler = ""

        for i in range(self.totalheaders):
            header = self.headers[i]
            collength = self.datalengths[i]

            headercompiler += " " + self.__renderspaces(header, collength) + " |"

        return headercompiler

    def __renderspaces(self, data, collength):
        spacesneeded = collength - len(data)
        compiler = data

        if spacesneeded < 0:
            spacesneeded = 0

        for _ in range(spacesneeded):
            compiler += " "

        return compiler
