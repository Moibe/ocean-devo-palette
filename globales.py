import gradio as gr

#MAIN
version = "0.1.2"
env = "dev"
aplicacion = "palette-dev"

seleccion_api = "eligeGratisOCosto" #eligeGratisOCosto , eligeAOB o eligeGratisOCosto
max_size = 20

#Gratis o Costo
api_gratis = ("Moibe/acuarela", "gratis")
api_costo = ("Moibe/acuarela", "costo")

interface_api_name = "/gradio_interface" #El endpoint al que llamará client.

process_cost = 0
seto = "palette"
work = "picswap"
app_path = "/palette-dev"
server_port=7820
#tema = tools.theme_selector()
tema = gr.themes.Default()
flag = "auto"

#Future: Put age to cookies.