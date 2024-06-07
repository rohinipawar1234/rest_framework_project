from django.core.management.base import BaseCommand
from faker import Faker
from drinks_app.models import Drink

class Command(BaseCommand):
    help = 'Generate fake data for the Drink model'

  
    def handle(self, *args, **kwargs):
    
        fake = Faker()

        drink_data = [
            {'name': 'Coffee', 'description': 'A classic hot beverage made from roasted coffee beans.'},
            {'name': 'Tea', 'description': 'A popular drink made by steeping tea leaves or herbs in hot water.'},
            {'name': 'Mocha', 'description': 'A delicious combination of coffee, chocolate, and milk.'},
            {'name': 'Latte', 'description': 'Espresso mixed with steamed milk, often topped with a small amount of foam.'},
            {'name': 'Smoothie', 'description': 'A blended beverage typically made with fruits, yogurt, and ice.'},
            {'name': 'Iced Tea', 'description': 'Chilled tea served with ice, often sweetened.'},
            {'name': 'Juice', 'description': 'Freshly squeezed or processed liquid obtained from fruits or vegetables.'},
            {'name': 'Soda', 'description': 'Carbonated beverage available in various flavors.'},
            {'name': 'Mocktail', 'description': 'Non-alcoholic cocktails with a variety of flavors and ingredients.'},
            {'name': 'Milkshake', 'description': 'A creamy and sweet beverage made from ice cream and milk, often flavored.'},
        ]

        for _ in range(10):
            drink = fake.random_element(drink_data)
            Drink.objects.create(name=drink['name'], description=drink['description'])

        self.stdout.write(self.style.SUCCESS(f'Successfully added fake Drink entries.'))
