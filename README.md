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

