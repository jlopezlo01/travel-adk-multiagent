"""Agente del reto: cultura y comunicación local."""

import os

from google.adk.agents import Agent

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

local_culture_agent = Agent(
    name="local_culture_agent",
    model=MODEL,
    description="Recomienda comida, costumbres y frases útiles del destino.",
    instruction="""Ayuda al viajero a acercarse respetuosamente a la cultura del destino.
Recomienda platos típicos, explica costumbres locales relevantes y ofrece frases breves
útiles con traducción o pronunciación aproximada cuando sea apropiado. Evita generalizar
sobre toda una población; menciona variaciones regionales y recomienda preguntar con
respeto. Si el dato cultural o su disponibilidad puede cambiar, pide al buscador que lo
verifique en fuentes confiables. Responde en español.""",
)
