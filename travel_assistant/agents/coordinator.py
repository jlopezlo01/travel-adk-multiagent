"""Coordinador principal del sistema multiagente."""

import os

from google.adk.agents import Agent

from travel_assistant.agents.budget import budget_agent
from travel_assistant.agents.itinerary import itinerary_agent
from travel_assistant.agents.local_culture import local_culture_agent
from travel_assistant.agents.risk import risk_reviewer_agent
from travel_assistant.agents.web_search import web_search_agent

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

travel_coordinator_agent = Agent(
    name="travel_coordinator_agent",
    model=MODEL,
    description="Coordina agentes especializados para planificar viajes.",
    instruction="""Eres el coordinador de un asistente de viajes y respondes siempre en español.
Delega la investigación actual en web_search_agent; la planificación diaria en
itinerary_agent; el cálculo en budget_agent cuando se conozca el gasto diario; los riesgos
en risk_reviewer_agent; y la cultura local en local_culture_agent. No inventes datos,
precios ni reservas. Separa hallazgos verificados de sugerencias y comunica incertidumbre.
Si falta información esencial para el presupuesto, pregunta al usuario. Consolida una
respuesta con resumen, hallazgos actuales y fuentes cuando aplique, itinerario, presupuesto
referencial, riesgos, cultura local y recomendaciones finales. Aconseja verificar datos
oficiales antes de reservar.""",
    sub_agents=[
        web_search_agent,
        itinerary_agent,
        budget_agent,
        risk_reviewer_agent,
        local_culture_agent,
    ],
)
