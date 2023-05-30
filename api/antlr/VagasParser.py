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
        4,1,450,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,
        0,30,8,0,10,0,12,0,33,9,0,1,1,1,1,1,2,1,2,1,3,1,3,4,3,41,8,3,11,
        3,12,3,42,1,3,1,3,3,3,47,8,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,8,1,0,1,9,1,0,
        10,14,1,0,15,18,1,0,19,87,2,0,46,46,88,175,3,0,121,122,127,129,176,
        230,1,0,231,344,8,0,88,95,97,103,105,105,111,112,131,137,152,152,
        171,173,345,446,61,0,31,1,0,0,0,2,34,1,0,0,0,4,36,1,0,0,0,6,38,1,
        0,0,0,8,48,1,0,0,0,10,50,1,0,0,0,12,52,1,0,0,0,14,54,1,0,0,0,16,
        56,1,0,0,0,18,58,1,0,0,0,20,30,3,2,1,0,21,30,3,4,2,0,22,30,3,6,3,
        0,23,30,3,8,4,0,24,30,3,10,5,0,25,30,3,12,6,0,26,30,3,14,7,0,27,
        30,3,16,8,0,28,30,3,18,9,0,29,20,1,0,0,0,29,21,1,0,0,0,29,22,1,0,
        0,0,29,23,1,0,0,0,29,24,1,0,0,0,29,25,1,0,0,0,29,26,1,0,0,0,29,27,
        1,0,0,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,
        32,1,1,0,0,0,33,31,1,0,0,0,34,35,7,0,0,0,35,3,1,0,0,0,36,37,7,1,
        0,0,37,5,1,0,0,0,38,40,5,447,0,0,39,41,5,449,0,0,40,39,1,0,0,0,41,
        42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,46,1,0,0,0,44,45,5,448,
        0,0,45,47,5,449,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,7,1,0,0,0,48,
        49,7,2,0,0,49,9,1,0,0,0,50,51,7,3,0,0,51,11,1,0,0,0,52,53,7,4,0,
        0,53,13,1,0,0,0,54,55,7,5,0,0,55,15,1,0,0,0,56,57,7,6,0,0,57,17,
        1,0,0,0,58,59,7,7,0,0,59,19,1,0,0,0,4,29,31,42,46
    ]

class VagasParser ( Parser ):

    grammarFileName = "Vagas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'est\\u00C3\\u00A1gio'", "'estagio'", 
                     "'estagi\\u00C3\\u00A1rio'", "'estagiario'", "'pj'", 
                     "'pessoa jur\\u00C3\\u00ADdica'", "'pessoa juridica'", 
                     "'clt'", "'carteira assinada'", "'j\\u00C3\\u00BAnior'", 
                     "'junior'", "'pleno'", "'s\\u00C3\\u00AAnior'", "'senior'", 
                     "'backend'", "'frontend'", "'fullstack'", "'mobile'", 
                     "'Spring boot'", "'Express'", "'Django'", "'Ruby on Rails'", 
                     "'ASP.NET'", "'Spring Boot'", "'Flask'", "'Laravel'", 
                     "'Play Framework'", "'CakePHP'", "'Symfony'", "'Phoenix'", 
                     "'Koa'", "'NestJS'", "'Gin'", "'Rocket'", "'Actix'", 
                     "'Vapor'", "'Perfect'", "'Kitura'", "'Echo'", "'Fastify'", 
                     "'Feathers'", "'Hapi'", "'AdonisJS'", "'Sails.js'", 
                     "'LoopBack'", "'Meteor'", "'Strapi'", "'Sinatra'", 
                     "'Hanami'", "'JHipster'", "'Grails'", "'Micronaut'", 
                     "'Quarkus'", "'Helidon'", "'Vert.x'", "'Scalatra'", 
                     "'Finatra'", "'Ktor'", "'Ratpack'", "'Dropwizard'", 
                     "'Jersey'", "'Spark'", "'Tornado'", "'Flask-RESTful'", 
                     "'Bottle'", "'Connexion'", "'FastAPI'", "'Slim'", "'Lumen'", 
                     "'Phalcon'", "'Zikula'", "'Xataface'", "'Cachet'", 
                     "'Mojolicious'", "'Catalyst'", "'Dancer'", "'Plack'", 
                     "'Wicket'", "'Tapestry'", "'Seam'", "'VRaptor'", "'JSF'", 
                     "'Grain'", "'Agavi'", "'KumbiaPHP'", "'ZK'", "'Agnostic'", 
                     "'React'", "'Angular'", "'Vue.js'", "'Ember.js'", "'Backbone.js'", 
                     "'Polymer'", "'Aurelia'", "'Svelte'", "'Preact'", "'Stencil'", 
                     "'Mithril'", "'Knockout.js'", "'Alpine.js'", "'Nuxt.js'", 
                     "'Next.js'", "'Gatsby'", "'Riot.js'", "'Marko'", "'Dojo'", 
                     "'Inferno'", "'Quasar'", "'Emotion'", "'Chakra UI'", 
                     "'Tailwind CSS'", "'Bootstrap'", "'Foundation'", "'Bulma'", 
                     "'Material-UI'", "'Ant Design'", "'Semantic UI'", "'UIKit'", 
                     "'Vuetify'", "'PrimeReact'", "'Onsen UI'", "'Ionic'", 
                     "'Quill'", "'Draft.js'", "'React Router'", "'Vue Router'", 
                     "'React Native'", "'Flutter'", "'NativeScript'", "'Electron'", 
                     "'Parcel'", "'Webpack'", "'Rollup'", "'Gulp'", "'Grunt'", 
                     "'Babel'", "'TypeScript'", "'ESLint'", "'Prettier'", 
                     "'Jest'", "'Mocha'", "'Cypress'", "'Storybook'", "'Enzyme'", 
                     "'Redux'", "'Mobx'", "'Vuex'", "'RxJS'", "'GraphQL'", 
                     "'Apollo Client'", "'Axios'", "'D3.js'", "'Chart.js'", 
                     "'Three.js'", "'GSAP'", "'Lodash'", "'Ramda'", "'Moment.js'", 
                     "'Day.js'", "'Numeral.js'", "'Framer Motion'", "'React Query'", 
                     "'SWR'", "'Zustand'", "'React Hook Form'", "'Formik'", 
                     "'Yup'", "'React Helmet'", "'Styled Components'", "'JSS'", 
                     "'Sass'", "'Less'", "'PostCSS'", "'CSS Modules'", "'Styled System'", 
                     "'Xamarin'", "'PhoneGap'", "'Cordova'", "'Unity'", 
                     "'Adobe AIR'", "'Kotlin Native'", "'Appcelerator Titanium'", 
                     "'Framework7'", "'Sencha Touch'", "'jQuery Mobile'", 
                     "'Marmalade SDK'", "'Corona SDK'", "'Cocos2d-x'", "'MoSync'", 
                     "'Felgo'", "'Qt'", "'ShiVa'", "'Appery.io'", "'Monaca'", 
                     "'Fuse'", "'React Native for Web'", "'Natives'", "'Weex'", 
                     "'Flutter Web'", "'Xamarin.Forms'", "'Adobe PhoneGap Build'", 
                     "'React Native Web'", "'Tabris.js'", "'Smartface'", 
                     "'Red Hat Mobile Application Platform'", "'Alpha Anywhere'", 
                     "'Xamarin.Android'", "'Xamarin.iOS'", "'Appcelerator'", 
                     "'ReactXP'", "'V-Play'", "'Gideros Mobile'", "'GameMaker Studio'", 
                     "'GoNative.io'", "'CoronaCards'", "'Haxe'", "'Defold'", 
                     "'jQWidgets'", "'DHTMLX Touch'", "'Noodl'", "'Fuseboxx'", 
                     "'GeneXus'", "'Kony'", "'SAP Fiori'", "'IBM MobileFirst Platform'", 
                     "'Kinvey'", "'Mendix'", "'OutSystems'", "'Xcode'", 
                     "'Android Studio'", "'Comunica\\u00C3\\u00A7\\u00C3\\u00A3o Efetiva'", 
                     "'Trabalho em Equipe'", "'Resolu\\u00C3\\u00A7\\u00C3\\u00A3o de Problemas'", 
                     "'Adaptabilidade'", "'Pensamento Cr\\u00C3\\u00ADtico'", 
                     "'Autodisciplina'", "'Aprendizagem Cont\\u00C3\\u00ADnua'", 
                     "'Criatividade'", "'Lideran\\u00C3\\u00A7a'", "'Resili\\u00C3\\u00AAncia'", 
                     "'Flexibilidade'", "'Colabora\\u00C3\\u00A7\\u00C3\\u00A3o'", 
                     "'Habilidades de Negocia\\u00C3\\u00A7\\u00C3\\u00A3o'", 
                     "'Gerenciamento de Tempo'", "'Organiza\\u00C3\\u00A7\\u00C3\\u00A3o'", 
                     "'Empatia'", "'Pensamento Anal\\u00C3\\u00ADtico'", 
                     "'Iniciativa'", "'Curiosidade'", "'Gest\\u00C3\\u00A3o de Conflitos'", 
                     "'Tomada de Decis\\u00C3\\u00A3o'", "'Foco no Cliente'", 
                     "'Mentalidade \\u00C3\\uFFFDgil'", "'Senso de Responsabilidade'", 
                     "'Capacidade de Lidar com a Press\\u00C3\\u00A3o'", 
                     "'Habilidades Interpessoais'", "'Respeito \\u00C3\\u00A0 Diversidade'", 
                     "'Habilidade de Lidar com Feedback'", "'Assertividade'", 
                     "'Habilidades de Apresenta\\u00C3\\u00A7\\u00C3\\u00A3o'", 
                     "'Lideran\\u00C3\\u00A7a Servidora'", "'Pensamento Sist\\u00C3\\u00AAmico'", 
                     "'Negocia\\u00C3\\u00A7\\u00C3\\u00A3o'", "'Capacidade de Lidar com Mudan\\u00C3\\u00A7as'", 
                     "'Orienta\\u00C3\\u00A7\\u00C3\\u00A3o a Resultados'", 
                     "'Vis\\u00C3\\u00A3o Estrat\\u00C3\\u00A9gica'", "'Habilidades de Facilita\\u00C3\\u00A7\\u00C3\\u00A3o'", 
                     "'Mentoria'", "'\\u00C3\\u2030tica Profissional'", 
                     "'Compreens\\u00C3\\u00A3o de Neg\\u00C3\\u00B3cios'", 
                     "'Gest\\u00C3\\u00A3o de Projetos'", "'Resolu\\u00C3\\u00A7\\u00C3\\u00A3o de Conflitos'", 
                     "'Comunica\\u00C3\\u00A7\\u00C3\\u00A3o Interpessoal'", 
                     "'Habilidades de Influ\\u00C3\\u00AAncia'", "'Intelig\\u00C3\\u00AAncia Emocional'", 
                     "'Orienta\\u00C3\\u00A7\\u00C3\\u00A3o para Detalhes'", 
                     "'Vis\\u00C3\\u00A3o de Produto'", "'Gerenciamento de Expectativas'", 
                     "'Habilidades de Coaching'", "'Pensamento Criativo'", 
                     "'Capacidade de Trabalhar sob Press\\u00C3\\u00A3o'", 
                     "'Habilidades de Facilita\\u00C3\\u00A7\\u00C3\\u00A3o de Reuni\\u00C3\\u00B5es'", 
                     "'Colabora\\u00C3\\u00A7\\u00C3\\u00A3o Multidisciplinar'", 
                     "'Orienta\\u00C3\\u00A7\\u00C3\\u00A3o para o Cliente'", 
                     "'Capacidade de Adapta\\u00C3\\u00A7\\u00C3\\u00A3o'", 
                     "'Resolu\\u00C3\\u00A7\\u00C3\\u00A3o de Problemas Complexos'", 
                     "'Gerenciamento de Conflitos'", "'Habilidades de Gest\\u00C3\\u00A3o de Equipes'", 
                     "'Proatividade'", "'Comunica de forma efetiva'", "'Trabalha em equipe'", 
                     "'Resolve problemas'", "'Adapta-se facilmente'", "'Pensa criticamente'", 
                     "'Demonstra autodisciplina'", "'Busca aprendizado cont\\u00C3\\u00ADnuo'", 
                     "'Apresenta criatividade'", "'Lidera'", "'Demonstra resili\\u00C3\\u00AAncia'", 
                     "'Mostra flexibilidade'", "'Colabora'", "'Possui habilidades de negocia\\u00C3\\u00A7\\u00C3\\u00A3o'", 
                     "'Gerencia o tempo'", "'Organiza-se'", "'Demonstra empatia'", 
                     "'Analisa de forma cr\\u00C3\\u00ADtica'", "'Demonstra iniciativa'", 
                     "'Demonstra curiosidade'", "'Gerencia conflitos'", 
                     "'Toma decis\\u00C3\\u00B5es'", "'Foca no cliente'", 
                     "'Possui mentalidade \\u00C3\\u00A1gil'", "'Assume responsabilidade'", 
                     "'Lida bem com press\\u00C3\\u00A3o'", "'Demonstra habilidades interpessoais'", 
                     "'Respeita a diversidade'", "'Lida bem com feedback'", 
                     "'\\u00C3\\u2030 assertivo'", "'Apresenta bem'", "'Demonstra lideran\\u00C3\\u00A7a servidora'", 
                     "'Possui pensamento sist\\u00C3\\u00AAmico'", "'Negocia'", 
                     "'Adapta-se a mudan\\u00C3\\u00A7as'", "'Orienta-se a resultados'", 
                     "'Possui vis\\u00C3\\u00A3o estrat\\u00C3\\u00A9gica'", 
                     "'Facilita'", "'Demonstra \\u00C3\\u00A9tica profissional'", 
                     "'Compreende neg\\u00C3\\u00B3cios'", "'Gerencia projetos'", 
                     "'Resolve conflitos'", "'Interage bem'", "'Influencia habilmente'", 
                     "'Possui intelig\\u00C3\\u00AAncia emocional'", "'Observa detalhes'", 
                     "'Tem vis\\u00C3\\u00A3o de produto'", "'Gerencia expectativas'", 
                     "'Coaching'", "'Pensa criativamente'", "'Facilita reuni\\u00C3\\u00B5es'", 
                     "'Colabora multidisciplinarmente'", "'Orienta-se ao cliente'", 
                     "'Resolve problemas complexos'", "'Gerencia equipes'", 
                     "'Demonstra proatividade'", "'Python'", "'Java'", "'C#'", 
                     "'Ruby'", "'PHP'", "'Go'", "'Rust'", "'JavaScript'", 
                     "'Scala'", "'Kotlin'", "'Swift'", "'Perl'", "'Groovy'", 
                     "'Haskell'", "'Lua'", "'Erlang'", "'Clojure'", "'Objective-C'", 
                     "'F#'", "'Dart'", "'Julia'", "'Elixir'", "'Scheme'", 
                     "'OCaml'", "'VB.NET'", "'PowerShell'", "'Shell Script'", 
                     "'Racket'", "'Fortran'", "'COBOL'", "'Pascal'", "'Lisp'", 
                     "'Ada'", "'Prolog'", "'Matlab'", "'Smalltalk'", "'Delphi'", 
                     "'ActionScript'", "'CoffeeScript'", "'LabVIEW'", "'Fora'", 
                     "'XPath'", "'XSLT'", "'HTML'", "'HTML5'", "'CSS'", 
                     "'jQuery'", "'Stylus'", "'WebAssembly'", "'Handlebars'", 
                     "'Mustache'", "'Pug'", "'Jade'", "'Elm'", "'ReasonML'", 
                     "'ClojureScript'", "'PureScript'", "'Glimmer.js'", 
                     "'Dojo Toolkit'", "'Browserify'", "'SQL'", "'MySQL'", 
                     "'PostgreSQL'", "'Oracle Database'", "'Microsoft SQL Server'", 
                     "'MongoDB'", "'Redis'", "'Cassandra'", "'SQLite'", 
                     "'MariaDB'", "'Amazon Aurora'", "'Google BigQuery'", 
                     "'IBM Db2'", "'Apache Hadoop'", "'Apache Hive'", "'Apache Cassandra'", 
                     "'Apache Kafka'", "'Apache Spark'", "'Neo4j'", "'Couchbase'", 
                     "'DynamoDB'", "'Firebase Realtime Database'", "'Realm'", 
                     "'CockroachDB'", "'ArangoDB'", "'RethinkDB'", "'InfluxDB'", 
                     "'Elasticsearch'", "'Amazon Redshift'", "'Teradata'", 
                     "'Sybase'", "'Informix'", "'Vertica'", "'RavenDB'", 
                     "'HBase'", "'Memcached'", "'VoltDB'", "'Snowflake'", 
                     "'Apache Derby'", "'Apache Lucene'", "'Cosmos DB'", 
                     "'Apache Solr'", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DOLAR", "PONTO", 
                      "DIGITO", "Space" ]

    RULE_ini = 0
    RULE_tipo_de_vaga = 1
    RULE_senioridade = 2
    RULE_salario = 3
    RULE_area = 4
    RULE_subareas_backend = 5
    RULE_subareas_frontend = 6
    RULE_subareas_mobile = 7
    RULE_softskills = 8
    RULE_linguagens = 9

    ruleNames =  [ "ini", "tipo_de_vaga", "senioridade", "salario", "area", 
                   "subareas_backend", "subareas_frontend", "subareas_mobile", 
                   "softskills", "linguagens" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    T__71=72
    T__72=73
    T__73=74
    T__74=75
    T__75=76
    T__76=77
    T__77=78
    T__78=79
    T__79=80
    T__80=81
    T__81=82
    T__82=83
    T__83=84
    T__84=85
    T__85=86
    T__86=87
    T__87=88
    T__88=89
    T__89=90
    T__90=91
    T__91=92
    T__92=93
    T__93=94
    T__94=95
    T__95=96
    T__96=97
    T__97=98
    T__98=99
    T__99=100
    T__100=101
    T__101=102
    T__102=103
    T__103=104
    T__104=105
    T__105=106
    T__106=107
    T__107=108
    T__108=109
    T__109=110
    T__110=111
    T__111=112
    T__112=113
    T__113=114
    T__114=115
    T__115=116
    T__116=117
    T__117=118
    T__118=119
    T__119=120
    T__120=121
    T__121=122
    T__122=123
    T__123=124
    T__124=125
    T__125=126
    T__126=127
    T__127=128
    T__128=129
    T__129=130
    T__130=131
    T__131=132
    T__132=133
    T__133=134
    T__134=135
    T__135=136
    T__136=137
    T__137=138
    T__138=139
    T__139=140
    T__140=141
    T__141=142
    T__142=143
    T__143=144
    T__144=145
    T__145=146
    T__146=147
    T__147=148
    T__148=149
    T__149=150
    T__150=151
    T__151=152
    T__152=153
    T__153=154
    T__154=155
    T__155=156
    T__156=157
    T__157=158
    T__158=159
    T__159=160
    T__160=161
    T__161=162
    T__162=163
    T__163=164
    T__164=165
    T__165=166
    T__166=167
    T__167=168
    T__168=169
    T__169=170
    T__170=171
    T__171=172
    T__172=173
    T__173=174
    T__174=175
    T__175=176
    T__176=177
    T__177=178
    T__178=179
    T__179=180
    T__180=181
    T__181=182
    T__182=183
    T__183=184
    T__184=185
    T__185=186
    T__186=187
    T__187=188
    T__188=189
    T__189=190
    T__190=191
    T__191=192
    T__192=193
    T__193=194
    T__194=195
    T__195=196
    T__196=197
    T__197=198
    T__198=199
    T__199=200
    T__200=201
    T__201=202
    T__202=203
    T__203=204
    T__204=205
    T__205=206
    T__206=207
    T__207=208
    T__208=209
    T__209=210
    T__210=211
    T__211=212
    T__212=213
    T__213=214
    T__214=215
    T__215=216
    T__216=217
    T__217=218
    T__218=219
    T__219=220
    T__220=221
    T__221=222
    T__222=223
    T__223=224
    T__224=225
    T__225=226
    T__226=227
    T__227=228
    T__228=229
    T__229=230
    T__230=231
    T__231=232
    T__232=233
    T__233=234
    T__234=235
    T__235=236
    T__236=237
    T__237=238
    T__238=239
    T__239=240
    T__240=241
    T__241=242
    T__242=243
    T__243=244
    T__244=245
    T__245=246
    T__246=247
    T__247=248
    T__248=249
    T__249=250
    T__250=251
    T__251=252
    T__252=253
    T__253=254
    T__254=255
    T__255=256
    T__256=257
    T__257=258
    T__258=259
    T__259=260
    T__260=261
    T__261=262
    T__262=263
    T__263=264
    T__264=265
    T__265=266
    T__266=267
    T__267=268
    T__268=269
    T__269=270
    T__270=271
    T__271=272
    T__272=273
    T__273=274
    T__274=275
    T__275=276
    T__276=277
    T__277=278
    T__278=279
    T__279=280
    T__280=281
    T__281=282
    T__282=283
    T__283=284
    T__284=285
    T__285=286
    T__286=287
    T__287=288
    T__288=289
    T__289=290
    T__290=291
    T__291=292
    T__292=293
    T__293=294
    T__294=295
    T__295=296
    T__296=297
    T__297=298
    T__298=299
    T__299=300
    T__300=301
    T__301=302
    T__302=303
    T__303=304
    T__304=305
    T__305=306
    T__306=307
    T__307=308
    T__308=309
    T__309=310
    T__310=311
    T__311=312
    T__312=313
    T__313=314
    T__314=315
    T__315=316
    T__316=317
    T__317=318
    T__318=319
    T__319=320
    T__320=321
    T__321=322
    T__322=323
    T__323=324
    T__324=325
    T__325=326
    T__326=327
    T__327=328
    T__328=329
    T__329=330
    T__330=331
    T__331=332
    T__332=333
    T__333=334
    T__334=335
    T__335=336
    T__336=337
    T__337=338
    T__338=339
    T__339=340
    T__340=341
    T__341=342
    T__342=343
    T__343=344
    T__344=345
    T__345=346
    T__346=347
    T__347=348
    T__348=349
    T__349=350
    T__350=351
    T__351=352
    T__352=353
    T__353=354
    T__354=355
    T__355=356
    T__356=357
    T__357=358
    T__358=359
    T__359=360
    T__360=361
    T__361=362
    T__362=363
    T__363=364
    T__364=365
    T__365=366
    T__366=367
    T__367=368
    T__368=369
    T__369=370
    T__370=371
    T__371=372
    T__372=373
    T__373=374
    T__374=375
    T__375=376
    T__376=377
    T__377=378
    T__378=379
    T__379=380
    T__380=381
    T__381=382
    T__382=383
    T__383=384
    T__384=385
    T__385=386
    T__386=387
    T__387=388
    T__388=389
    T__389=390
    T__390=391
    T__391=392
    T__392=393
    T__393=394
    T__394=395
    T__395=396
    T__396=397
    T__397=398
    T__398=399
    T__399=400
    T__400=401
    T__401=402
    T__402=403
    T__403=404
    T__404=405
    T__405=406
    T__406=407
    T__407=408
    T__408=409
    T__409=410
    T__410=411
    T__411=412
    T__412=413
    T__413=414
    T__414=415
    T__415=416
    T__416=417
    T__417=418
    T__418=419
    T__419=420
    T__420=421
    T__421=422
    T__422=423
    T__423=424
    T__424=425
    T__425=426
    T__426=427
    T__427=428
    T__428=429
    T__429=430
    T__430=431
    T__431=432
    T__432=433
    T__433=434
    T__434=435
    T__435=436
    T__436=437
    T__437=438
    T__438=439
    T__439=440
    T__440=441
    T__441=442
    T__442=443
    T__443=444
    T__444=445
    T__445=446
    DOLAR=447
    PONTO=448
    DIGITO=449
    Space=450

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

        def tipo_de_vaga(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagasParser.Tipo_de_vagaContext)
            else:
                return self.getTypedRuleContext(VagasParser.Tipo_de_vagaContext,i)


        def senioridade(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagasParser.SenioridadeContext)
            else:
                return self.getTypedRuleContext(VagasParser.SenioridadeContext,i)


        def salario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagasParser.SalarioContext)
            else:
                return self.getTypedRuleContext(VagasParser.SalarioContext,i)


        def area(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagasParser.AreaContext)
            else:
                return self.getTypedRuleContext(VagasParser.AreaContext,i)


        def subareas_backend(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagasParser.Subareas_backendContext)
            else:
                return self.getTypedRuleContext(VagasParser.Subareas_backendContext,i)


        def subareas_frontend(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagasParser.Subareas_frontendContext)
            else:
                return self.getTypedRuleContext(VagasParser.Subareas_frontendContext,i)


        def subareas_mobile(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagasParser.Subareas_mobileContext)
            else:
                return self.getTypedRuleContext(VagasParser.Subareas_mobileContext,i)


        def softskills(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagasParser.SoftskillsContext)
            else:
                return self.getTypedRuleContext(VagasParser.SoftskillsContext,i)


        def linguagens(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VagasParser.LinguagensContext)
            else:
                return self.getTypedRuleContext(VagasParser.LinguagensContext,i)


        def getRuleIndex(self):
            return VagasParser.RULE_ini




    def ini(self):

        localctx = VagasParser.IniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ini)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -2) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & -1) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & -1) != 0) or ((((_la - 192)) & ~0x3f) == 0 and ((1 << (_la - 192)) & -1) != 0) or ((((_la - 256)) & ~0x3f) == 0 and ((1 << (_la - 256)) & -1) != 0) or ((((_la - 320)) & ~0x3f) == 0 and ((1 << (_la - 320)) & -1) != 0) or ((((_la - 384)) & ~0x3f) == 0 and ((1 << (_la - 384)) & -1) != 0):
                self.state = 29
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 20
                    self.tipo_de_vaga()
                    pass

                elif la_ == 2:
                    self.state = 21
                    self.senioridade()
                    pass

                elif la_ == 3:
                    self.state = 22
                    self.salario()
                    pass

                elif la_ == 4:
                    self.state = 23
                    self.area()
                    pass

                elif la_ == 5:
                    self.state = 24
                    self.subareas_backend()
                    pass

                elif la_ == 6:
                    self.state = 25
                    self.subareas_frontend()
                    pass

                elif la_ == 7:
                    self.state = 26
                    self.subareas_mobile()
                    pass

                elif la_ == 8:
                    self.state = 27
                    self.softskills()
                    pass

                elif la_ == 9:
                    self.state = 28
                    self.linguagens()
                    pass


                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipo_de_vagaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VagasParser.RULE_tipo_de_vaga




    def tipo_de_vaga(self):

        localctx = VagasParser.Tipo_de_vagaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tipo_de_vaga)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1022) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SenioridadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VagasParser.RULE_senioridade




    def senioridade(self):

        localctx = VagasParser.SenioridadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_senioridade)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SalarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLAR(self):
            return self.getToken(VagasParser.DOLAR, 0)

        def DIGITO(self, i:int=None):
            if i is None:
                return self.getTokens(VagasParser.DIGITO)
            else:
                return self.getToken(VagasParser.DIGITO, i)

        def PONTO(self):
            return self.getToken(VagasParser.PONTO, 0)

        def getRuleIndex(self):
            return VagasParser.RULE_salario




    def salario(self):

        localctx = VagasParser.SalarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_salario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(VagasParser.DOLAR)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.match(VagasParser.DIGITO)
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==449):
                    break

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==448:
                self.state = 44
                self.match(VagasParser.PONTO)
                self.state = 45
                self.match(VagasParser.DIGITO)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AreaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VagasParser.RULE_area




    def area(self):

        localctx = VagasParser.AreaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_area)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subareas_backendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VagasParser.RULE_subareas_backend




    def subareas_backend(self):

        localctx = VagasParser.Subareas_backendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_subareas_backend)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -524288) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 16777215) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subareas_frontendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VagasParser.RULE_subareas_frontend




    def subareas_frontend(self):

        localctx = VagasParser.Subareas_frontendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subareas_frontend)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not(_la==46 or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & -1) != 0) or ((((_la - 152)) & ~0x3f) == 0 and ((1 << (_la - 152)) & 16777215) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subareas_mobileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VagasParser.RULE_subareas_mobile




    def subareas_mobile(self):

        localctx = VagasParser.Subareas_mobileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_subareas_mobile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not(((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & -36028797018963517) != 0) or ((((_la - 185)) & ~0x3f) == 0 and ((1 << (_la - 185)) & 70368744177663) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SoftskillsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VagasParser.RULE_softskills




    def softskills(self):

        localctx = VagasParser.SoftskillsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_softskills)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not(((((_la - 231)) & ~0x3f) == 0 and ((1 << (_la - 231)) & -1) != 0) or ((((_la - 295)) & ~0x3f) == 0 and ((1 << (_la - 295)) & 1125899906842623) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinguagensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VagasParser.RULE_linguagens




    def linguagens(self):

        localctx = VagasParser.LinguagensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_linguagens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & 1117103839182591) != 0) or ((((_la - 152)) & ~0x3f) == 0 and ((1 << (_la - 152)) & 3670017) != 0) or ((((_la - 345)) & ~0x3f) == 0 and ((1 << (_la - 345)) & -1) != 0) or ((((_la - 409)) & ~0x3f) == 0 and ((1 << (_la - 409)) & 274877906943) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





