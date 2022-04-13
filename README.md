<!--
 * @Author: your name
 * @Date: 2022-04-13 21:32:08
 * @LastEditTime: 2022-04-13 21:43:41
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: /test_pytest/README.md
-->
# Test unit test

This is a project about how to use the unit test 

In the lib file, we creat the module greet. Then In the tests dir, we want to couduct the unit test. Note that the test functions are begin with "test"

```
def test_print():
    n = print_num(5)
    assert n == 5

```

Then we use the pytest to conduct the unit test.

```
pytest

```
or 

```
python -m pytest tests/test_greet_sum.py
```

we can also use the VSCODE plugin to help us conduct unit test. 


