class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        # Cria uma linha de '*' multiplicada pela largura, adiciona \n, e multiplica pela altura
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        # Utiliza a divisão inteira (//) para ver quantas vezes a forma cabe sem rotações
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # Chama o __init__ da classe pai (Rectangle) passando o lado como largura e altura
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        # Na classe Square, alterar a largura também altera a altura
        self.set_side(width)

    def set_height(self, height):
        # Na classe Square, alterar a altura também altera a largura
        self.set_side(height)

    def __str__(self):
        # Na classe Square a largura e altura são sempre iguais ao side
        return f"Square(side={self.width})"
