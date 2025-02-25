import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування 
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для обчислення інтеграла
N = 100000  # Кількість випадкових точок
random_x = np.random.uniform(a, b, N)
random_y = np.random.uniform(0, f(b), N)

# Точки, які лежать під кривою
points_under_curve = random_y < f(random_x)
integral_monte_carlo = (b - a) * f(b) * np.sum(points_under_curve) / N

print(f"Інтеграл (метод Монте-Карло): {integral_monte_carlo}")

# Перевірка за допомогою scipy.integrate.quad
result, error = spi.quad(f, a, b)
print(f"Інтеграл (SciPy quad): {result}")

