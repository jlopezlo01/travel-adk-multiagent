from travel_assistant.tools.budget_tools import estimate_trip_budget


def test_estimate_trip_budget_success():
    result = estimate_trip_budget("Cusco", 5, 80)
    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert result["days"] == 5
    assert result["estimated_total_usd"] == 400


def test_estimate_trip_budget_rejects_invalid_values():
    assert estimate_trip_budget("Cusco", 0, 80)["status"] == "error"
    assert estimate_trip_budget("Cusco", 5, 0)["status"] == "error"
    assert estimate_trip_budget("  ", 5, 80)["status"] == "error"


def test_estimate_trip_budget_rounds_total():
    result = estimate_trip_budget("Lima", 3, 10.336)
    assert result["estimated_total_usd"] == 31.01
