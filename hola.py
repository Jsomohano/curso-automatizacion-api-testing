from graphviz import Digraph

# Crear el diagrama
dot = Digraph(comment="Arquitectura API Client", format="png")

# Nodos principales
dot.node("BaseApiClient", "BaseApiClient\n(Métodos base para requests, manejo de headers, auth)")
dot.node("TaskApiClient", "TaskApiClient\n(Heredado de BaseApiClient, métodos específicos de tasks)")
dot.node("Models", "Modelos Pydantic\n(Validación y tipado de datos)")
dot.node("API", "API Externa\n(Endpoints REST/GraphQL)")

# Relaciones jerárquicas
dot.edge("BaseApiClient", "TaskApiClient", label="Herencia")
dot.edge("TaskApiClient", "API", label="Hace requests a")
dot.edge("Models", "TaskApiClient", label="Usa para requests/responses")
dot.edge("API", "Models", label="Respuestas validadas por")

# Guardar diagrama
output_path = "/mnt/data/api_client_tree.png"
dot.render(output_path, cleanup=True)

output_path
