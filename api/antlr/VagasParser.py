# Generated from Vagas.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,9,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,0,0,1,0,0,1,2,
        0,1,3,7,12,8,0,5,1,0,0,0,2,4,7,0,0,0,3,2,1,0,0,0,4,7,1,0,0,0,5,3,
        1,0,0,0,5,6,1,0,0,0,6,1,1,0,0,0,7,5,1,0,0,0,1,5
    ]

class VagasParser ( Parser ):

    grammarFileName = "Vagas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "TIPO_DE_VAGA", "SENIORIDADE", "SALARIO", 
                      "DOLAR", "PONTO", "DIGITO", "AREA", "SUBAREAS_BACKEND", 
                      "SUBAREAS_FRONTEND", "SUBAREAS_MOBILE", "SOFTSKILLS", 
                      "LINGUAGENS", "SPACE" ]

    RULE_ini = 0

    ruleNames =  [ "ini" ]

    EOF = Token.EOF
    TIPO_DE_VAGA=1
    SENIORIDADE=2
    SALARIO=3
    DOLAR=4
    PONTO=5
    DIGITO=6
    AREA=7
    SUBAREAS_BACKEND=8
    SUBAREAS_FRONTEND=9
    SUBAREAS_MOBILE=10
    SOFTSKILLS=11
    LINGUAGENS=12
    SPACE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class IniContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINGUAGENS(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.LINGUAGENS)
            else:
                return self.getToken(VagasParser.LINGUAGENS, i)

        def TIPO_DE_VAGA(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.TIPO_DE_VAGA)
            else:
                return self.getToken(VagasParser.TIPO_DE_VAGA, i)

        def SENIORIDADE(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.SENIORIDADE)
            else:
                return self.getToken(VagasParser.SENIORIDADE, i)

        def SALARIO(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.SALARIO)
            else:
                return self.getToken(VagasParser.SALARIO, i)

        def AREA(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.AREA)
            else:
                return self.getToken(VagasParser.AREA, i)

        def SUBAREAS_BACKEND(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.SUBAREAS_BACKEND)
            else:
                return self.getToken(VagasParser.SUBAREAS_BACKEND, i)

        def SUBAREAS_FRONTEND(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.SUBAREAS_FRONTEND)
            else:
                return self.getToken(VagasParser.SUBAREAS_FRONTEND, i)

        def SUBAREAS_MOBILE(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.SUBAREAS_MOBILE)
            else:
                return self.getToken(VagasParser.SUBAREAS_MOBILE, i)

        def SOFTSKILLS(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.SOFTSKILLS)
            else:
                return self.getToken(VagasParser.SOFTSKILLS, i)

        def getRuleIndex(self):
            return VagasParser.RULE_ini

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIni" ):
                listener.enterIni(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIni" ):
                listener.exitIni(self)




    def ini(self):

        localctx = VagasParser.IniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ini)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8078) != 0):
                self.state = 2
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8078) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





