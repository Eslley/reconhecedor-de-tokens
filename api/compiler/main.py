import os
    
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from .LanguageLexer import LanguageLexer
from .LanguageListener import LanguageListener
from .LanguageParser import LanguageParser


def compile(stream):
    input_stream = InputStream(stream)
    lexer = LanguageLexer(input_stream)
        
    tokens = CommonTokenStream(lexer)
    parser = LanguageParser(tokens)

    tree = parser.prog()
    walker = ParseTreeWalker()
    l = LanguageListener()
    walker.walk(l, tree)

    return generate_class_program()


def generate_class_program():
    os.system('java -jar jasmin.jar Program.j')
    
    with open('Program.class', 'r') as f:
        javaProgram = f.read()
        return javaProgram
