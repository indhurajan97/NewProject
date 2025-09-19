from faker import Faker

fake = Faker()

def random_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone": fake.phone_number(),
    }
