from antlr4 import *
from api.antlr.MyGrammarLexer import MyGrammarLexer


class Error:

    def __init__(self):
        self.nonRecognizedTokens = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        text = e.input.getText(e.startIndex, e.startIndex)

        self.nonRecognizedTokens.append({
            'text': text,
            'line': line, 
            'column': column 
        })


def processInput(input_string: str):
    input_stream = InputStream(input_string)

    lexer = MyGrammarLexer(input_stream)

    errorListener = Error()

    lexer.removeErrorListeners() 
    lexer.addErrorListener(errorListener)  

    recognizedTokens = []

    for token in lexer.getAllTokens():
        recognizedTokens.append({
            'text': token.text,
            'type': lexer.ruleNames[token.type-1], 
            'line': token.line, 
            'column': token.column 
        })

    return {
        'ruleNames': lexer.ruleNames,
        'recognizedTokens': recognizedTokens,
        'nonRecognizedTokens': errorListener.nonRecognizedTokens
    }
