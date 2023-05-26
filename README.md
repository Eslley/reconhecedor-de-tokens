# Projeto de Compiladores

Reconhecedor de tokens

URL Base: https://projeto-compiladores.vercel.app

* **POST /analisador**

    Request:
    ```
        {
            "input": "(c1+1)b*3a"
        }
    ```
        
    Response:
    ```
        {
            "tokens": {
                "ruleNames": [
                    "T__0",
                    "T__1",
                    "T__2",
                    "T__3",
                    "T__4",
                    "T__5",
                    "NEWLINE",
                    "INT"
                ],
                "recognizedTokens": [
                    {
                        "text": "(",
                        "type": "T__4",
                        "line": 1,
                        "column": 0
                    },
                    {
                        "text": "1",
                        "type": "INT",
                        "line": 1,
                        "column": 2
                    },
                    {
                        "text": "+",
                        "type": "T__2",
                        "line": 1,
                        "column": 3
                    },
                    {
                        "text": "1",
                        "type": "INT",
                        "line": 1,
                        "column": 4
                    },
                    {
                        "text": ")",
                        "type": "T__5",
                        "line": 1,
                        "column": 5
                    },
                    {
                        "text": "*",
                        "type": "T__0",
                        "line": 1,
                        "column": 7
                    },
                    {
                        "text": "3",
                        "type": "INT",
                        "line": 1,
                        "column": 8
                    }
                ],
                "nonRecognizedTokens": [
                    {
                        "text": "c",
                        "line": 1,
                        "column": 1
                    },
                    {
                        "text": "b",
                        "line": 1,
                        "column": 6
                    },
                    {
                        "text": "a",
                        "line": 1,
                        "column": 9
                    }
                ]
            }
        }
    ```
