import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Bottonline.cl - BI con Power BI", layout="wide")

# --- HERO SECTION ---
st.image("logo_temp.png", width=120)



st.markdown("<h1 style='font-size: 42px;'>Transforma tus Datos en Decisiones</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 20px; color: gray;'>Aprovecha el poder de Microsoft Power BI con nuestros servicios expertos en Inteligencia de Negocios</p>", unsafe_allow_html=True)

st.markdown("<a href='#contacto'><button style='padding: 0.8em 2em; font-size: 18px; background-color: #0078D7; color: white; border: none; border-radius: 6px;'>Agenda una Consultoría Gratis</button></a>", unsafe_allow_html=True)

st.markdown("---")

# --- BENEFICIOS / SERVICIOS ---
st.header("¿Por qué elegir Bottonline.cl?")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3189/3189876.png", width=60)
    st.subheader("Dashboards Impactantes")
    st.write("Conecta tus fuentes de datos y crea visualizaciones interactivas que impulsan la toma de decisiones.")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/270/270798.png", width=60)
    st.subheader("Automatización de Reportes")
    st.write("Ahorra tiempo con reportes automáticos, actualizados y listos para compartir.")

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/2331/2331970.png", width=60)
    st.subheader("Capacitación y Soporte")
    st.write("Acompañamos a tu equipo para que dominen Power BI y aprovechen al máximo su potencial.")

st.markdown("---")

# --- IMAGEN O DEMO ---

import streamlit as st
import streamlit.components.v1 as components

st.header("Una Imagen Vale Más que Mil Datos")
st.markdown("Visualiza nuestro reporte interactivo embebido directamente aquí:")

components.iframe(
    "https://app.powerbi.com/view?r=eyJrIjoiODZiNDY2MzUtNjI2Zi00ZGJmLWE1ZjgtOTY0ZGY3MDc4ZjJlIiwidCI6IjRhMGVmNGI3LWVhOTMtNGMzNi05OWYyLWEyZDY1YmYyODUwZiJ9",
    width=600,
    height=374
)

st.markdown("---")


# --- TESTIMONIOS ---
st.header("Lo que dicen nuestros clientes")

col1, col2 = st.columns(2)
with col1:
    st.markdown("> ⭐⭐⭐⭐⭐ 'Gracias a Bottonline ahora entendemos mejor nuestros KPIs. ¡El equipo de BI es increíble!'  \n**– Carolina Soto, Gerente Comercial**")

with col2:
    st.markdown("> ⭐⭐⭐⭐⭐ 'Nuestro equipo aprendió Power BI desde cero y ahora generamos reportes sin depender de TI.'  \n**– Diego Fuentes, CFO de empresa logística**")

st.markdown("---")

# --- FORMULARIO DE CONTACTO ---
st.header("¿Listo para potenciar tu empresa con datos?")
st.markdown("Completa el formulario y te contactamos 👇")


with st.form(key="contact_form"):
    nombre = st.text_input("Nombre completo")
    correo = st.text_input("Correo electrónico")
    empresa = st.text_input("Nombre de la empresa")
    mensaje = st.text_area("¿En qué podemos ayudarte?")
    submit_button = st.form_submit_button(label="Enviar mensaje")

if submit_button:
    if nombre and correo and mensaje:
        st.success("✅ ¡Gracias por contactarnos! Te responderemos pronto.")
    else:
        st.error("Por favor completa todos los campos obligatorios.")

st.markdown("---")

# --- FOOTER ---
st.markdown("""
<center>
<p style='font-size: 14px; color: gray;'>© 2025 Bottonline.cl | Inteligencia de Negocios con Microsoft Power BI</p>
<p><a href='https://www.bottonline.cl' target='_blank'>Sitio oficial</a> | contacto@bottonline.cl</p>
</center>
""", unsafe_allow_html=True)
