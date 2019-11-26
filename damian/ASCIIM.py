#Programa1-calcular el promedio de deuda de un cliente
#Declaracion
deuda_bcp=0.0
deuda_bbva=0.0
deuda_cajas=0.0
deuda_otras=0.0
deuda_promedio=0.0

#Input
deuda_bcp=float(input("ingrese deuda_bcp:"))
deuda_bbva=float(input("ingrese deuda_bbva:"))
deuda_cajas=float(input("ingrese deuda_cajas:"))
deuda_otras=float(input("ingrese deuda_otras:"))

#Processing
deuda_promedio=((deuda_bcp+deuda_bbva+deuda_cajas+deuda_otras)/4)

#Output
print("#######################")
print("#       Infocorp      #")
print("#######################")
print("# deuda_bcp: ",deuda_bcp)
print("# deuda_bbva: ",deuda_bbva)
print("# deuda_cajas: ",deuda_cajas)
print("# deuda_otras: ",deuda_otras)
print("# deuda_promedio: ",deuda_promedio)


#Programa2-calcular importe prestamo
#Declaracion
importe_desembolsado=0.0
tasa_efectiva_anual=0.0
cuotas_año=0
periodo_pago=0
tasa_mensual=0.0
penalidad=0.0
dias_año=0
dias_mes=0
tna=0.0
tda=0.0
tda_ajustada_plazo=0.0

#Input
importe_desembolsado=float(input("ingrese importe_desembolsado"))
tasa_efectiva_anual=float(input("ingrese tasa_efectiva_anual:"))
cuotas_año=int(input("ingrese cuotas_año:"))
periodo_pago=int(input("ingrese periodo_pago:"))
tasa_mensual=float(input("ingrese tasa_mensual:"))
penalidad=float(input("ingrese penalidad:"))
dias_año=int(input("ingrese dias_año:"))
dias_mes=int(input("ingrese dias_mes:"))

#Processing
tna=(1+tasa_efectiva_anual**1/cuotas_año-1*cuotas_año*dias_año/360)
tda=(tasa_mensual*cuotas_año)
tda_ajustada_plazo=(tda/dias_año*dias_mes)

#Output
print("##########################")
print("#           BCP          #")
print("##########################")
print("# importe_desembolsado: ",importe_desembolsado)
print("# tasa_efectiva_anual: ",tasa_efectiva_anual)
print("# cuotas_año: ",cuotas_año)
print("# periodo_pago: ",periodo_pago)
print("# tasa_mensual: ",tasa_mensual)
print("# penalidad: ",penalidad)
print("# dias_año: ",dias_año)
print("# dias_mes: ",dias_mes)
print("# tna: ",tna)
print("# tda: ",tda)
print("# tda_ajustada_plazo: ",tda_ajustada_plazo)


#Programa3-calcular la cuota
monto=0.0
plazo=0
tasa_efectiva_mensual=0.0
comision=0.0
seguro_desgravamen=0.0
saldo_capital=0.0
tea=0.0
ted=0.0
suma_factores=0.0
cuota=0.0

#Input
monto=float(input("ingrese monto:"))
plazo=int(input("ingrese plazo"))
tasa_mensual=float(input("ingrese tasa_mensual"))
comision=float(input("ingrese comision:"))
seguro_desgravamen=float(input("ingrese seguro_desgravamen:"))
saldo_capital=float(input("ingrese saldo_capital:"))
suma_factores=float(input("ingrese suma_factores:"))

#Processing
tea=((1+tasa_mensual)**plazo-1)
ted=(1+tea)**0.0027-1
cuota=(saldo_capital+suma_factores)

#Output
print("############################")
print("#       Banco Ripley       #")
print("############################")
print("# monto: ",monto)
print("# plazo: ",plazo)
print("# tasa_efectiva_mensual: ",tasa_mensual)
print("# seguro_desgravamen: ",seguro_desgravamen)
print("# saldo_capital: ",saldo_capital)
print("# tea: ",tea)
print("# ted: ",ted)
print("# suma_factores: ",suma_factores)
print("# cuota:",cuota)


#Programa4-calcular el promedio de deuda de un cliente
#Declaracion
tasa_de_interes=0.0
capital_prestamo=0.0
plazo_num_cuotas=0
cuota=0.0

#Input
tasa_de_interes=float(input("ingrese tasa_de_interes:"))
capital_prestamo=float(input("ingrese capital_prestamo:"))
plazo_num_cuotas=int(input("ingrese plazo_num_cuotas:"))

#Processing
cuota=(capital_prestamo*(1+tasa_de_interes**plazo_num_cuotas*tasa_de_interes/(1+tasa_de_interes)**plazo_num_cuotas)-1)

#Output
print("###############################")
print("#      Caja municipal ica     #")
print("###############################")
print("# tasa_de_interes: ",tasa_de_interes)
print("# capital_prestamo: ",capital_prestamo)
print("# plaza_num_cuotas: ",plazo_num_cuotas)
print("# cuota: ",cuota)



#Programa5-calcular el producto bruto interno
#Declaracion
consumo=0.0
inversion_efectuada=0.0
gasto_publico=0.0
exportaciones=0.0
importaciones=0.0
producto_bruto_interno=0.0

#Input
consumo=float(input("ingrese consumo:"))
inversion_efectuada=float(input("ingrese inversion_efectuada:"))
gasto_publico=float(input("ingrese gasto_publico:"))
exportaciones=float(input("ingrese exportaciones:"))
importaciones=float(input("ingrese importaciones:"))

#Processing
producto_bruto_interno=(consumo+inversion_efectuada+gasto_publico+(exportaciones-importaciones))

#Output
print("#######################")
print("#       SENTINEL      #")
print("#######################")
print("# consumo: ",consumo)
print("# inversion_efectuada: ",inversion_efectuada)
print("# gasto_publico: ",gasto_publico)
print("# exportaciones: ",exportaciones)
print("# importaciones: ",importaciones)
print("# producto_bruto_interno: ",producto_bruto_interno)


#Programa6-calcular el importe de interes generado
#Declaracion
capital_inicial=0.0
tiempo=0
interes_simple=0.0
importe_interes_generado=0.0

#Input
capital_inicial=float(input("ingrese capital_inicial:"))
tiempo=str(input("ingrese tiempo:"))
interes_simple=float(input("ingrese interes_capital"))

#Processing
importe_interes_generado=(capital_inicial*interes_simple*tiempo)

#Output
print("#######################")
print("#       Infocorp      #")
print("#######################")
print("# capital_inicial: ",capital_inicial)
print("# tiempo: ",tiempo)
print("# interes_simple: ",interes_simple)
print("# importe_interes_generado: ",importe_interes_generado)


#Programa7-calcular el importe de interes diario
#Declaracion
saldo_final_dia=0.0
tasa_interes_ahorro=0.0
dias_base_anual=0
interes_diario=0.0

#Input
saldo_final_dia=float(input("ingrese saldo_final_dia:"))
tasa_interes_ahorro=float(input("ingrese tasa_interes_ahorr:"))
dias_base_anual=int(input("ingrese dias_base_anual:"))

#Processing
interes_diario=((saldo_final_dia*tasa_interes_ahorro)/dias_base_anual)

#Output
print("#################################")
print("#        Banco Interbank        #")
print("#################################")
print("# saldo_final_dia: ",saldo_final_dia)
print("# tasa_interes_ahorro: ",tasa_interes_ahorro)
print("# dias_base_anual: ",dias_base_anual)
print("# interes_diario: ",interes_diario)


#Programa8-calcular el mantenimiento de valor cuenta de ahorro
monto_principal=0.0
tipo_cambio_dia_anterior=0.0
cambio_dia_hoy=0.0
mantenimiento_valor_cuenta_de_ahorro=0.0

#Input
monto_principal=float(input("ingrese monto_principal:"))
tipo_cambio_dia_anterior=float(input("ingrese tipo_cambio_dia_anterior:"))
cambio_dia_hoy=float(input("ingrese cambio_dia_hoy:"))

#Processing
mantenimiento_valor_cuenta_de_ahorro=(monto_principal/tipo_cambio_dia_anterior*cambio_dia_hoy-monto_principal)

#Output
print("#######################")
print("#         BCR         #")
print("#######################")
print("# monto principal: ",monto_principal)
print("# tipo_cambio_dia_anterior: ",tipo_cambio_dia_anterior)
print("# cambio_dia_hoy: ",cambio_dia_hoy)
print("# mantenimiento_valor_cuenta_de_ahorro: ",mantenimiento_valor_cuenta_de_ahorro)


#Programa9-calcular el promedio de deuda de un cliente
#Declaracion
materia_prima_directa=0.0
materia_prima_comprada=0.0
materia_prima_disponible=0.0
materia_directa_final_disponible=0.0
materia_prima_utilizada=0.0
mano_obra=0.0
costo_indirecto=0.0
producto_proceso=0.0
produc_inicial=0.0
costo_produccion=0.0

#Input
materia_prima_directa=float(input("ingrese materia_prima_directa:"))
materia_prima_comprada=float(input("ingrese materia_prima_comprada:"))
materia_directa_final_disponible=float(input("ingrese materia_directa_final_disponible:"))
mano_obra=float(input("ingrese mano_obra;"))
costo_indirecto=float(input("ingrese costo_indirecto:"))
producto_proceso=float(input("ingrese producto_proceso:"))
produc_inicial=float(input("ingrese produc_inicial:"))

#Processing
materia_prima_disponible=(materia_prima_directa+materia_prima_comprada)
costo_produccion=(materia_prima_disponible+mano_obra+materia_prima_comprada-producto_proceso)

#Output
print("###############################")
print("#      Caja municipal ica     #")
print("###############################")
print("# materia_prima_directa: ",materia_prima_directa)
print("# materia_prima_comprada: ",materia_prima_comprada)
print("# materia_directa_final_disponible: ",materia_directa_final_disponible)
print("# mano_obra: ",mano_obra)
print("# materia_prima_disponible: ",materia_prima_disponible)
print("# materia_prima_utilizada: ",materia_prima_utilizada)
print("# costo_produccion: ",costo_produccion)


#Programa10-calcular el costo de venta
#Declaracion
existencia_inicial=0
costo_produccion=0.0
existencia_final=0
costo_venta=0.0

#Input
existencia_inicial=int(input("ingrese existencia_inicial:"))
costo_produccion=float(input("ingrese costo_produccion:"))
existencia_final=float(input("ingrese existencia_final:"))

#Processing
costo_venta=(existencia_inicial+costo_produccion-existencia_final)

#Output
print("#######################")
print("#      tienda         #")
print("#######################")
print("# existencia_inicial: ",existencia_inicial)
print("# costo_produccion: ",costo_produccion)
print("# existencia_final: ",existencia_final)
print("# costo_venta: ",costo_venta)
