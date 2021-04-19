## Requisitos do Trabalho

- [x] 4 tipos, sendo int e float obrigatórios;
- [x] Instância e uso de classes;
- [x] Definição e chamada de funções;
- [x] Estruturas de controle if-then-else e switch-case.
- [x] Laços for e while;
- [x] Operações \*, /, +, -, >, <, <=, >= e == seguindo essa ordem de precedência;
- [x] Possibilidade de definir a precedência de operações usando parênteses.

## Como rodar

Gerar arquivos Java

```sh
antlr4 pir/parser/pir.g4 -o build/
javac build/pir/parser/*.java
cd build/pir/parser/
grun pir start -gui < ../../../input.pir
```

ou

```sh
antlr4 pir/parser/pir.g4 -o build/ && javac build/pir/parser/*java && cd build/pir/parser/ && grun pir start -gui < ../../../input.pir && cd ../../../
```

Gerar arquivos python

```sh
antlr4 -Dlanguage=Python3 -visitor -no-listener pir/parser/pir.g4
```

ou

```py
python -m pir input.pir
```
