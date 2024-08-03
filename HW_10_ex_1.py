import pulp 

# Створення моделі 
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
Limonade = pulp.LpVariable('Limonade', lowBound=0, cat='Integer')  # Кількість виробленого Лимонаду
FruitJuice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')  # Кількість виробленого Фруктового соку

# Обмеження ресурсів
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Витрати ресурсів на одиницю продукції
water_for_limonade = 2
sugar_for_limonade = 1
lemon_juice_for_limonade = 1

water_for_fruit_juice = 1
fruit_puree_for_fruit_juice = 2

# Додавання обмежень
model += (water_for_limonade * Limonade + water_for_fruit_juice * FruitJuice <= water_limit), "Water_Limit"
model += (sugar_for_limonade * Limonade <= sugar_limit), "Sugar_Limit"
model += (lemon_juice_for_limonade * Limonade <= lemon_juice_limit), "Lemon_Juice_Limit"
model += (fruit_puree_for_fruit_juice * FruitJuice <= fruit_puree_limit), "Fruit_Puree_Limit"

# Функція цілі (максимізація загальної кількості продукції)
model += Limonade + FruitJuice, "Total_Production"

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Оптимальна кількість виробленого Лимонаду: {pulp.value(Limonade)}")
print(f"Оптимальна кількість виробленого Фруктового соку: {pulp.value(FruitJuice)}")
print(f"Максимальна загальна кількість продукції: {pulp.value(model.objective)}")
