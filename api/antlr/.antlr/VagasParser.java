// Generated from c:\Users\VAIO\Desktop\compiladores\antlr\api\antlr\Vagas.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class VagasParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CONHECIMENTOS=1, MODALIDADE=2, BENEFICIOS=3, TIPO_DE_VAGA=4, SENIORIDADE=5, 
		SALARIO=6, AREA=7, FRAMEWORKS_BACKEND=8, FRAMEWORKS_FRONTEND=9, FRAMEWORKS_MOBILE=10, 
		SOFTSKILLS=11, LINGUAGENS=12, Space=13, PALAVRA=14, ESPECIAIS=15, NUMEROS=16;
	public static final int
		RULE_ini = 0;
	private static String[] makeRuleNames() {
		return new String[] {
			"ini"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CONHECIMENTOS", "MODALIDADE", "BENEFICIOS", "TIPO_DE_VAGA", "SENIORIDADE", 
			"SALARIO", "AREA", "FRAMEWORKS_BACKEND", "FRAMEWORKS_FRONTEND", "FRAMEWORKS_MOBILE", 
			"SOFTSKILLS", "LINGUAGENS", "Space", "PALAVRA", "ESPECIAIS", "NUMEROS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Vagas.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public VagasParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class IniContext extends ParserRuleContext {
		public List<TerminalNode> TIPO_DE_VAGA() { return getTokens(VagasParser.TIPO_DE_VAGA); }
		public TerminalNode TIPO_DE_VAGA(int i) {
			return getToken(VagasParser.TIPO_DE_VAGA, i);
		}
		public List<TerminalNode> CONHECIMENTOS() { return getTokens(VagasParser.CONHECIMENTOS); }
		public TerminalNode CONHECIMENTOS(int i) {
			return getToken(VagasParser.CONHECIMENTOS, i);
		}
		public List<TerminalNode> MODALIDADE() { return getTokens(VagasParser.MODALIDADE); }
		public TerminalNode MODALIDADE(int i) {
			return getToken(VagasParser.MODALIDADE, i);
		}
		public List<TerminalNode> BENEFICIOS() { return getTokens(VagasParser.BENEFICIOS); }
		public TerminalNode BENEFICIOS(int i) {
			return getToken(VagasParser.BENEFICIOS, i);
		}
		public List<TerminalNode> SENIORIDADE() { return getTokens(VagasParser.SENIORIDADE); }
		public TerminalNode SENIORIDADE(int i) {
			return getToken(VagasParser.SENIORIDADE, i);
		}
		public List<TerminalNode> SALARIO() { return getTokens(VagasParser.SALARIO); }
		public TerminalNode SALARIO(int i) {
			return getToken(VagasParser.SALARIO, i);
		}
		public List<TerminalNode> AREA() { return getTokens(VagasParser.AREA); }
		public TerminalNode AREA(int i) {
			return getToken(VagasParser.AREA, i);
		}
		public List<TerminalNode> FRAMEWORKS_BACKEND() { return getTokens(VagasParser.FRAMEWORKS_BACKEND); }
		public TerminalNode FRAMEWORKS_BACKEND(int i) {
			return getToken(VagasParser.FRAMEWORKS_BACKEND, i);
		}
		public List<TerminalNode> FRAMEWORKS_FRONTEND() { return getTokens(VagasParser.FRAMEWORKS_FRONTEND); }
		public TerminalNode FRAMEWORKS_FRONTEND(int i) {
			return getToken(VagasParser.FRAMEWORKS_FRONTEND, i);
		}
		public List<TerminalNode> FRAMEWORKS_MOBILE() { return getTokens(VagasParser.FRAMEWORKS_MOBILE); }
		public TerminalNode FRAMEWORKS_MOBILE(int i) {
			return getToken(VagasParser.FRAMEWORKS_MOBILE, i);
		}
		public List<TerminalNode> SOFTSKILLS() { return getTokens(VagasParser.SOFTSKILLS); }
		public TerminalNode SOFTSKILLS(int i) {
			return getToken(VagasParser.SOFTSKILLS, i);
		}
		public List<TerminalNode> LINGUAGENS() { return getTokens(VagasParser.LINGUAGENS); }
		public TerminalNode LINGUAGENS(int i) {
			return getToken(VagasParser.LINGUAGENS, i);
		}
		public List<TerminalNode> Space() { return getTokens(VagasParser.Space); }
		public TerminalNode Space(int i) {
			return getToken(VagasParser.Space, i);
		}
		public List<TerminalNode> PALAVRA() { return getTokens(VagasParser.PALAVRA); }
		public TerminalNode PALAVRA(int i) {
			return getToken(VagasParser.PALAVRA, i);
		}
		public List<TerminalNode> ESPECIAIS() { return getTokens(VagasParser.ESPECIAIS); }
		public TerminalNode ESPECIAIS(int i) {
			return getToken(VagasParser.ESPECIAIS, i);
		}
		public List<TerminalNode> NUMEROS() { return getTokens(VagasParser.NUMEROS); }
		public TerminalNode NUMEROS(int i) {
			return getToken(VagasParser.NUMEROS, i);
		}
		public IniContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ini; }
	}

	public final IniContext ini() throws RecognitionException {
		IniContext _localctx = new IniContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_ini);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(5);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CONHECIMENTOS) | (1L << MODALIDADE) | (1L << BENEFICIOS) | (1L << TIPO_DE_VAGA) | (1L << SENIORIDADE) | (1L << SALARIO) | (1L << AREA) | (1L << FRAMEWORKS_BACKEND) | (1L << FRAMEWORKS_FRONTEND) | (1L << FRAMEWORKS_MOBILE) | (1L << SOFTSKILLS) | (1L << LINGUAGENS) | (1L << Space) | (1L << PALAVRA) | (1L << ESPECIAIS) | (1L << NUMEROS))) != 0)) {
				{
				{
				setState(2);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CONHECIMENTOS) | (1L << MODALIDADE) | (1L << BENEFICIOS) | (1L << TIPO_DE_VAGA) | (1L << SENIORIDADE) | (1L << SALARIO) | (1L << AREA) | (1L << FRAMEWORKS_BACKEND) | (1L << FRAMEWORKS_FRONTEND) | (1L << FRAMEWORKS_MOBILE) | (1L << SOFTSKILLS) | (1L << LINGUAGENS) | (1L << Space) | (1L << PALAVRA) | (1L << ESPECIAIS) | (1L << NUMEROS))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(7);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22\13\4\2\t\2\3\2"+
		"\7\2\6\n\2\f\2\16\2\t\13\2\3\2\2\2\3\2\2\3\3\2\3\22\2\n\2\7\3\2\2\2\4"+
		"\6\t\2\2\2\5\4\3\2\2\2\6\t\3\2\2\2\7\5\3\2\2\2\7\b\3\2\2\2\b\3\3\2\2\2"+
		"\t\7\3\2\2\2\3\7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}