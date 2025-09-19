
from faker import Faker

fake = Faker()

def random_user():
    return {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'uuid': fake.uuid4()
    }

def random_text(paragraphs=1):
    return "\\n\\n".join(fake.paragraphs(paragraphs))

