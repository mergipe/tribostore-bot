import pytest

from tribostorebot.items import Item, ItemList, ItemRetriever
from tribostorebot.config import Config


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

def _create_dictionary():
    return {
        'name': 'Nome',
        'description': 'Descrição',
        'cost': 'Preço',
        'enabled': True,
        'quantity': {
            'current': 10,
            'total': 20
        }
    }

def _create_dictlist():
    return [
        _create_dictionary()
    ] * 3

def test_item_instantiation():
    item = Item('Nome', 'Descrição', 'Preço', True, 10, 20)
    _assert_item_attributes(item)

def test_item_instantiation_from_dict():
    item = Item.from_dict(_create_dictionary())
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

def test_itemlist_instantiation_from_dictlist():
    itemlist = ItemList.from_dictlist(_create_dictlist())
    
    assert type(itemlist._items).__name__ == 'list'
    assert len(itemlist) > 0

    for item in itemlist._items:
        assert isinstance(item, Item)

def test_itemlist_sort_by_name():
    itemlist = ItemList(_create_item_list())
    itemlist.sort_by_name()
    l = itemlist._items
    assert all(l[i] <= l[i+1] for i in range(len(l)-1))

def test_itemlist_len():
    items = _create_item_list()
    itemlist = ItemList(items)
    assert len(itemlist) == len(items)

def test_itemlist_eq():
    itemlist1 = ItemList(_create_item_list())
    itemlist2 = ItemList(_create_item_list())
    itemlist3 = ItemList(_create_item_list()[0:2])
    itemlist4 = ItemList(_create_item_list())
    itemlist4._items[2].name = 'Nome5'

    assert itemlist1 == itemlist2
    assert itemlist1 != itemlist3
    assert itemlist1 != itemlist4

def test_itemlist_filter_available():
    itemlist = ItemList(_create_item_list())
    itemlist.filter_available()

    for item in itemlist._items:
        assert item.enabled and item.available_quantity > 0


def test_retriever_instantiation():
    url = 'mock_url'
    s = ItemRetriever(url)
    assert s._url == url

def test_retriever_retrieve_items():
    cfg = Config()
    r = ItemRetriever(cfg.request_url)
    itemlist = r.retrieve_items()
    assert type(itemlist).__name__ == ItemList.__name__

def test_retriever_retrieve_items_exception():
    r = ItemRetriever('mock_url')

    with pytest.raises(Exception):
        itemlist = r.retrieve_items()
