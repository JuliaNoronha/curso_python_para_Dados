# Python para Dados — Aquecendo na Programação

Este material reúne os principais conceitos de Python usados nos exercícios iniciais do curso de **Python para Dados**, com foco em lógica de programação antes de depender das facilidades prontas da linguagem.

## Conteúdos

- `input()`
- `int()` e `float()`
- `if`, `elif` e `else`
- Operadores de comparação
- Operadores lógicos `and` e `or`
- Operador módulo `%`
- Comparação entre valores
- Tratamento de empates
- Maior e menor valor
- Par ou ímpar
- Positivo ou negativo
- Inteiro ou decimal
- Listas e dicionários

---

## 1. Entrada de dados

A função `input()` recebe informações digitadas pela pessoa usuária.

```python
nome = input("Digite seu nome: ")
```

Por padrão, `input()` retorna uma `str`.

Para trabalhar com números:

```python
idade = int(input("Digite sua idade: "))
preco = float(input("Digite o preço: "))
```

---

## 2. Estruturas condicionais

```python
if condicao:
    ...
elif outra_condicao:
    ...
else:
    ...
```

Exemplo:

```python
idade = 20

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
```

---

## 3. Operadores de comparação

| Operador | Significado |
|---|---|
| `==` | igual |
| `!=` | diferente |
| `>` | maior |
| `<` | menor |
| `>=` | maior ou igual |
| `<=` | menor ou igual |

---

## 4. Operadores lógicos

### `and`

Todas as condições precisam ser verdadeiras.

```python
if numero > 0 and numero < 100:
    print("Está entre 0 e 100.")
```

### `or`

Pelo menos uma condição precisa ser verdadeira.

```python
if turno == "manhã" or turno == "manha":
    print("Bom Dia!")
```

---

## 5. Comparando valores manualmente

Antes de utilizar `min()` e `max()`, podemos fazer a comparação manualmente.

Para descobrir se `a` é o menor:

```python
if a < b and a < c:
    print("A é o menor.")
```

### Atenção

Isto:

```python
if a < b and c:
```

não significa:

```text
a < b E a < c
```

O Python interpreta como:

```text
(a < b) E c
```

O correto é repetir a comparação:

```python
if a < b and a < c:
```

---

## 6. Tratamento de empates

No exercício dos produtos, existem vários casos possíveis.

```python
if macarrao == trigo == arroz:
    print("Os três possuem o mesmo preço.")

elif macarrao == trigo < arroz:
    print("Macarrão e trigo são os mais baratos.")

elif macarrao == arroz < trigo:
    print("Macarrão e arroz são os mais baratos.")

elif trigo == arroz < macarrao:
    print("Trigo e arroz são os mais baratos.")
```

Depois dos empates, podemos testar o menor individualmente:

```python
elif macarrao < trigo and macarrao < arroz:
    print("Macarrão é o mais barato.")
```

---

## 7. `min()` e `max()`

Depois de entender a comparação manual, Python oferece funções prontas:

```python
menor = min(10, 5, 7)
maior = max(10, 5, 7)
```

---

## 8. Par ou ímpar

O operador `%` retorna o resto de uma divisão.

```python
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
```

---

## 9. Positivo, negativo ou zero

```python
if numero > 0:
    print("Positivo.")
elif numero < 0:
    print("Negativo.")
else:
    print("Zero.")
```

---

## 10. Inteiro ou decimal

```python
numero = 10.5

if numero == int(numero):
    print("Inteiro.")
else:
    print("Decimal.")
```

---

## 11. Trabalhando com texto

Podemos normalizar uma entrada:

```python
turno = input("Digite seu turno: ").strip().lower()
```

Isso ajuda a tratar variações de maiúsculas, minúsculas e espaços extras.

---

## 12. Listas

```python
precos = [5.50, 7.00, 4.80]
```

Acesso por índice:

```python
print(precos[0])
```

Também podemos usar:

```python
min(precos)
max(precos)
```

---

## 13. Dicionários

Dicionários relacionam uma chave a um valor.

```python
produtos = {
    "macarrão": 5.50,
    "trigo": 4.00,
    "arroz": 7.00
}
```

Aqui temos:

```text
produto -> preço
```

Para acessar:

```python
produtos["macarrão"]
```

---

# Exercícios

## 1. Maior entre dois números

Pratique:

- `input()`
- `int()` ou `float()`
- `if`
- `elif`
- `else`
- `>` e `<`

Pense também no empate.

---

## 2. Crescimento ou decrescimento

Analise:

```text
valor > 0
valor < 0
valor == 0
```

---

## 3. Vogal ou consoante

Pratique:

- strings
- comparação
- `or`
- `.lower()`

Vogais:

```text
a, e, i, o, u
```

---

## 4. Maior e menor preço em três anos

Resolva primeiro manualmente.

Depois compare com:

```python
min()
max()
```

---

## 5. Produto mais barato

Entrada:

```python
macarrao = float(input("Preço do macarrão: "))
trigo = float(input("Preço do trigo: "))
arroz = float(input("Preço do arroz: "))
```

Antes de procurar o menor, pense nos empates:

```text
macarrão = trigo = arroz
macarrão = trigo < arroz
macarrão = arroz < trigo
trigo = arroz < macarrão
```

Depois verifique:

```text
macarrão < trigo e arroz
trigo < macarrão e arroz
arroz < macarrão e trigo
```

---

## 6. Ordem decrescente

Objetivo:

```text
maior
↓
meio
↓
menor
```

Depois de entender a lógica manual, você pode estudar `sorted()`.

---

## 7. Turno de estudo

```text
manhã -> Bom Dia!
tarde -> Boa Tarde!
noite -> Boa Noite!
outro -> Valor Inválido!
```

---

## 8. Par ou ímpar

Pergunta principal:

```text
o resto da divisão por 2 é zero?
```

---

## 9. Inteiro ou decimal

Exemplos:

```text
10.0 -> inteiro
10.7 -> decimal
```

---

# Momento dos Projetos

## 10. Calculadora com análise do resultado

Fluxo:

```text
número 1
   ↓
número 2
   ↓
operação
   ↓
resultado
   ↓
par ou ímpar
positivo ou negativo
inteiro ou decimal
```

---

## 11. Triângulos

Três lados formam um triângulo quando:

```text
lado1 + lado2 > lado3
lado1 + lado3 > lado2
lado2 + lado3 > lado1
```

Classificação:

```text
3 iguais       -> equilátero
2 iguais       -> isósceles
3 diferentes   -> escaleno
```

---

## 12. Combustíveis

### Etanol

```text
Preço: R$ 1,70/L
até 15 L    -> 2% de desconto
acima 15 L  -> 4% de desconto
```

### Diesel

```text
Preço: R$ 2,00/L
até 15 L    -> 3% de desconto
acima 15 L  -> 5% de desconto
```

Cálculos:

```text
valor bruto = preço × litros
desconto = preço × litros × percentual
valor final = valor bruto - desconto
```

---

## 13. Variação percentual

Primeiro:

```text
diferença = vendas_2023 - vendas_2022
```

Depois:

```text
variação = diferença / vendas_2022 × 100
```

Decisões:

| Variação | Ação |
|---|---|
| acima de 20% | bonificação |
| entre 2% e 20% | pequena bonificação |
| entre -10% e 2% | políticas de incentivo |
| abaixo de -10% | corte de gastos |

---

# Como pensar antes de programar

Antes de escrever código:

1. Quais são as entradas?
2. O que precisa ser processado?
3. Quais decisões existem?
4. Qual deve ser a saída?

Fluxo:

```text
ENTRADA
   ↓
PROCESSAMENTO
   ↓
DECISÃO
   ↓
SAÍDA
```

Exemplo:

```text
"Macarrão precisa ser menor que trigo
E menor que arroz."
```

Transformando em Python:

```python
macarrao < trigo and macarrao < arroz
```

---

# Estratégia de estudo

Para cada exercício:

1. Leia o problema sem escrever código.
2. Liste as entradas.
3. Liste os casos possíveis.
4. Escreva as condições em português.
5. Transforme as condições em Python.
6. Teste casos normais.
7. Teste empates e valores limite.
8. Só depois tente simplificar o código.

---

# Checklist

- [ ] Recebi todos os valores necessários?
- [ ] Converti os valores para o tipo correto?
- [ ] Considerei todos os casos?
- [ ] Existe possibilidade de empate?
- [ ] Os limites das condições estão corretos?
- [ ] O `and` está comparando os dois lados?
- [ ] Testei valores diferentes?
- [ ] Testei valores iguais?
- [ ] A mensagem final está clara?

---

# Objetivo desta etapa

A ideia principal é aprender a transformar um problema em:

```text
dados
↓
comparações
↓
decisões
↓
resultado
```

Depois que essa lógica estiver clara, recursos como listas, dicionários, `min()`, `max()` e `sorted()` passam a servir para **simplificar um algoritmo que você já entende**.
