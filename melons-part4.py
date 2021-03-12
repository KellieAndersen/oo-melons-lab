"""Classes for melon orders."""

import random

class AbstractMelonOrder(): # parent class, child classes inherit everything here
    """An abstract base class that other Melon Orders inherit from."""

    # all melon orders have these attributes in common
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_base_price(self):
        """get a new base price randomly for splurge pricing"""
        base_price = random.randrange(5, 10)

        return base_price

     # getting total (money) owed for each order  
     def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "christmas melon":
            base_price = base_price * 1.5
   
        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == "international" & self.qty < 10:
            total = total + 3

        return total

    # shipping melons
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder): # child class
    """A melon order within the USA."""

    # taking species of order and how many
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        # taking attributes from the parent, but changing specifically the order_type and tax
        # so that all domestic orders have the same order_type (domestic) and tax rate (0.08)
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder): # child class
    """An international (non-US) melon order."""

    # taking species of order and how many, plus what country
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        # taking attributes from the parent, but changing specifically the order_type and tax
        # so that all domestic orders have the same order_type (international) and tax rate (0.17)
        super().__init__(species, qty, "international", 0.17)
        # international orders are special, because they have an extra attribute, country_code
        self.country_code = country_code
        
        # tells them where to ship the melon(s)
    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government order of melons."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0.00)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Whether or not the melon order has passed inspection."""

        self.passed_inspection = passed
