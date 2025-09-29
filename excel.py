import pandas as pd
import os



excel = pd.read_excel("horas de trabajo.xlsx")


def iterar_excel(excel):
   
    hora = 161.97
    extra_1200 = 0
    hora_1202 = 0
    doble_1203 = 0 
    
    for index, row in excel.iterrows():
        if row["codigo"] == 1203:
            doble_1203 += row["hora extra"]
        elif row["codigo"] == 1200:
            extra_1200 += row["hora extra"]
        elif row["codigo"] == 1202:
            hora_1202 += row["hora extra"]  
    return hora, extra_1200, hora_1202, doble_1203 
            
def generar(hora,extra_1200,hora_1202,doble_1203,salario_base):
    
    h_135 = hora*1.35*extra_1200
    h_200 = hora*2*hora_1202
    h_270 = hora*2.7*doble_1203
    
    print("----------Salario------------".center(40))
    print(f"Su salario es: {h_135+h_200+h_270+salario_base}" )
    
            
def inicio():
    print("--------------Menu inicio-------------------".center(40))
    
    salario = int(input("Ingrese salario base: "))/ 2

    
    input("Leyendo excel>>>>")
    
    return salario
    
os.system("cls")  
deb = inicio()  
hora, extra_1200, hora_1202, doble_1203 = iterar_excel(excel) 
generar(hora, extra_1200, hora_1202, doble_1203, deb)
 
            
          
            
        

        
        
        

        




        
        
        


