from unittest.mock import MagicMock
from product import ProductionClass

thing = ProductionClass()
thing.method = MagicMock(return_value=4)
thing.method(3, 4, 5, key='value')
# 大概是跟上面那个调用相比较，看是否一样，如果不一样就Error
thing.method.assert_called_with(3, 4, 5, key='value')
# OK
# thing.method.assert_called_with(3, 4, 6, key='value')
# AssertionError: Expected call: mock(3, 4, 6, key='value')
# Actual call: mock(3, 4, 5, key='value')

############################################################

from unittest.mock import Mock
# 报异常的side_effect
mock = Mock(side_effect=KeyError('foo'))
# mock()

# 自定义的情况
values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]
mock.side_effect = side_effect
print(mock('a'), mock('b'), mock('c'))
# 1 2 3

# 列表的情况
mock.side_effect = [5, 4, 3, 2, 1]
print(mock(), mock(), mock())
# 5 4 3

############################################################

from unittest.mock import patch
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, 2, 3)
mock_method.assert_called_once_with(1, 2, 3)
# OK
# mock_method.assert_called_once_with(1, 2, 4)
# AssertionError: Expected call: method(1, 2, 4)
# Actual call: method(1, 2, 3)

############################################################

# patch.dict的作用是改了foo的内容后，测试完后能恢复到之前
foo = {'key': 'value'}
original = foo.copy()
with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    assert foo == {'newkey': 'newvalue'}
assert foo == original

############################################################

mock = MagicMock()
mock.__str__.return_value = 'foobarbaz'
print(str(mock))
# foobarbaz
mock.__str__.assert_called_with()  # 检查该函数是否被调用过

############################################################

# TODO 不懂
from unittest.mock import create_autospec
def function(a, b, c):
    pass
mock_function = create_autospec(function, return_value='fishy')
print(mock_function(1, 2, 3))
# fishy
mock_function.assert_called_once_with(1, 2, 3)
# mock_function('wrong arguments')
# TypeError: 'b' parameter lacking default value





























