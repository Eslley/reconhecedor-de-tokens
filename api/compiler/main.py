import os
    
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from .LanguageLexer import LanguageLexer
from .LanguageListener import LanguageListener
from .LanguageParser import LanguageParser
from antlr4.error.ErrorListener import ErrorListener


class ParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f'line {line}:{column} {msg}')

def compile(stream):
    try:
        input_stream = InputStream(stream)
        lexer = LanguageLexer(input_stream)
            
        tokens = CommonTokenStream(lexer)
        parser = LanguageParser(tokens)

        parserErrorListener = ParserErrorListener()

        parser.removeErrorListeners()
        parser.addErrorListener(parserErrorListener)

        tree = parser.prog()
        walker = ParseTreeWalker()
        l = LanguageListener()
        walker.walk(l, tree)

        return generate_class_program()
    except Exception as e:
        return {
            'error': str(e)
        }


def generate_class_program():
    os.system('java -jar jasmin.jar Program.j')
    return True
