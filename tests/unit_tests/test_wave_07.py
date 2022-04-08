import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#1 @pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(condition=2.0, age=4.0)
    item_b = Electronics(condition=4.0, age=2.0)
    item_c = Decor(condition=4.0, age=2.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0, age=4.0)
    item_e = Decor(condition=4.0, age=2.0)
    item_f = Clothing(condition=4.0, age=2.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # raise Exception("Complete this test according to comments below.")
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_a, item_b, item_f]
    assert jesse.inventory == [item_d, item_e, item_c]

#2 @pytest.mark.skip
def test_swap_by_newest_reordered():
    # Arrange
    item_a = Decor(condition=2.0, age=4.0)
    item_b = Electronics(condition=4.0, age=2.0)
    item_c = Decor(condition=4.0, age=2.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0, age=4.0)
    item_e = Decor(condition=4.0, age=2.0)
    item_f = Clothing(condition=4.0, age=2.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_b, item_a, item_f]
    assert jesse.inventory == [item_e, item_d, item_c]

#3 @pytest.mark.skip
def test_swap_by_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0, age=4.0)
    item_b = Decor(condition=4.0, age=2.0)
    item_c = Clothing(condition=4.0, age=2.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

#4 @pytest.mark.skip
def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0, age=4.0)
    item_b = Decor(condition=4.0, age=2.0)
    item_c = Clothing(condition=4.0, age=2.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

#5 @pytest.mark.skip
def test_swap_by_newest_no_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0, age=4.0)
    item_b = Electronics(condition=4.0, age=2.0)
    item_c = Decor(condition=4.0, age=2.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=4.0)
    item_e = Decor(condition=4.0, age=2.0)
    item_f = Clothing(condition=4.0, age=2.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert jesse.inventory == [item_d, item_e, item_f]

#6 @pytest.mark.skip
def test_swap_by_newest_no_other_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0, age=4.0)
    item_b = Electronics(condition=4.0, age=2.0)
    item_c = Decor(condition=4.0, age=2.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    #raise Exception("Complete this test according to comments below.")
    assert result == False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert jesse.inventory == [item_f, item_e, item_d]