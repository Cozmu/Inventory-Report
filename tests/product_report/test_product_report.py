from inventory_report.product import Product


def test_product_report() -> None:
    instance_product = Product(
        '1', 'carne', 'friboi', '10/01/2019', '10/05/2020', '123123',
        'embalado'
    )

    assert instance_product.__str__() == (
        'The product 1 - carne '
        'with serial number 123123 '
        'manufactured on 10/01/2019 '
        'by the company friboi '
        'valid until 10/05/2020 '
        'must be stored according to the following instructions: '
        'embalado.'
    )
