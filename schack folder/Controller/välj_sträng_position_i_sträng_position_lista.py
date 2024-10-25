def välj_sträng_position_i_sträng_position_lista(sträng_position_lista):
        vald_sträng_position=input()
        try:
            if len(vald_sträng_position)==2:
                if vald_sträng_position in sträng_position_lista:
                    return(sträng_position_lista[sträng_position_lista.index(vald_sträng_position)])
                else:
                    print(f'Strängen du skrev in finns inte med i listan av alternativ')
            else:
                print(f'Strängen du skriver in ska vara 2 karaktärer lång')
        except:
           print("Fanns inget sådant drag att välja")
        

    
