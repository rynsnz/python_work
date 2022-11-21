def make_car(manufacturer, model, **car_info):
    """Build a car containing everything the customer selected."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info