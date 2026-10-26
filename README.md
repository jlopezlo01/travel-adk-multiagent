# Travel ADK Multiagent

Proyecto del laboratorio UCV de Sistemas Inteligentes: asistente de viajes con Google ADK. Un agente coordinador delega la investigación actual, el itinerario, el presupuesto, los riesgos y la cultura local en agentes especializados.

## Requisitos

- Python 3.11, 3.12 o 3.13
- Git
- Una clave de Google AI Studio para ejecutar agentes con Gemini
- Poetry (se instala dentro del entorno virtual en estos pasos)

## Preparar el entorno en Windows PowerShell

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install poetry
poetry install
Copy-Item .env.example .env
```

Edita `.env` y agrega `GOOGLE_API_KEY`. No subas ese archivo a Git. Si PowerShell bloquea la activación, usa `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` solo en la ventana actual o ejecuta los comandos desde Git Bash.

## Ejecutar

```powershell
poetry run adk run travel_assistant
poetry run adk web --port 8000
```

Para la interfaz web, abre <http://localhost:8000> y selecciona `travel_assistant`.

## Pruebas y calidad

```powershell
poetry run pytest
poetry run ruff check .
poetry run pytest --cov=travel_assistant --cov-report=term-missing --cov-report=xml
```

Las pruebas cubren cálculos deterministas y la estructura del equipo de agentes; no requieren llamadas a Gemini.

## Pruebas manuales del laboratorio

Con `.env` configurado, prueba en la consola o en ADK Web:

1. `Quiero viajar 5 días a Cusco en julio. Busca información actualizada y propón un itinerario.`
2. `Planeo viajar 4 días a Buenos Aires con presupuesto medio. ¿Qué itinerario recomiendas?`
3. `Quiero visitar Arequipa por 3 días. ¿Qué riesgos debo considerar?`
4. `Estoy pensando viajar a París por 5 días. Dame una propuesta general y recomendaciones.`

Guarda las respuestas reales de Cusco y París como evidencia después de ejecutarlas con tu clave.

## Agentes

- `travel_coordinator_agent`: delega y consolida la respuesta en español.
- `web_search_agent`: utiliza Google Search para información que puede cambiar.
- `itinerary_agent`: organiza actividades por día con tiempos realistas.
- `budget_agent`: explica un cálculo referencial con la herramienta Python.
- `risk_reviewer_agent`: enumera precauciones según destino y temporada.
- `local_culture_agent`: sugiere comida, costumbres y frases útiles.

## Git y publicación

El laboratorio propone `main`, `develop` y `feature/travel-multiagent`, y un Pull Request hacia `develop`. Revisa [ENTREGA.md](ENTREGA.md) para los pasos que necesitan tus cuentas de GitHub y Sonar.

Para iniciar el repositorio y crear las ramas después de configurar tu identidad Git:

```powershell
git init
git add .
git commit -m "feat: add travel multiagent laboratory"
git branch -M main
git switch -c develop
git switch -c feature/travel-multiagent
```

## Preguntas de análisis

Las respuestas argumentadas están en [ANALISIS.md](ANALISIS.md).
