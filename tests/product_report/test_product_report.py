from inventory_report.product import Product


def test_product_report() -> None:
    instance_product = Product(
        '1', 'carne', 'friboi', '10/01/2019', '10/05/2020', '123123', 'embalado'
    )

    assert instance_product.__str__() == (
        f'The product 1 - carne '
        f'with serial number 123123 '
        f'manufactured on 10/01/2019 '
        f'by the company friboi '
        f'valid until 10/05/2020 '
        f'must be stored according to the following instructions: '
        f'embalado.'
    )
