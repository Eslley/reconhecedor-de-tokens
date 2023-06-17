import re


class SQLParser:
    current_token = 0
    current_token_line = 1
    token = ''
    reserved_words = ['create', 'table', 'database', ' use', 'insert', 'into', 'values', 'select', 'from', 'order', 'by',
                      'where', 'truncate', 'update', 'set', 'delete']

    def __init__(self, tokens):
        self.tokens = tokens

    def next_token(self):
        self.current_token += 1
        if self.current_token > len(self.tokens):
            self.print_error_fim()
        self.token = self.tokens[self.current_token-1]['token']
        self.current_token_line = self.tokens[self.current_token-1]['line']

    def ini(self):
        while self.current_token < len(self.tokens):
            self.next_token()
            self.cmd()
            if self.token == ";":
                continue
            else:
                self.print_error(";")

    def cmd(self):
        self.create()
        self.use()
        self.insert()
        #select()
        #delete()
        #truncate()

    def create(self):
        if "create" == self.token:
            self.next_token()
            self.cmd1()

    def insert(self):
        if "insert" == self.token:
            self.next_token()
            if "into" == self.token:
                self.next_token()
                self.id()
                if self.token == '(':
                    self.next_token()
                    self.ids()
                    if self.token == ")":
                        self.next_token()
                    else:
                        self.print_error(")")
                else:
                    self.print_error("(")
                if self.token == "values":
                    self.next_token()
                    if self.token == '(':
                        self.next_token()
                        self.values()
                        if self.token == ")":
                            self.next_token()
                        else:
                            self.print_error(")")
                    else:
                        self.print_error("(")
                else:
                    self.print_error("values")
            else:
                self.print_error("into")

    def cmd1(self):
        if self.token == "database":
            self.next_token()
            self.id()
        elif self.token == "table":
            self.next_token()
            self.id()
            if self.token == "(":
                self.next_token()
                self.fields()
                if self.token == ")":
                    self.next_token()
                    return
                else:
                    self.print_error(')')
            else:
                self.print_error('(')

    def ids(self):
        self.id()
        if self.token == ',':
            self.next_token()
            self.id()

    def values(self):
        self.value()
        if self.token == ',':
            self.next_token()
            self.values()

    def id(self):
        if re.match(r'[a-z]+', self.token):
            if self.token not in self.reserved_words:
                self.next_token()
            else:
                self.print_error("<id>")
        else:
            self.print_error("<id>")

    def value(self):
        if re.match(r'[a-z]+|[0-9]+', self.token):
            if self.token not in self.reserved_words:
                self.next_token()
            else:
                self.print_error("<value>")
        else:
            self.print_error("<value>")

    def fields(self):
        self.field()
        if self.token == ',':
            self.next_token()
            self.fields()

    def field(self):
        self.id()
        self.id()

    def use(self):
        if self.token == 'use':
            self.next_token()
            self.id()

    def print_error_fim(self):
         raise ValueError({
            'errorType': 'end_input_not_expected',
            'line': self.current_token_line,
            'received': self.token
        })

    def print_error(self, esperado):
        raise ValueError({
            'errorType': 'token_not_expected',
            'line': self.current_token_line,
            'expected': esperado,
            'received': self.token
        })