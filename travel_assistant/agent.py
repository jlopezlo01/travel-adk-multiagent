"""Punto de entrada requerido por ADK."""

from dotenv import load_dotenv

load_dotenv()

from travel_assistant.agents.coordinator import travel_coordinator_agent  # noqa: E402

root_agent = travel_coordinator_agent
