import logging
import requests


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
        raise TypeError(f"'<' not supported between instances of "
            f"'{type(self).__name__}' and '{type(other).__name__}'")

    def __le__(self, other):
        if isinstance(other, Item):
            return self.name <= other.name
        raise TypeError(f"'<=' not supported between instances of "
            f"'{type(self).__name__}' and '{type(other).__name__}'")

    def __str__(self):
        s = (
            f"{self.name}"
            f"\n{self.description}"
            f"\nPreço (GAUPOINTS): {str(self.cost)}"
             "\nDisponível: "
            f"{str(self.available_quantity) if self.enabled else 'Não'}"
            f"\nEm estoque: {self.total_quantity}"
        )
        return s


class ItemList:

    def __init__(self, items=None):
        if items == None:
            self._items = []
        else:
            self._items = items.copy()

    @classmethod
    def from_dictlist(cls, dictlist):
        items = []

        for dictionary in dictlist:
            item = Item.from_dict(dictionary)
            items.append(item)

        return cls(items)

    def __len__(self):
        return len(self._items)

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        self.sort_by_name()
        other.sort_by_name()
        pairs = zip(self._items, other._items)
        neq = any(x != y for x, y in pairs)

        return not neq

    def sort_by_name(self):
        self._items = sorted(self._items)

    def filter_available(self):
        self._items = [
            item for item in self._items if(
                item.enabled and item.available_quantity > 0
            )
        ]


class Scraper:

    def __init__(self, url):
        self._url = url

    def fetch_items(self):
        try:
            req = requests.get(self._url)

            if req.ok:
                itemlist = ItemList.from_dictlist(req.json())
                itemlist.sort_by_name()
                return itemlist
            else:
                logging.warning('Request error at Scraper.fetch_items(): %s',
                                str(req.json()))
        except:
            logging.exception('Exception raised at Scraper.fetch_items()')
            raise
