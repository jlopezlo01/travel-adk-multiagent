"""Evaluación introductoria y no exhaustiva de riesgos de viaje."""


def assess_basic_travel_risks(destination: str, season: str) -> dict:
    """Devuelve precauciones generales para destino y temporada indicados.

    Args:
        destination: Nombre de la ciudad o región.
        season: Temporada o contexto temporal descrito por el viajero.

    Returns:
        Estado, destino, temporada y lista de precauciones generales.
    """
    destination_normalized = destination.casefold().strip()
    season_normalized = season.casefold().strip()
    risks = []

    if "cusco" in destination_normalized or "machu picchu" in destination_normalized:
        risks.append(
            "Considera la altura, aclimatación gradual e indicaciones médicas personales."
        )
    if any(word in season_normalized for word in ("lluvia", "rain", "húmeda", "wet")):
        risks.append(
            "Lleva protección para lluvia y confirma el estado de rutas y transporte."
        )
    if any(word in season_normalized for word in ("alta", "high", "julio", "agosto")):
        risks.append(
            "Reserva con anticipación y confirma disponibilidad y "
            "horarios con proveedores oficiales."
        )
    if not risks:
        risks.append(
            "Consulta clima, transporte, requisitos sanitarios y documentos en fuentes oficiales."
        )

    return {"status": "success", "destination": destination, "season": season, "risks": risks}
