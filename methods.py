def productos_medios(sem1, sem2, iteraciones):
    nums_al = []
    lon_semilla = len(str(sem1))
    for i in range(iteraciones):
        product = sem1 * sem2
        str_n = str(product)
        str_cor = "0" + str_n if len(str_n) % 2 != 0 else str_n
        n = int((len(str_cor) - lon_semilla) / 2)
        new_n = int(str_cor[n:n + 4])
        nums_al.append([i+1,sem1,sem2,product, len(str_n),str_cor[2:6], new_n / 10000])
        sem1 = sem2
        sem2 = new_n
    return nums_al