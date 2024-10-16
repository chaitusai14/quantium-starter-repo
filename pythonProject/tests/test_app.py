import pytest
from dash.testing.application_runners import import_app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_app(dash_duo):
    # Set the path to ChromeDriver executable
    path = "/Users/saichaitanya/Downloads/chromedriver-mac-arm64/chromedriver"
    chrome_service = ChromeService(executable_path=path)

    dash_duo.start_driver(webdriver.Chrome(service=chrome_service))

    app = import_app("dash_visual")
    dash_duo.start_server(app)
    return dash_duo

# Test 1: Verify the header is present
def test_header_present(dash_app):
    header = dash_app.find_element("h1")
    assert header.text == "Soul Foods Sales Data Visualiser", "Header text does not match"

# Test 2: Verify the visualisation is present
def test_visualization_present(dash_app):
    # Check if the graph element is present
    graph = dash_app.find_element("#sales-line-chart")
    assert graph is not None, "Graph is not present on the page"

# Test 3: Verify the region picker (radio items) is present
def test_region_picker_present(dash_app):
    # Check if the radio items for region selection are present
    region_picker = dash_app.find_element("#region-filter")
    assert region_picker is not None, "Region picker is not present on the page"
