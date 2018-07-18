def test_addition(calc_page):
    calc_page.add(2.25, 2.75, 3.04)
    assert calc_page.is_result_match(8.04)
