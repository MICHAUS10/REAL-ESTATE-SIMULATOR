import streamlit as st

def calcular_roi_anual_con_credito_y_plusvalia():
    st.title("Simulador de Inversiones: ROI con Crédito Hipotecario y Plusvalía")
    
    # Solicitar al usuario ingresar el precio de la propiedad
    precio_propiedad = st.number_input("Ingresa el precio total de la propiedad en preventa:", min_value=0.0)
    
    # Solicitar al usuario el tiempo (en años) entre la compra y la venta
    tiempo_espera = st.number_input("Ingresa el número de años desde la compra hasta la venta:", min_value=0.0)
    
    # Solicitar al usuario ingresar el enganche y el descuento sobre el valor del inmueble
    enganche_porcentaje = st.slider("Ingresa el porcentaje de enganche que deseas pagar (en %):", 0, 100, 30) / 100
    descuento_porcentaje = st.slider("Ingresa el porcentaje de descuento sobre el precio total del inmueble (en %):", 0, 100, 0) / 100
    
    # Calcular el monto final pagado por la propiedad después del descuento
    precio_final = precio_propiedad * (1 - descuento_porcentaje)
    
    # Calcular el enganche pagado
    monto_enganche = precio_final * enganche_porcentaje
    
    # Calcular el monto pendiente (restante a financiar con crédito hipotecario)
    monto_pendiente = precio_final - monto_enganche
    
    # Solicitar detalles del crédito hipotecario
    tasa_interes_anual = st.number_input("Ingresa la tasa de interés anual del crédito hipotecario (en %):", min_value=0.0) / 100
    plazo_credito = st.number_input("Ingresa el plazo del crédito hipotecario (en años):", min_value=0)
    
    # Calcular la tasa de interés mensual
    tasa_interes_mensual = tasa_interes_anual / 12
    
    # Calcular el número total de meses del crédito
    meses_credito = plazo_credito * 12
    
    # Calcular el pago mensual usando la fórmula de amortización
    pago_mensual = (monto_pendiente * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** -meses_credito)
    
    # Calcular los pagos realizados hasta la fecha de venta
    meses_espera = int(tiempo_espera * 12)
    
    # Variables para calcular el saldo pendiente e intereses acumulados mes a mes
    saldo_actual = monto_pendiente
    intereses_pagados_hasta_la_fecha = 0.0
    total_pagado_credito = 0.0  # Inicializar el total pagado por crédito hasta la fecha
    
    # Simulación mes a mes para calcular el saldo pendiente e intereses acumulados
    for mes in range(meses_espera):
        interes_mes = saldo_actual * tasa_interes_mensual
        capital_mes = pago_mensual - interes_mes
        saldo_actual -= capital_mes
        intereses_pagados_hasta_la_fecha += interes_mes
        total_pagado_credito += pago_mensual  # Acumular el pago total mensual
    
    saldo_restante = saldo_actual  # Saldo pendiente al momento de la venta
    
    # Solicitar el porcentaje de plusvalía anual
    plusvalia_anual = st.number_input("Ingresa el porcentaje de plusvalía anual esperado (en %):", min_value=0.0) / 100
    
    # Calcular el precio de venta esperado usando la fórmula de crecimiento compuesto
    precio_venta_esperado = precio_final * (1 + plusvalia_anual) ** tiempo_espera
    
    # Mostrar los resultados
    if st.button("Calcular ROI"):
        st.write(f"Precio final de la propiedad después del descuento: ${precio_final:,.2f}")
        st.write(f"Enganche pagado: ${monto_enganche:,.2f}")
        st.write(f"Total restante a financiar con crédito hipotecario: ${monto_pendiente:,.2f}")
        st.write(f"Pago mensual del crédito hipotecario: ${pago_mensual:,.2f}")
        st.write(f"Saldo restante del crédito en el momento de la venta: ${saldo_restante:,.2f}")
        st.write(f"Precio de venta esperado después de {tiempo_espera:.2f} años con plusvalía: ${precio_venta_esperado:,.2f}")

if __name__ == "__main__":
    calcular_roi_anual_con_credito_y_plusvalia()
