# TODO Найдите количество книг, которое можно разместить на дискете

disketa_mb = 1.44 # Мб
stranizi = 100
stroki = 50
simvoli = 25
ves_simvola = 4 # б

disketa_b = disketa_mb * 1024 * 1024 # перевод из Мб в б

kniga = stranizi * stroki * simvoli * ves_simvola # вес 1 книги

vsego_knig = disketa_b // kniga

print("Количество книг, помещающихся на дискету:", int(vsego_knig))
