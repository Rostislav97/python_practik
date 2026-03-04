def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y 

def c(x, y, z):
    total = x + y + z  
    square = b(total)**2
    return square


x = 1
y = x + 1
print(c(x, y+3, x+y))


""" ├── Глобальная область
│   ├── x = 1
│   ├── y = 2
│   └── print(c(1, 5, 3))
│
├── Вызов c: x=1, y=5, z=3
│   ├── total = 9
│   ├── square = b(9)**2
│   │
│   ├── Вызов b: z=9
│   │   ├── prod = a(9, 9)
│   │   │
│   │   ├── Вызов a: x=9, y=9
│   │   │   ├── x = 10 (после x+1)
│   │   │   └── return 90
│   │   │
│   │   ├── print(9, 90)
│   │   └── return 90
│   │
│   ├── square = 90**2 = 8100
│   └── return 8100
│
└── print(8100) """