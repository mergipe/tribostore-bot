from tribostorebot.item import Item

def _assert_item_attributes(item):
    assert item.name == 'Nome'
    assert item.description == 'Descrição'
    assert item.cost == 'Preço'
    assert item.enabled == True
    assert item.available_quantity == 10
    assert item.total_quantity == 20

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
    item1 = Item('Nome1', 'Descrição1', 'Preço1', True, 10, 20)
    item2 = Item('Nome2', 'Descrição2', 'Preço2', True, 20, 40)
    item3 = Item('Nome1', 'Descrição1', 'Preço1', True, 10, 20)
    assert item2 != item1
    assert item3 == item1
    assert item3 != item2
    assert None != item1
