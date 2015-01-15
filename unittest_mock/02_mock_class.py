from unittest.mock import Mock

# -----------------------------
# assert_called_with
# assert_called_once_with
# assert_any_call

mock = Mock()
mock.method(1, 2, 3, test='wow')
mock.method.assert_called_with(1, 2, 3, test='wow')
mock.method.assert_called_once_with(1, 2, 3, test='wow')
mock.method(1, 2, 3, test='wow')
# mock.method.assert_called_once_with(1, 2, 3, test='wow')
# 只能调用一次
mock = Mock(return_value=None)
mock(1, 2, arg='thing')
mock('some', 'thing', 'else')
mock.assert_any_call(1, 2, arg='thing')  # 只要调用过

# -----------------------------
# assert_has_calls

from unittest.mock import call
mock = Mock(return_value=None)
mock(1)
mock(2)
mock(3)
mock(4)
calls = [call(2), call(3)]
mock.assert_has_calls(calls)
calls = [call(4), call(2), call(3)]
mock.assert_has_calls(calls, any_order=True)
# 如果any_order=False，则必须按顺序

# -----------------------------
# reset_mock

mock = Mock(return_value=None)
mock('hello')
print(mock.called)
# True
mock.reset_mock()
print(mock.called)
# False

# -----------------------------
# confiture_mock
mock = Mock()
attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
mock.configure_mock(**attrs)
print(mock.method())
# print(mock.other())

# -----------------------------
# called - 是否调用过
mock = Mock(return_value=None)
print(mock.called)
# False
mock()
print(mock.called)
# True

# -----------------------------
# call_count - 调用过的次数
mock = Mock(return_value=None)
print(mock.call_count)
# 0
mock()
mock()
print(mock.call_count)
# 2

# -----------------------------
# return_value
mock = Mock()
mock.return_value = 'fish'
print(mock())
# fish

mock = Mock(return_value=3)
print(mock.return_value)
# 3
print(mock())
# 3

# -----------------------------
# side_effect
mock = Mock()
mock.side_effect = Exception('boom')
# mock()

mock = Mock()
mock.side_effect = [3, 2, 1]
print(mock(), mock(), mock())
# 3 2 1

from unittest.mock import DEFAULT
mock = Mock(return_value=3)
def side_effect(*args, **kwargs):
    return DEFAULT   # 用的是return_value
mock.side_effect = side_effect
print(mock())
# 3

side_effect = lambda value: value+1
mock = Mock(side_effect=side_effect)
print(mock(3))
# 4
print(mock(-8))
# -7

# -----------------------------
# call_args
mock = Mock(return_value=None)
print(mock.call_args)
# None
mock()
print(mock.call_args)
# call()
print(mock.call_args == ())
# True
mock(3, 4)
print(mock.call_args)
# call(3, 4)
print(mock.call_args == ((3, 4),))
# True
mock(3, 4, 5, key='fish', next='woot')
print(mock.call_args)
# call(3, 4, 5, next='woot', key='fish')








