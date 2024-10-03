# Jogo de Movimentação em Python

Este projeto é um pequeno jogo de movimentação no console, onde o jogador controla um cavaleiro representado pelo emoji "🏇" em uma área de jogo composta por blocos verdes "🟩". O jogador pode se mover para cima, baixo, esquerda ou direita usando as teclas `w`, `s`, `d` e `a`.

## Funcionalidades

- **Movimentação do jogador:** O jogador pode se mover em quatro direções no grid (cima, baixo, esquerda e direita).
- **Área de jogo:** O campo de jogo é um grid de 5 linhas por 10 colunas, onde o cavaleiro "🏇" se move.
- **Interface visual simples:** O jogo é exibido no console, mostrando o cavaleiro no meio de blocos verdes.
- **Limpeza da tela:** A tela é atualizada a cada movimento, criando uma experiência de jogo contínua.

## Controles

- **`w`**: Mover para cima.
- **`s`**: Mover para baixo.
- **`d`**: Mover para a direita.
- **`a`**: Mover para a esquerda.

## Requisitos

- **Sistema Operacional:** O comando `os.system('cls')` é utilizado para limpar o console, sendo compatível com Windows. Para outros sistemas operacionais (Linux/macOS), é necessário substituir por `os.system('clear')`.
- **Python 3.x** instalado.

## Como Jogar

1. Execute o script:

    ```bash
    python main.py
    ```

2. O cavaleiro "🏇" será exibido no campo de jogo composto de blocos verdes "🟩".
   
3. Use as teclas `w`, `a`, `s`, `d` para mover o cavaleiro pelo grid:

    - `w`: Move o cavaleiro para cima.
    - `s`: Move o cavaleiro para baixo.
    - `d`: Move o cavaleiro para a direita.
    - `a`: Move o cavaleiro para a esquerda.

4. A tela será limpa e atualizada a cada movimento.

## Personalização

- **Tamanho do campo de jogo:** Você pode ajustar o tamanho do grid modificando os valores de `range(5)` para as linhas e `range(10)` para as colunas na parte que desenha o campo de jogo.
- **Comando de limpeza da tela:** Para sistemas operacionais que não sejam Windows, altere a linha:

    ```python
    os.system('cls')
    ```

    Para:

    ```python
    os.system('clear')
    ```

## Exemplo de Uso

Ao rodar o jogo, a saída será algo semelhante a:


Aqui está o README formatado em markdown:

markdown
Copiar código
# Jogo de Movimentação em Python

Este projeto é um pequeno jogo de movimentação no console, onde o jogador controla um cavaleiro representado pelo emoji "🏇" em uma área de jogo composta por blocos verdes "🟩". O jogador pode se mover para cima, baixo, esquerda ou direita usando as teclas `w`, `s`, `d` e `a`.

## Funcionalidades

- **Movimentação do jogador:** O jogador pode se mover em quatro direções no grid (cima, baixo, esquerda e direita).
- **Área de jogo:** O campo de jogo é um grid de 5 linhas por 10 colunas, onde o cavaleiro "🏇" se move.
- **Interface visual simples:** O jogo é exibido no console, mostrando o cavaleiro no meio de blocos verdes.
- **Limpeza da tela:** A tela é atualizada a cada movimento, criando uma experiência de jogo contínua.

## Controles

- **`w`**: Mover para cima.
- **`s`**: Mover para baixo.
- **`d`**: Mover para a direita.
- **`a`**: Mover para a esquerda.

## Requisitos

- **Sistema Operacional:** O comando `os.system('cls')` é utilizado para limpar o console, sendo compatível com Windows. Para outros sistemas operacionais (Linux/macOS), é necessário substituir por `os.system('clear')`.
- **Python 3.x** instalado.

## Como Jogar

1. Execute o script:

    ```bash
    python main.py
    ```

2. O cavaleiro "🏇" será exibido no campo de jogo composto de blocos verdes "🟩".
   
3. Use as teclas `w`, `a`, `s`, `d` para mover o cavaleiro pelo grid:

    - `w`: Move o cavaleiro para cima.
    - `s`: Move o cavaleiro para baixo.
    - `d`: Move o cavaleiro para a direita.
    - `a`: Move o cavaleiro para a esquerda.

4. A tela será limpa e atualizada a cada movimento.

## Personalização

- **Tamanho do campo de jogo:** Você pode ajustar o tamanho do grid modificando os valores de `range(5)` para as linhas e `range(10)` para as colunas na parte que desenha o campo de jogo.
- **Comando de limpeza da tela:** Para sistemas operacionais que não sejam Windows, altere a linha:

    ```python
    os.system('cls')
    ```

    Para:

    ```python
    os.system('clear')
    ```

## Exemplo de Uso

Ao rodar o jogo, a saída será algo semelhante a:
```python
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
Próxima direção (w,s,d,a):
```
O cavaleiro "🏇" se moverá de acordo com a entrada do jogador.
