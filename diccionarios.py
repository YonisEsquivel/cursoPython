def run():
    # mi_diccionario = {
    #     "llave1" : 1,
    #     "llave2" : 2,
    #     "llave3" : 3
    #  }

    # print(mi_diccionario)

    poblacion_paises = {
        "Argentina" : 44000000,
        "Colombia" : 50000000,
        "Brasil" : 300000000
    }

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")
        print(f"{pais} tiene {poblacion} abitantes")


if __name__ == "__main__":
    run()