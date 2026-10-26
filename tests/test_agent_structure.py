from travel_assistant.agent import root_agent


def test_root_agent_name_and_sub_agents():
    assert root_agent.name == "travel_coordinator_agent"
    assert len(root_agent.sub_agents) == 5


def test_coordinator_includes_required_specialists():
    names = {agent.name for agent in root_agent.sub_agents}
    assert names == {
        "web_search_agent",
        "itinerary_agent",
        "budget_agent",
        "risk_reviewer_agent",
        "local_culture_agent",
    }
