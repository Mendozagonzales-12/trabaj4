#PROGRAMA1_CALCULAR LA SUMA TOTAL DE VENTAS DEL 2013 DE LOS PRIMEROS 6 MESES
#DECLARACION
ventas_enero2013, ventas_febrero2013, ventas_marzo2013, ventas_abril2013, ventas_mayo2013, ventas_junio2013=0.0,0.0,0.0,0.0,0.0,0.0
total_ventas2013=0.0

#INPUT
ventas_enero2013=float(input("Ingrese el total de ventas del mes de enero: "))
ventas_febrero2013=float(input("Ingrese el total de ventas del mes de febrero: "))
ventas_marzo2013=float(input("Ingrese el total de ventas del mes de marzo: "))
ventas_abril2013=float(input("Ingrese el total de ventas del mes de abril:"))
ventas_mayo2013=float(input("Ingrese el total de ventas del mes de mayo:"))
ventas_junio2013=float(input("Ingrese el total de ventas del mes de abril:"))

#PROCESSING
total_ventas2013=ventas_enero2013+ventas_febrero2013+ventas_marzo2013+ventas_abril2013+ventas_mayo2013+ventas_junio2013

#OUTPUT
print("#######################################")
print("#       BOLETA VENTAS 2013   #")
print("#######################################")
print("# ventas_enero2013: ",ventas_enero2013," #")
print("# ventas_febrero2013: ",ventas_febrero2013," #")
print("# ventas_marzo2013: ",ventas_marzo2013," #")
print("# ventas_abril2013: ",ventas_abril2013," #")
print("# ventas_mayo2013: ",ventas_mayo2013," #")
print("# ventas_junio2013:",ventas_junio2013," #")
print("#total_ventas2013:",total_ventas2013," #")
print("#######################################")


#PROGRAMA2_CALCULAR LA SUMA TOTAL DE VENTAS NETAS
#DECLARACION
venetas2005,venetas2006,venetas2007,venetas2008,venetas2009,venetas2010=0,0,0,0,0,0
total_venetas=0

#INPUT
venetas2005=int(input("Ingrese el total de ventas netas del año 2005: "))
venetas2006=int(input("Ingrese el total de ventas netas del año 2006: "))
venetas2007=int(input("Ingrese el total de ventas netas del año 2007: "))
venetas2008=int(input("Ingrese el total de ventas netas del año 2008: "))
venetas2009=int(input("Ingrese el total de ventas netas del año 2009: "))
venetas2010=int(input("Ingrese el total de ventas netas del año 2010: "))

#PROCESSING
total_venetas=venetas2005+venetas2006+venetas2007+venetas2008+venetas2009+venetas2010


#OUTPUT
print("#######################################")
print("#       BOLETA VENTAS DE 5AÑOS  #")
print("#######################################")
print("# venetas2005: ",venetas2005," #")
print("# venetas2006: ",venetas2006," #")
print("# venetas2007: ",venetas2007," #")
print("# venetas2008: ",venetas2008," #")
print("# venetas2009: ",venetas2009," #")
print("# venetas2010: ",venetas2010," #")
print("#total_venetas: ",total_venetas," #")
print("#######################################")


#PROGRAMA3_CALCULAR LA SUMA TOTAL DEl COSTO DE VENTAS
#DECLARACION
costoven2005,costoven2006,costoven2007,costoven2008,costoven2009,costoven2010=0,0,0,0,0,0
total_costoven=0

#INPUT
costoven2005=int(input("Ingrese el total de costos del año 2005"))
costoven2006=int(input("Ingrese el total de costos del año 2006"))
costoven2007=int(input("Ingrese el total de costos del año 2007"))
costoven2008=int(input("Ingrese el total de costos del año 2008"))
costoven2009=int(input("Ingrese el total de costos del año 2009"))
costoven2010=int(input("Ingrese el total de costos del año 2010"))

#PROCESSING
total_costoven=costoven2005+costoven2006+costoven2007+costoven2008+costoven2009+costoven2010

#OUTPUT
print("#######################################")
print("#       BOLETA DE COSTOS DE VENTAS DE 5AÑOS  #")
print("#######################################")
print("# costoven2005: ",costoven2005," #")
print("# costoven2006: ",costoven2006," #")
print("# costoven2007: ",costoven2007," #")
print("# costoven2008: ",costoven2008," #")
print("# costoven2009: ",costoven2009," #")
print("# costoven2010: ",costoven2010," #")
print("# total_costoven: ",total_costoven," #")
print("#######################################")


#PROGRAMA4_CALCULAR EL TOTAL DE LAS ESPECIES EN RIESGO
#DECLARACION
anfibios_riesgo,coniferas_riesgo,corales_riesgo,tiburones_riego,crustaceos_riesgo,mamiferos_riesgo,aves_riesgo=0,0,0,0,0,0,0
sumatotal=0

#INPUT
anfibios_riesgo=int(input("Ingrese el total de anfibios en peligro de riesgo: "))
coniferas_riesgo=int(input("Ingrese el total de coniferas en peligro de riesgo: "))
corales_riesgo=int(input("Ingrese el total de corales en peligro de riesgo: "))
tiburones_riego=int(input("Ingrese el total de tiburones en peligro de riesgo: "))
crustaceos_riesgo=int(input("Ingrese el total de crustaceos en peligro de riesgo: "))
mamiferos_riesgo=int(input("Ingrese el total de mamiferos en peligro de riesgo: "))
aves_riesgo=int(input("Ingrese el total de aves en peligro de riesgo: "))

#PROCESSING
sumatotal=anfibios_riesgo+coniferas_riesgo+corales_riesgo+tiburones_riego+crustaceos_riesgo+mamiferos_riesgo+aves_riesgo

#OUTPUT
print("#######################################")
print("#       ESPECIES EN RIESGO    #")
print("#######################################")
print("# anfibios_riesgo: ",anfibios_riesgo," #")
print("# coniferas_riesgo: ",coniferas_riesgo," #")
print("# corales_riesgo: ",corales_riesgo," #")
print("# tiburones_riesgo: ",tiburones_riego," #")
print("# crustaceos_riesg: ",crustaceos_riesgo," #")
print("# mamiferos_riesgo: ",mamiferos_riesgo," #")
print("# aves_riesgo: ",aves_riesgo," #")
print("# sumatotal: ",sumatotal," #")
print("#######################################")


#PROGRAMA5_CALCULAR EL PORCENTAJE TOTAL DEL MARGEN DE FLUJO
#DECLARACION
margenflujo2005,margenflujo2006,margenflujo2007,margenflujo2008,margenflujo2009,margenflujo2010=0.0,0.0,0.0,0.0,0.0,0.0
porcentajetotal1=0.0

#INPUT
margenflujo2005=float(input("Ingrese el margen de flujo del año 2005: "))
margenflujo2006=float(input("Ingrese el margen de flujo del año 2006: "))
margenflujo2007=float(input("Ingrese el margen de flujo del año 2007: "))
margenflujo2008=float(input("Ingrese el margen de flujo del año 2008: "))
margenflujo2009=float(input("Ingrese el margen de flujo del año 2009: "))
margenflujo2010=float(input("Ingrese el margen de flujo del año 2010: "))

#PROCESSING
porcentajetotal1=(margenflujo2005+margenflujo2006+margenflujo2007+margenflujo2008+margenflujo2009+margenflujo2010)*100

#OUTPUT
print("#######################################")
print("#       MARGEN DE FLUJO DE LOS 5AÑOS   #")
print("#######################################")
print("# margen de fujo 2005: ",margenflujo2005," #")
print("# margen de fujo 2006: ",margenflujo2006," #")
print("# margen de fujo 2007: ",margenflujo2007," #")
print("# margen de fujo 2008: ",margenflujo2008," #")
print("# margen de fujo 2009: ",margenflujo2009," #")
print("# margen de fujo 2010: ",margenflujo2010," #")
print("# porcentajetotall: ",porcentajetotal1," #")
print("#######################################")


#PROGRAMA6_CALCULAR EL PORCENTAJE TOTAL DEL MARGEN DE OPERACION
#DECLARACION
margenope2005,margenope2006,margenope2007,margenope2008,margenope2009,margenope2010=0.0,0.0,0.0,0.0,0.0,0.0
porcentajetotal2=0.0

#INPUT
margenope2005=float(input("Ingrese el margen de operacion del año 2005: "))
margenope2006=float(input("Ingrese el margen de operacion del año 2006: "))
margenope2007=float(input("Ingrese el margen de operacion del año 2007: "))
margenope2008=float(input("Ingrese el margen de operacion del año 2008: "))
margenope2009=float(input("Ingrese el margen de operacion del año 2009: "))
margenope2010=float(input("Ingrese el margen de operacion del año 2010: "))

#PROCESSING
porcentajetotal2=(margenope2005+margenope2006+margenope2007+margenope2008+margenope2009+margenope2010)*100


#OUTPUT
print("#######################################")
print("#       MARGEN DE OPERACIONES DEL LOS 5 AÑOS    #")
print("#######################################")
print("# margenope2005: ",margenope2005," #")
print("# margenope2006: ",margenope2006," #")
print("# margenope2007: ",margenope2007," #")
print("# margenope2008: ",margenope2008," #")
print("# margenope2009: ",margenope2009," #")
print("# margenope2010: ",margenope2010," #")
print("# Porcentaje Total: ",porcentajetotal2," #")
print("#######################################")



#PROGRAMA7_CALCULAR EL TOTAL DE RESULTADOS DE OPERACION
#DECLARACION
resultadoper2005,resultadoper2006,resultadoper2007,resultadoper2008,resultadoper2009,resultadoper2010=0.0,0.0,0.0,0.0,0.0,0.0
total_resul=0.0

#INPUT
resultadoper2005=float(input("Ingrese los resultados totales de operaciones del año 2005: "))
resultadoper2006=float(input("Ingrese los resultados totales de operaciones del año 2006: "))
resultadoper2007=float(input("Ingrese los resultados totales de operaciones del año 2007: "))
resultadoper2008=float(input("Ingrese los resultados totales de operaciones del año 2008: "))
resultadoper2009=float(input("Ingrese los resultados totales de operaciones del año 2009: "))
resultadoper2010=float(input("Ingrese los resultados totales de operaciones del año 2010: "))

#PROCESSING
total_resul=resultadoper2005+resultadoper2006+resultadoper2007+resultadoper2008+resultadoper2009+resultadoper2010


#OUTPUT
print("#######################################")
print("#       RESULTADOS TOTALES DE OPERACIONES DEL LOS 5 AÑOS    #")
print("#######################################")
print("# resultadoper2005: ",resultadoper2005," #")
print("# resultadoper2006: ",resultadoper2006," #")
print("# resultadoper2007: ",resultadoper2007," #")
print("# resultadoper2008: ",resultadoper2008," #")
print("# resultadoper2009: ",resultadoper2009," #")
print("# resultadoper2010: ",resultadoper2010," #")
print("# Total de Resultados: ",total_resul," #")
print("#######################################")


#PROGRAMA8_CALCULAR EL TOTAL DE LA PARTICIPACION NO CONTROLADA
#DECLARACION
partnocontr2005,partnocontr2006,partnocontr2007,partnocontr2008,partnocontr2009,partnocontr2010=0,0,0,0,0,0
total_partno=0

#INPUT
partnocontr2005=int(input("Ingrese el total de participacion no controlada del año 2005: "))
partnocontr2006=int(input("Ingrese el total de participacion no controlada del año 2006: "))
partnocontr2007=int(input("Ingrese el total de participacion no controlada del año 2007: "))
partnocontr2008=int(input("Ingrese el total de participacion no controlada del año 2008: "))
partnocontr2009=int(input("Ingrese el total de participacion no controlada del año 2009: "))
partnocontr2010=int(input("Ingrese el total de participacion no controlada del año 2010: "))

#PROCESSING
total_partno=partnocontr2005+partnocontr2006+partnocontr2007+partnocontr2008+partnocontr2009+partnocontr2010

#OUTPUT
print("#######################################")
print("#      Participaciones No Controladas     #")
print("#######################################")
print("# partnocontr2005: ",partnocontr2005," #")
print("# partnocontr2006: ",partnocontr2006," #")
print("# partnocontr2007: ",partnocontr2007," #")
print("# partnocontr2008: ",partnocontr2008," #")
print("# partnocontr2009: ",partnocontr2009," #")
print("# partnocontr2010: ",partnocontr2010," #")
print("# Total de Participaciones: ",total_partno," #")
print("#######################################")


#PROGRAMA9_CALCULAR LA SUMA TOTAL DE DIVIDENDOS POR CPO
#DECLARACION
dividendosCPOs2005,dividendosCPOs2006,dividendosCPOs2007,dividendosCPOs2008,dividendosCPOs2009,dividendosCPOs2010=0.0,0.0,0.0,0.0,0.0,0.0
suma_dividendosCPO=0.0

#INPUT
dividendosCPOs2005=float(input("Ingreso total de dividendos por CPO en el año 2005: "))
dividendosCPOs2006=float(input("Ingreso total de dividendos por CPO en el año 2006: "))
dividendosCPOs2007=float(input("Ingreso total de dividendos por CPO en el año 2007: "))
dividendosCPOs2008=float(input("Ingreso total de dividendos por CPO en el año 2008: "))
dividendosCPOs2009=float(input("Ingreso total de dividendos por CPO en el año 2009: "))
dividendosCPOs2010=float(input("Ingreso total de dividendos por CPO en el año 2010: "))

#PROCESSING
suma_dividendosCPO=dividendosCPOs2005+dividendosCPOs2006+dividendosCPOs2007+dividendosCPOs2008+dividendosCPOs2009+dividendosCPOs2010

#OUTPUT
print("#######################################")
print("#     Dividendos por CPO en los 5 años     #")
print("#######################################")
print("# dividendosCPOs2005: ",dividendosCPOs2005," #")
print("# dividendosCPOs2006: ",dividendosCPOs2006," #")
print("# dividendosCPOs2007: ",dividendosCPOs2007," #")
print("# dividendosCPOs2008: ",dividendosCPOs2008," #")
print("# dividendosCPOs2009: ",dividendosCPOs2009," #")
print("# dividendosCPOs2010: ",dividendosCPOs2010," #")
print("# Total de dividendos: ",suma_dividendosCPO," #")
print("#######################################")


#PROGRAMA10_CALCULAR EL TOTAL DE LA UTILIDAD PERDIDA
#DECLARACION
utilidadCPOs2005,utilidadCPOs2006,utilidadCPOs2007,utilidadCPOs2008,utilidadCPOs2009,utilidadCPOs2010=0.0,0.0,0.0,0.0,0.0,0.0
suma_utilidadper=0.0

#INPUT
utilidadCPOs2005=float(input("Ingrese el total de utilidades por perdida del año 2005: "))
utilidadCPOs2006=float(input("Ingrese el total de utilidades por perdida del año 2006: "))
utilidadCPOs2007=float(input("Ingrese el total de utilidades por perdida del año 2007: "))
utilidadCPOs2008=float(input("Ingrese el total de utilidades por perdida del año 2008: "))
utilidadCPOs2009=float(input("Ingrese el total de utilidades por perdida del año 2009: "))
utilidadCPOs2010=float(input("Ingrese el total de utilidades por perdida del año 2010: "))

#PROCESSING
suma_utilidadper=utilidadCPOs2005+utilidadCPOs2006+utilidadCPOs2007+utilidadCPOs2008+utilidadCPOs2009+utilidadCPOs2010

#OUTPUT
print("#######################################")
print("#      UTILIDADES PERDIDAS EN LOS 5 AÑOS     #")
print("#######################################")
print("# utilidadCPOs2005: ",utilidadCPOs2005," #")
print("# utilidadCPOs2006: ",utilidadCPOs2006," #")
print("# utilidadCPOs2007: ",utilidadCPOs2007," #")
print("# utilidadCPOs2008: ",utilidadCPOs2008," #")
print("# utilidadCPOs2009: ",utilidadCPOs2009," #")
print("# utilidadCPOs2010: ",utilidadCPOs2010," #")
print("# Total de Utilidad P.: ",suma_utilidadper," #")
print("#######################################")
