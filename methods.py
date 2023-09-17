def handler_repeat(dic):
    for v in dic.values():
        if v > 1:
            return True
    return False

def productos_medios(sem1, sem2, iteraciones):
    centros = {}
    nums_al = []
    lon_semilla = len(str(sem1))
    for i in range(iteraciones):
        product = sem1 * sem2
        str_product = str(product)
        str_cor = "0" + str_product if len(str_product) % 2 != 0 else str_product
        n = int((len(str_cor) - lon_semilla) / 2)
        new_n = int(str_cor[n:n + lon_semilla])
        centro = str_cor[n:n+lon_semilla]
        if centro in centros:
            centros[centro]+=1
        else:
            centros[centro]=1

        if handler_repeat(centros):
            centro="*"+centro
        
        nums_al.append([i+1,sem1,sem2,product, len(str_product),centro, new_n / (10 ** len(centro))])
        sem1 = sem2
        sem2 = new_n
    return nums_al

def cuadrados_medios(sem1, iteraciones):
    centros = {}
    nums_al = []
    lon_semilla = len(str(sem1))
    for i in range(iteraciones):
        product = sem1 * sem1
        str_product = str(product)
        str_cor = "0" + str_product if len(str_product) % 2 != 0 else str_product
        n = int((len(str_cor) - lon_semilla) / 2)
        new_n = int(str_cor[n:n + lon_semilla])
        
        centro = str_cor[n:n + lon_semilla]
        if centro in centros:
            centros[centro]+=1
        else:
            centros[centro]=1

        if handler_repeat(centros):
            centro="*"+centro
        
        nums_al.append([i+1,sem1,product, len(str_product),centro, new_n / (10 ** len(centro))])
        sem1 = new_n
    return nums_al