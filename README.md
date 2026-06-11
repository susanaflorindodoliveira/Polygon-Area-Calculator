# Polygon Area Calculator 📐

Uma calculadora geométrica desenvolvida em Python que utiliza conceitos fundamentais de **Programação Orientada a Objetos (POO)**, como herança e polimorfismo, para manipular propriedades de retângulos e quadrados.

Este projeto faz parte da certificação de **Scientific Computing with Python** do freeCodeCamp.

![Estado do Projeto](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Linguagem](https://img.shields.io/badge/Linguagem-Python%203-blue)

---

## 🚀 Funcionalidades

- **Cálculos Geométricos:** Calcula automaticamente a área, o perímetro e a diagonal de retângulos e quadrados.
- **Representação Visual:** Gera uma representação em formato de texto (usando caracteres `*`) da forma geométrica com base nas suas dimensões (até um limite de 50 unidades).
- **Herança (`Square` herda de `Rectangle`):** A classe `Square` reutiliza a lógica da classe `Rectangle`, mas garante que os lados (largura e altura) permanecem sempre iguais ao modificar as suas dimensões.
- **Cálculo de Encaixe (`get_amount_inside`):** Determina quantas vezes uma determinada forma geométrica consegue caber dentro de outra (sem rotações).

---

## 🛠️ Métodos Disponíveis

### Classe `Rectangle`
* `set_width(width)` / `set_height(height)`: Define as dimensões do retângulo.
* `get_area()`: Retorna a área ($largura \times altura$).
* `get_perimeter()`: Retorna o perímetro ($2 \times largura + 2 \times altura$).
* `get_diagonal()`: Retorna a linha diagonal da forma.
* `get_picture()`: Retorna uma string que representa a forma com asteriscos.
* `get_amount_inside(shape)`: Retorna o número de vezes que a forma passada como argumento cabe dentro do retângulo atual.

### Classe `Square`
* Herda todos os métodos de `Rectangle`.
* `set_side(side)`: Define o tamanho do lado (alterando simultaneamente a largura e a altura).

---

## 💻 Exemplo de Uso

```python
# Criar um retângulo
rect = Rectangle(10, 5)
print(rect.get_area())        # Saída: 50
print(rect.get_perimeter())   # Saída: 30
print(rect)                   # Saída: Rectangle(width=10, height=5)
print(rect.get_picture())

# Criar um quadrado
sq = Square(5)
print(sq.get_area())          # Saída: 25
sq.set_side(3)
print(sq.get_diagonal())      # Saída: 4.242640687119285
print(sq)                     # Saída: Square(side=3)

# Verificar encaixe
rect.set_width(15)
rect.set_height(10)
print(rect.get_amount_inside(sq)) # Saída: 15
Exemplo de Saída da Imagem (get_picture()):
Plaintext
**********
**********
**********
**********
**********
⚙️ Como executar localmente
Faz o clone deste repositório:

Bash
git clone [https://github.com/susanaflorindodoliveira/polygon-area-calculator.git](https://github.com/susanaflorindodoliveira/polygon-area-calculator.git)
Navega até à pasta do projeto:

Bash
cd polygon-area-calculator
Executa o script principal utilizando o Python:

Bash
python main.py
👨‍💻 Autor
Desenvolvido por Susana Florindo de Oliveira.
