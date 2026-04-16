from app import app
 
 
def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.wait_for_element("h1", timeout=10)
    assert header.text == "Pink Morsel Visualiser"

def test_visualisation_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)

def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)