import dash_bootstrap_components as dbc
from dash import html

# Se crean 2 estilos personalizados para la barra de navegación, uno para el título y el otro para los creadores de la página
navegador_style = {
    'font-size': '24px',  # Tamaño grande para el título principal
    'font-weight': 'bold',  # Texto en negrita
}

autores_style = {
    'font-size': '14px',  # Tamaño más pequeño para los creadores
    'font-style': 'italic',  # Texto en cursiva
}

navegador = dbc.NavbarSimple(
    brand=html.Div([
        html.Span("Clasificación de los Suelos - Universidad Distrital Francisco José de Caldas", style=navegador_style),
        html.Br(),  # Agrega un salto de línea
        html.Span("Natalia Ximena Tovar - 20222579057", style=autores_style),
        html.Br(),
        html.Span("Juan David Torres - 20222579045", style=autores_style),
    ]),
    color="steelblue",
    dark=True,
    fluid=True,  # Haz que la barra de navegación ocupe toda la altura de la página
)