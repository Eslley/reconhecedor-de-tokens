# Projeto da Disciplina de Compiladores

Reconhecedor de tokens em vagas de estágio/empregos na área de tecnologia

URL Base: https://projeto-compiladores.vercel.app

* **POST /parser**

* **POST /analisador**

    Request:
    ```
        {
            "input":  "sênior junior - 100% REMOTO júnior estágio\nSólida experiência com Java (Spring boot, maven, gradle, Spring Data, Spring mvc) pleno\nExperiência com bancos de dados Postgresql e Oracle. clt\nExperiência com aplicações distribuídas.\nExperiência com SaaS.\nConhecimento em cloud (AWS, desejável OCI).\nConhecimento em protocolos de autenticação (OAuth)\nSólidos conhecimentos em protocolos e padrões de comunicação e integração entre aplicações.\n\nPrazo: 06 meses - com possibilidade de prorrogação\nAtuação 100% Remoto\nEnviar currículo para recrutamento@infovagas.com indicando no assunto: \"JAVA - 100% REMOTO\"\nContato: (11) 98129-9574\nCompartilhe com seus contatos\nIndique Amigos"
        }
    ```
        
    Response:
    ```
        {
            "ruleNames": [
                "CONHECIMENTOS",
                "MODALIDADE",
                "BENEFICIOS",
                "TIPO_DE_VAGA",
                "SENIORIDADE",
                "SALARIO",
                "AREA",
                "FRAMEWORKS_BACKEND",
                "FRAMEWORKS_FRONTEND",
                "FRAMEWORKS_MOBILE",
                "SOFTSKILLS",
                "LINGUAGENS",
                "Space",
                "PALAVRA",
                "ESPECIAIS",
                "NUMEROS"
            ],
            "tokens": {
                "recognizedTokens": [
                    {
                        "text": "senior",
                        "type": "SENIORIDADE",
                        "line": 1,
                        "column": 0
                    },
                    {
                        "text": "junior",
                        "type": "SENIORIDADE",
                        "line": 1,
                        "column": 7
                    },
                    {
                        "text": "-",
                        "type": "ESPECIAIS",
                        "line": 1,
                        "column": 14
                    },
                    {
                        "text": "100",
                        "type": "NUMEROS",
                        "line": 1,
                        "column": 16
                    },
                    {
                        "text": "%",
                        "type": "ESPECIAIS",
                        "line": 1,
                        "column": 19
                    },
                    {
                        "text": "REMOTO",
                        "type": "MODALIDADE",
                        "line": 1,
                        "column": 21
                    },
                    {
                        "text": "junior",
                        "type": "SENIORIDADE",
                        "line": 1,
                        "column": 28
                    },
                    {
                        "text": "estagio",
                        "type": "TIPO_DE_VAGA",
                        "line": 1,
                        "column": 35
                    },
                ],
                "nonRecognizedTokens": []
            }
        }
    ```
