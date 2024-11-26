from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology", "origin_country": "Japan"},
        {"name": "Mercedes", "description": "Great cars. German technology", "origin_country": "Germany"},
        {"name": "Audi", "description": "Great cars. German technology", "origin_country": "Germany"},
        {"name": "Kia", "description": "Great cars. Korean technology", "origin_country": "South Korea"},
        {"name": "Toyota", "description": "Great cars. Japanese technology", "origin_country": "Japan"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data["name"],
                description=data["description"],
                origin_country=data["origin_country"],
            )
        )

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "dealer_id": "D001", "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "dealer_id": "D002", "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "dealer_id": "D003", "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SEDAN", "year": 2023, "dealer_id": "D004", "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SEDAN", "year": 2023, "dealer_id": "D005", "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SEDAN", "year": 2023, "dealer_id": "D006", "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SEDAN", "year": 2023, "dealer_id": "D007", "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SEDAN", "year": 2023, "dealer_id": "D008", "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SEDAN", "year": 2023, "dealer_id": "D009", "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "dealer_id": "D010", "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "dealer_id": "D011", "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "SEDAN", "year": 2023, "dealer_id": "D012", "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "SEDAN", "year": 2023, "dealer_id": "D013", "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "SEDAN", "year": 2023, "dealer_id": "D014", "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "dealer_id": "D015", "car_make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            car_make=data["car_make"],
            type=data["type"],
            year=data["year"],
            dealer_id=data["dealer_id"],
        )
