print'NumberPhone-Generator v.2.1----------- Creado por R4nd0mByt3'
def Fun1():
    lada1=raw_input("ingrese la lada principal: ")
    lada2=raw_input("ingrese la lada secundaria: ")
    numero=int(0000)
    print 'la lada principal es: ',lada1,' y la lada secundaria es: ',lada2
    decision=raw_input("presione Y si desea continuar, o presione N para corregir: ").upper()
    if (decision=='Y'):
        print("generando diccionario, porfavor espere....")
        while(numero<=9999):
            archivo=open("diccionario.txt",'a')
            archivo.write(lada1)
            archivo.write(lada2)
            num2=str(numero)
            if (len(num2)<2):                
                num2='000'+num2
            elif (len(num2)<3):                
                num2='00'+num2
            elif (len(num2)<4):                
                num2='0'+num2
            archivo.write(num2)
            archivo.write("\n")
            numero+=1
    elif(decision=='N'):
            Fun1()
    else:
        print("caracter no valido, cerrando proceso..")
        exit
Fun1()
