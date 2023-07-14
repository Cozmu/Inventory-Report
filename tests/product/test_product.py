from inventory_report.product import Product


def test_create_product() -> None:
    instance_product = Product(
        '1', 'carne', 'friboi', '10/01/2019', '10/05/2020', '123123', 'embalado'
    )

    assert instance_product.id == '1'
    assert instance_product.product_name == 'carne'
    assert instance_product.company_name == 'friboi'
    assert instance_product.manufacturing_date == '10/01/2019'
    assert instance_product.expiration_date == '10/05/2020'
    assert instance_product.serial_number == '123123'
    assert instance_product.storage_instructions == 'embalado'

