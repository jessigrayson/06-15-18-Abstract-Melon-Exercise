"""Classes for melon orders."""

class AbstractMelonOder:
    """An abstract melon order class"""

    def __init__(self, species, qty, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = False

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'Christmas melons':
            base_price = 5 * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3

        return total
class GovernmentMelonOrder(AbstractMelonOder):
    """A tax-free government order"""
    
    self.passed_inspection = False

    def mark_inspection(self):
        self.passed_inspection = True

class DomesticMelonOrder(AbstractMelonOder):
    """A melon order within the USA."""

    tax = 0.08

    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOder):
    """An international (non-US) melon order."""

    tax = 0.17

    order_type = "international"

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        """Initialize melon order attributes."""

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
