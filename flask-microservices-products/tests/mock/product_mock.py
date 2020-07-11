from app.utils.number_utils import NumberUtils
from app.utils.string_utils import StringUtils


def get_mock_product(
        name=f'Produto {StringUtils.get_random_string()}',
        description='Lorem ipsum dolor sit amet',
):
    return {
        'name': name,
        'description': description,
        'price': NumberUtils.get_random_number(max=100)
    }
