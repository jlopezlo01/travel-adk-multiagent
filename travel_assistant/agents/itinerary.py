"""Agente especializado en itinerarios."""

import os

from google.adk.agents import Agent

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

itinerary_agent = Agent(
    name="itinerary_agent",
    model=MODEL,
    description="Propone itinerarios realistas por día.",
    instruction="""Diseña itinerarios en español organizados por día y en bloques de mañana,
tarde y noche. Considera traslados realistas, descanso, duración del viaje, intereses y
accesibilidad indicada por el usuario. Explica brevemente el orden propuesto. No inventes
reservas ni horarios confirmados; señala qué datos se deben verificar.""",
)
