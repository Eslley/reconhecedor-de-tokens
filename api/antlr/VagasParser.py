# Generated from C:/Users/Jhoisnayra/PycharmProjects/pythonProject\Vagas.g4 by ANTLR 4.12.0
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
        4,1,16,9,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,0,0,1,0,0,1,1,
        0,1,15,8,0,5,1,0,0,0,2,4,7,0,0,0,3,2,1,0,0,0,4,7,1,0,0,0,5,3,1,0,
        0,0,5,6,1,0,0,0,6,1,1,0,0,0,7,5,1,0,0,0,1,5
    ]

class VagasParser ( Parser ):

    grammarFileName = "Vagas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "CONHECIMENTOS", "MODALIDADE", "BENEFICIOS", 
                      "TIPO_DE_VAGA", "SENIORIDADE", "SALARIO", "AREA", 
                      "FRAMEWORKS_BACKEND", "FRAMEWORKS_FRONTEND", "FRAMEWORKS_MOBILE", 
                      "SOFTSKILLS", "LINGUAGENS", "Space", "PALAVRA", "ESPECIAIS", 
                      "NUMEROS" ]

    RULE_ini = 0

    ruleNames =  [ "ini" ]

    EOF = Token.EOF
    CONHECIMENTOS=1
    MODALIDADE=2
    BENEFICIOS=3
    TIPO_DE_VAGA=4
    SENIORIDADE=5
    SALARIO=6
    AREA=7
    FRAMEWORKS_BACKEND=8
    FRAMEWORKS_FRONTEND=9
    FRAMEWORKS_MOBILE=10
    SOFTSKILLS=11
    LINGUAGENS=12
    Space=13
    PALAVRA=14
    ESPECIAIS=15
    NUMEROS=16

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

        def TIPO_DE_VAGA(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.TIPO_DE_VAGA)
            else:
                return self.getToken(VagasParser.TIPO_DE_VAGA, i)

        def CONHECIMENTOS(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.CONHECIMENTOS)
            else:
                return self.getToken(VagasParser.CONHECIMENTOS, i)

        def MODALIDADE(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.MODALIDADE)
            else:
                return self.getToken(VagasParser.MODALIDADE, i)

        def BENEFICIOS(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.BENEFICIOS)
            else:
                return self.getToken(VagasParser.BENEFICIOS, i)

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

        def FRAMEWORKS_BACKEND(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.FRAMEWORKS_BACKEND)
            else:
                return self.getToken(VagasParser.FRAMEWORKS_BACKEND, i)

        def FRAMEWORKS_FRONTEND(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.FRAMEWORKS_FRONTEND)
            else:
                return self.getToken(VagasParser.FRAMEWORKS_FRONTEND, i)

        def FRAMEWORKS_MOBILE(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.FRAMEWORKS_MOBILE)
            else:
                return self.getToken(VagasParser.FRAMEWORKS_MOBILE, i)

        def SOFTSKILLS(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.SOFTSKILLS)
            else:
                return self.getToken(VagasParser.SOFTSKILLS, i)

        def LINGUAGENS(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.LINGUAGENS)
            else:
                return self.getToken(VagasParser.LINGUAGENS, i)

        def Space(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.Space)
            else:
                return self.getToken(VagasParser.Space, i)

        def PALAVRA(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.PALAVRA)
            else:
                return self.getToken(VagasParser.PALAVRA, i)

        def ESPECIAIS(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.ESPECIAIS)
            else:
                return self.getToken(VagasParser.ESPECIAIS, i)

        def getRuleIndex(self):
            return VagasParser.RULE_ini




    def ini(self):

        localctx = VagasParser.IniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ini)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 65534) != 0):
                self.state = 2
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65534) != 0)):
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





