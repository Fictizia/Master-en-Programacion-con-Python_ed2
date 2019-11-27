class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
      
    def __repr__(self):
        return f'Los lados son {self.a} {self.b} {self.c}'    
    
    def __enter__(self):
        return self.a + self.b + self.c

    def __exit__(self, err_type, err_value, traceback):
        self.a, self.b = self.b, self.a

    def __eq__(self, other_triangle):
        first =  self.a == other_triangle.a 
        second = self.b == other_triangle.b
        third =  self.c == other_triangle.c

        return first == second == third == True
            
    



primer_triangulo = Triangulo(1,2,3)
segundo_triangulo = Triangulo(1,2,3)

print(primer_triangulo)
print(segundo_triangulo)
print(primer_triangulo == segundo_triangulo)
print(primer_triangulo is segundo_triangulo)
