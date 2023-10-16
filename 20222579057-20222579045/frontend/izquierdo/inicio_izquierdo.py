import dash
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Contenido de inicio_izquierdo con la lista desplegable
inicio_izquierdo = html.Div([
    html.H3("Clasificación de los suelos",style={'text-align': 'center', 'color': 'steelblue'}),
    html.P("Los suelos se pueden clasificar en dos tipos principales: Granulares y Finos, dependiendo de cómo está distribuido el material que pasa. Si más del 50% del material pasa a través de un tamiz más pequeño conocido como Tamiz número 200 (abreviado como T200), se considera que el suelo es FINO. Por otro lado, si menos del 50% del material pasa por este tamiz, entonces el material se clasifica como GRANULAR y puede ser grava o arena.", style={'text-align': 'justify'}),
    
    # Lista desplegable para seleccionar el concepto
    dcc.Dropdown(
        id='concepto-dropdown',
        options=[
            {'label': 'Suelos Granulares', 'value': 'granulares'},
            {'label': 'Suelos Finos', 'value': 'finos'},
            {'label': 'Límite Líquido', 'value': 'Limite Liquido'},
            {'label': 'Límite Plástico', 'value': 'Limite Plastico'},
            {'label': 'Índice de plasticidad', 'value': 'Indice de plasticidad'},
            {'label': 'Carta de plasticidad', 'value': 'Carta de plasticidad'},
            {'label': 'Coeficiente de uniformidad', 'value': 'Coeficiente de uniformidad'},
            {'label': 'Coeficiente de curvatura', 'value': 'Coeficiente de curvatura'},
        ],
        value='granulares'  # Valor predeterminado
    ),
    
    # Div para mostrar la descripción del concepto
    html.Div(id='concepto-descripcion'),
    
    # Div para mostrar la descripción debajo de la definición
    html.Div(id='descripcion-bajo-definicion')
])

def actualizar_descripcion(selected_concept):
    if selected_concept == 'granulares':
        return "Los suelos granulares se caracterizan por tener menos del 50% de material que pasa por el Tamiz número 200 (T200). Estos suelos pueden incluir grava y arena."
    elif selected_concept == 'finos':
        return "Los suelos finos se caracterizan por tener más del 50% de material que pasa por el Tamiz número 200 (T200). Estos suelos son considerados suelos finos y pueden incluir limo y arcilla."
    elif selected_concept == 'Limite Liquido':
        return "El Límite Líquido (LL) es la humedad en la que un suelo pasa de un estado plástico a un estado líquido. Se determina mediante un ensayo de penetración y es importante en la clasificación de suelos y en la ingeniería geotécnica."
    elif selected_concept == 'Limite Plastico':
        return "El Límite Plástico (LP) es la humedad en la que un suelo se vuelve lo suficientemente plástico como para ser moldeado, pero aún conserva cierta cohesión. Se determina mediante un ensayo de enrollamiento y es esencial para definir la plasticidad de un suelo."
    elif selected_concept == 'Indice de plasticidad':
        return "El Índice de Plasticidad (IP) es la diferencia entre el Límite Líquido (LL) y el Límite Plástico (LP) de un suelo. Este índice se utiliza para evaluar la capacidad de un suelo para retener agua y su plasticidad, lo que es fundamental en la ingeniería de suelos."
    elif selected_concept == 'Carta de plasticidad':
        return "La Carta de Plasticidad es un gráfico que representa el Límite Líquido (LL) y el Límite Plástico (LP) de un suelo, lo que permite clasificarlo en términos de su plasticidad y proporciona información valiosa para el diseño geotécnico."
    elif selected_concept == 'Coeficiente de uniformidad':
        return "El Coeficiente de Uniformidad (CU) es una medida que indica la variabilidad del tamaño de las partículas en un suelo. Se calcula dividiendo el tamaño de partícula D60 (diámetro que el 60% de las partículas son más pequeñas) por el tamaño de partícula D10 (diámetro que el 10% de las partículas son más pequeñas)."
    elif selected_concept == 'Coeficiente de curvatura':
        return "El Coeficiente de Curvatura (CC) es una medida que cuantifica la variación en el tamaño de partícula de un suelo. Se calcula dividiendo la diferencia entre los diámetros D30 y D10 (D30 - D10) por la diferencia entre los diámetros D60 y D10 (D60 - D10). Un CC alto indica una curva granulométrica más amplia."

# Callback para actualizar la descripción
@app.callback(Output('concepto-descripcion', 'children'), [Input('concepto-dropdown', 'value')])
def update_concept_description(selected_concept):
    return actualizar_descripcion(selected_concept)

# Callback para mostrar la descripción debajo de la definición
@app.callback(Output('descripcion-bajo-definicion', 'children'), [Input('concepto-dropdown', 'value')])
def update_description_below_definition(selected_concept):
    return actualizar_descripcion(selected_concept)