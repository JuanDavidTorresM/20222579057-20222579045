import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Contenido de inicio_derecho con la tabla
inicio_centro = html.Div([
    html.P("La clasificación de suelos es una parte fundamental de la ingeniería civil y la construcción. Comprender las propiedades de los suelos es esencial para el diseño de cimientos, carreteras, presas y muchas otras estructuras. La norma de la Asociación Americana de Carreteras y Transportes (ASHTO) proporciona un sistema de clasificación que se utiliza ampliamente en la industria.", style={'text-align': 'justify'}),
    
    html.P("La correcta clasificación de suelos permite tomar decisiones informadas en proyectos de construcción y geotécnicos. Al conocer las características de un suelo, los ingenieros pueden determinar la capacidad de carga, la permeabilidad y la estabilidad de una estructura. Además, la clasificación de suelos es esencial para cumplir con las regulaciones de construcción y garantizar la seguridad y eficiencia de las obras civiles.", style={'text-align': 'justify'}),
    
    html.P("Nuestra aplicación te ofrece una forma interactiva de aprender y aplicar la clasificación de suelos según la ASHTO. Puedes explorar la tabla granulométrica, la curva granulométrica y la carta de plasticidad. Aprenderás a identificar y clasificar diferentes tipos de suelos, lo que te brindará una base sólida para tus futuros proyectos de ingeniería civil.", style={'text-align': 'justify'}),
    
    html.P("¡Te invitamos a explorar nuestra aplicación y mejorar tus habilidades en la clasificación de suelos! Utiliza las herramientas proporcionadas para familiarizarte con los conceptos y practicar la identificación de suelos. La clasificación de suelos es una habilidad que te abrirá puertas en el mundo de la ingeniería civil.", style={'text-align': 'justify'}),
    
    html.H3("Conclusión"),
    html.P("La clasificación de suelos es un aspecto crucial de la ingeniería civil que influye en la seguridad y la eficiencia de los proyectos de construcción. La norma ASHTO proporciona un sistema de clasificación ampliamente aceptado que ayuda a los ingenieros a entender y trabajar con diferentes tipos de suelos. Nuestra aplicación te brinda una oportunidad única de aprender y practicar la clasificación de suelos de manera interactiva.", style={'text-align': 'justify'}),
    html.P("Aprovecha esta herramienta para mejorar tus habilidades y conocimientos en geotecnia. Al comprender la importancia de la clasificación de suelos, estarás mejor preparado para abordar desafíos en futuros proyectos.", style={'text-align': 'justify'}),
])
