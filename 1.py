#Создание музыкального фрагмента с помощью генерации различных синусоид
append_sinewave(freq=160.0, milliseconds = 700, volume = 0.3)
append_sinewave(freq=160.0, milliseconds = 700, volume = 0.5)
append_sinewave(freq=160.0, milliseconds = 700, volume = 0.7)
append_sinewave(freq=160.0, milliseconds = 700, volume = 1)

for _ in range(2):
    append_sinewave(freq=300.0, milliseconds = 400, volume= 1)
    append_voidwave(duration_milliseconds = 100)
    append_sinewave(freq=400.0, milliseconds = 400, volume= 1)
    append_voidwave(duration_milliseconds = 100)
    append_sinewave(freq=500.0, milliseconds = 400, volume= 1)
    append_voidwave(duration_milliseconds = 200)


    append_sinewave(freq=500.0, milliseconds = 400, volume= 1)
    append_voidwave(duration_milliseconds = 100)
    append_sinewave(freq=400.0, milliseconds = 400, volume= 1)
    append_voidwave(duration_milliseconds = 100)
    append_sinewave(freq=300.0, milliseconds = 400, volume= 1)
    append_voidwave(duration_milliseconds = 200)
    
    
append_sinewave(freq=350.0, milliseconds = 2000, volume= 1)
for _ in range(8):
    append_sinewave(freq=500.0, milliseconds = 300, volume= 1)
    append_voidwave(duration_milliseconds = 50)
for _ in range(8):
    append_sinewave(freq=350.0, milliseconds = 300, volume= 1)
    append_voidwave(duration_milliseconds = 50)
for _ in range(8):
    append_sinewave(freq=500.0, milliseconds = 300, volume= 1)
    append_voidwave(duration_milliseconds = 50)
for _ in range(8):
    append_sinewave(freq=350.0, milliseconds = 300, volume= 1)
    append_voidwave(duration_milliseconds = 50)
for i in range(300):
    append_sinewave(freq=350.0, milliseconds = 10, volume= 1 - i/299.0)
    append_voidwave(duration_milliseconds = 5)

save_wav("output.wav") # Сохранение wav файла
