"""Cálculos referenciales de presupuesto de viaje."""


def estimate_trip_budget(destination: str, days: int, daily_budget_usd: float) -> dict:
    """Calcula un presupuesto base multiplicando días por gasto diario.

    Args:
        destination: Destino del viaje.
        days: Cantidad de días, mayor que cero.
        daily_budget_usd: Presupuesto diario referencial en dólares, mayor que cero.

    Returns:
        Resultado con estado y detalle del cálculo, o un mensaje de validación.
    """
    if not destination.strip():
        return {"status": "error", "message": "El destino no puede estar vacío."}
    if days <= 0:
        return {"status": "error", "message": "La cantidad de días debe ser mayor que cero."}
    if daily_budget_usd <= 0:
        return {"status": "error", "message": "El presupuesto diario debe ser mayor que cero."}

    return {
        "status": "success",
        "destination": destination.strip(),
        "days": days,
        "daily_budget_usd": daily_budget_usd,
        "estimated_total_usd": round(days * daily_budget_usd, 2),
        "note": "Estimación referencial; no incluye necesariamente vuelos ni tasas.",
    }
