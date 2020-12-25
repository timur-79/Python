import numpy as np

x = np.random.rand() * 100
type(x)
if x > 85:
    print('Pass')
else:
    print('No pasaran')
A=(10, 2, -17, 2, -43, 11, 22.5)
for num in A:
    if num % 2 == 0:
        print('Четное ', num)
    elif num % 2 == 1:
        print('Нечетное ', num)
    else:
        print('Чо за нах?')

