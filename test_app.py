import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def start_dash_app():
    """Fixture to import and start the Dash app."""
    return import_app("app")

def test_app_header(dash_duo, start_dash_app):
    """Check if the app header is present."""
    dash_duo.start_server(start_dash_app)
    dash_duo.wait_for_text_to_equal("h1", "Pink Morsel Sales Visualizer", timeout=10)

def test_app_graph(dash_duo, start_dash_app):
    """Check if the graph exists in the app."""
    dash_duo.start_server(start_dash_app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None

def test_app_radio_buttons(dash_duo, start_dash_app):
    """Check if all radio buttons are present."""
    dash_duo.start_server(start_dash_app)
    radio_buttons = dash_duo.find_elements("input[type='radio']")
    assert len(radio_buttons) == 5