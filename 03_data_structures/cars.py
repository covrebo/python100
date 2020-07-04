cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeeps = ''
    for model in cars.get('Jeep'):
        if len(jeeps) == 0:
            jeeps = model
        else:
            jeeps = jeeps + f', {model}'
    return jeeps


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    models = []
    for keys, values in cars.items():
        models.append(values[0])
    return models


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    trail_list = []
    for values in cars.values():
        for value in values:
            if grep.lower() in value.lower():
                trail_list.append(value)
    return sorted(trail_list)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    model_list = {}
    for keys, values in cars.items():
        model_list[keys] = sorted(values)
    return model_list