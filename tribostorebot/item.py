class Item:

    def __init__(self, name, description, cost, enabled, available_quantity,
                 total_quantity):
        self.name = name
        self.description = description
        self.cost = cost
        self.enabled = enabled
        self.available_quantity = available_quantity
        self.total_quantity = total_quantity

    @classmethod
    def from_dict(cls, dictionary):
        return cls(
            dictionary.get('name'),
            dictionary.get('description'),
            dictionary.get('cost'),
            dictionary.get('enabled'),
            dictionary.get('quantity').get('current'),
            dictionary.get('quantity').get('total')
        )

    def __eq__(self, other):
        if isinstance(other, Item):
            return (
                self.name == other.name
                and self.description == other.description
                and self.cost == other.cost
                and self.enabled == other.enabled
                and self.available_quantity == other.available_quantity
                and self.total_quantity == other.total_quantity
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Item):
            return self.name < other.name
        return False

    def __le__(self, other):
        if isinstance(other, Item):
            return self.name <= other.name
        return False


class ItemList:

    def __init__(self, items=None):
        if items == None:
            self._items = []
        else:
            self._items = items

    def sort_by_name(self):
        self._items = sorted(self._items)
