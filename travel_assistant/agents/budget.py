"""Agente especializado en estimación de presupuesto."""

import os

from google.adk.agents import Agent

from travel_assistant.tools.budget_tools import estimate_trip_budget

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

budget_agent = Agent(
    name="budget_agent",
    model=MODEL,
    description="Estima un presupuesto referencial cuando hay datos suficientes.",
    instruction="""Responde en español. Si el usuario proporciona destino, días y gasto diario,
usa la herramienta para calcular un total referencial. Si faltan datos, pregunta por ellos
antes de calcular. Explica que el cálculo no es una cotización y separa rubros solo si hay
datos suficientes; recomienda verificar precios y moneda con proveedores actuales.""",
    tools=[estimate_trip_budget],
)
