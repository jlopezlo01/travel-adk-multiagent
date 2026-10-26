from travel_assistant.tools.risk_tools import assess_basic_travel_risks


def test_assess_basic_travel_risks_for_cusco():
    result = assess_basic_travel_risks("Cusco", "temporada alta")
    assert result["status"] == "success"
    assert any("altura" in risk.lower() for risk in result["risks"])
    assert any("reserva" in risk.lower() for risk in result["risks"])


def test_assess_basic_travel_risks_for_rain():
    result = assess_basic_travel_risks("Lima", "temporada de lluvias")
    assert any("lluvia" in risk.lower() for risk in result["risks"])


def test_assess_basic_travel_risks_default_case():
    result = assess_basic_travel_risks("Lima", "normal")
    assert result["status"] == "success"
    assert len(result["risks"]) == 1
