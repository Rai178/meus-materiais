def make_cars(manufacture, model, **info_car):
    info_car['manufacture_name'] = manufacture
    info_car['model_name'] = model
    return info_car


car = make_cars('subaru', 'outback', color='blue', tow_packge=False)
print(car)