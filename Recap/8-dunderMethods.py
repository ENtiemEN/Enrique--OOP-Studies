''' Módulo 8: Métodos Especiales (Dunder Methods) y Sobrecarga de Operadores

-> Los métodos con doble guion bajo ('double underscore o *dunder*') permiten integrar tus clases directamente con la sintaxis nativa de Python.
En lugar de inventar métodos como `sumar()`, `imprimir()` o `longitud()`, implementas los dunder corespondientes y Python los llama automáticamente cuando usas operadores o funciones integradas:

- `__str__` --> Representación legible e informal pensada para el usuario final (`print(obj)` o `str(obj)`)

- `__repr__` --> Representación inequívoca y formal orientada al desarrollador o depuración (`repr(obj)` o en la consola interactiva). Lo ideal es que parezca el código exacto necesario para recrear el objeto

- `__len__` --> Define el comportamiento al pasar el objeto a la función `len(obj)`. Debe retornar un entero no negativo

- Sobrecarga de operadores (`__add__`, `__eq__`, etc.) --> Permite que tus objetos interactúen con operadores como `+`, `==`, `<`, etc.
'''

class CarritoCompras:
    def __init__(self, cliente: str):
        self.cliente = cliente
        # type(tuple([str, float])) -> <class 'tuple'>
        # type(tuple[str, float]) -> <class 'types.GenericAlias'>
        self.items: list[tuple[str, float]] = []
        # [(str, float), (str, float), ..., (str, float)]

    def agregar(self, item: str, precio: float) -> None:
        self.items.append((item, precio))

    # 1. Función len():
    def __len__(self) -> int:
        return len(self.items)

    # 2. Representación para depuración: repr(carrito)
    def __repr__(self) -> str:
        return f"CarritoCompras(cliente='{self.cliente}')"

    # 3. Representación legible: print(carrito)
    def __str__(self) -> str:
        total = sum(precio for _, precio in self.items)
        return f"Carrito de {self.cliente} ({len(self)} artículos) - Total: ${total}"

    # 4. Sobrecarga de suma (+): carrito1 + carrito2
    