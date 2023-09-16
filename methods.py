def handler_repeat(dic,n):
    for v in dic.values():
        if v > 1:
            return True
    return False

def productos_medios(sem1, sem2, iteraciones):
    centros = {}
    nums_al = []
    lon_semilla = len(str(sem1))
    repeat_flag = False
    for i in range(iteraciones):
        product = sem1 * sem2
        str_n = str(product)
        str_cor = "0" + str_n if len(str_n) % 2 != 0 else str_n
        n = int((len(str_cor) - lon_semilla) / 2)
        new_n = int(str_cor[n:n + 4])
        centro = str_cor[2:6]
        if centro in centros:
            centros[centro]+=1
        else:
            centros[centro]=1

        if handler_repeat(centros,centro):
            centro="-"+centro
        
        nums_al.append([i+1,sem1,sem2,product, len(str_n),centro, new_n / 10000])
        sem1 = sem2
        sem2 = new_n
    return nums_al

def cuadrados_medios(sem1, iteraciones):
    centros = {}
    nums_al = []
    lon_semilla = len(str(sem1))
    for i in range(iteraciones):
        product = sem1 * sem1
        str_n = str(product)
        str_cor = "0" + str_n if len(str_n) % 2 != 0 else str_n
        n = int((len(str_cor) - lon_semilla) / 2)
        new_n = int(str_cor[n:n + 4])
        
        centro = str_cor[2:6]
        if centro in centros:
            centros[centro]+=1
        else:
            centros[centro]=1

        if handler_repeat(centros,centro):
            centro="-"+centro
        
        nums_al.append([i+1,sem1,product, len(str_n),centro, new_n / 10000])
        sem1 = new_n
    return nums_al