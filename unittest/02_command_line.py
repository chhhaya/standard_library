# 命令行接口
# 1. 指定模块
# python -m unittest 01_basic
# 2. 指定类
# python -m unittest 01_basic.TestSequenceFunctions
# 3. 指定具体的测试函数
# python -m unittest 01_basic.TestSequenceFunctions.test_shuffle
# 4. 带—v的
# python -m unittest -v 01_basic

# Discovery
# -v: verbose output
# -s: start directory(.)
# -p: pattern(test*.py)
# -t: top level directory
# python -m unittest discover -s project_directory -p '*_test.py'
# python -m unittest discover project_directory '*_test.py'


