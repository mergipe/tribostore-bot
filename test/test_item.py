import pytest

from tribostorebot.item import Item
from tribostorebot.item import ItemList

def _assert_item_attributes(item):
    assert item.name == 'Nome'
    assert item.description == 'Descrição'
    assert item.cost == 'Preço'
    assert item.enabled == True
    assert item.available_quantity == 10
    assert item.total_quantity == 20

def _create_item_list():
    return [
        Item('Nome1', 'Descrição1', 'Preço1', True, 10, 20),
        Item('Nome2', 'Descrição2', 'Preço2', False, 20, 40),
        Item('Nome1', 'Descrição1', 'Preço1', True, 10, 20)
    ]

def test_item_instantiation():
    item = Item('Nome', 'Descrição', 'Preço', True, 10, 20)
    _assert_item_attributes(item)

def test_item_instantiation_from_dict():
    dictionary = {
        'name': 'Nome',
        'description': 'Descrição',
        'cost': 'Preço',
        'enabled': True,
        'quantity': {
            'current': 10,
            'total': 20
        }
    }
    item = Item.from_dict(dictionary)
    _assert_item_attributes(item)

def test_item_equality():
    item1, item2, item3 = _create_item_list()
    assert item2 != item1
    assert item3 == item1
    assert item3 != item2
    assert None != item1

def test_item_le_and_lt():
    item1, item2, item3 = _create_item_list()

    assert item1 <= item2
    assert item1 <= item3
    assert item3 <= item1
    assert item3 <= item2

    assert item1 < item2
    assert item3 < item2

    with pytest.raises(TypeError):
        item1 < 5

    with pytest.raises(TypeError):
        item1 <= 5

def test_itemlist_instantiation():
    itemlist = ItemList()
    assert itemlist._items == []

    items = _create_item_list()
    itemlist = ItemList(items)
    assert itemlist._items == items

def test_itemlist_sort_by_name():
    items = _create_item_list()
    itemlist = ItemList(items)
    itemlist.sort_by_name()
    l = itemlist._items
    assert all(l[i] <= l[i+1] for i in range(len(l)-1))
