"""Agente especializado en precauciones de viaje."""

import os

from google.adk.agents import Agent

from travel_assistant.tools.risk_tools import assess_basic_travel_risks

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

risk_reviewer_agent = Agent(
    name="risk_reviewer_agent",
    model=MODEL,
    description="Revisa riesgos prácticos y propone medidas preventivas.",
    instruction="""Evalúa clima, altura, temporada, seguridad, salud, transporte y documentos
de forma prudente. Usa la herramienta para las comprobaciones generales cuando haya destino
y temporada. Da recomendaciones concretas sin alarmismo. No sustituye asesoría médica,
consular ni alertas oficiales; para información actualizada pide al buscador fuentes oficiales.""",
    tools=[assess_basic_travel_risks],
)
