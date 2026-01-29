def caching_fibonacci():
    cache = {}

# Створення внутріщньої функції дял обчислення ряду Фібоначчі
    def fibonacci(n):
        # Умови
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Перевірка кешу
        elif n in cache:
            return cache[n]

        # Рекурсія
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))
