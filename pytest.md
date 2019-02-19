# Pytest Guide

## installation
in your console
```bash
$ pip install -U pytest
```

#### HOW to write Test code
##### 1. test in your file
> 보통 파일명으로 - 를 잘 사용하지 않는다.
[PEP 8 summary](https://hashcode.co.kr/questions/489/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%B3%80%EC%88%98%ED%95%A8%EC%88%98-%EC%9D%B4%EB%A6%84%EC%9D%84-%EC%A7%80%EC%9D%84-%EB%95%8C-%EA%B7%9C%EC%B9%99%EC%9D%B4-%EC%9E%88%EB%82%98%EC%9A%94)

아래 코드와 같이, 실행 파일 내에서 테스트 코드를 돌릴 수 있다.
(다만, 파일명이 test_*.py나 *_test.py여야 함.)
```python
# content of test_sample.py
def func(x):
    return x+1
   
def test_answer():
    assert func(3) == 5 # FAIL
```
- assert 키워드로 test의 예상값과 결과값을 확인할 수 있음.

##### 2. test with existing code
###### HOW to use import
[jumpToPython](https://wikidocs.net/1418) 참고하여 만듦.

1 ) Basic Usage
```python
from {package_name.module_name} import {function/class/...} 
```
{module_name}에 정의된 {기능/변수/클래스}를 사용하겠다.

- packages (directory)
  - 파이썬 모듈을 계층적으로 관리할 수 있게 해줌. 
  - , \_\_init__.py 파일이 있어야 해당 디렉토리가 패키지의 일부임을 알려줌.
- modules (.py file)
  - 함수나 변수 또는 클래스들을 모아 놓은 파일.
  - 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만들어진 파이썬 파일.
 
2 ) 
```python
# from {currnetDIR.subDIR1.subDIR2} import {importModuleName}
from program import p001_abs

def check():
    if (p001_abs.abs_sign(-1) == 1):
        return True
```
program 패키지 하위의 p001_abs 모듈을 사용하겠다.
- 사용 시엔, p001_abs.{모듈에서 정의한 function/class/variable} 이렇게 사용해야 한다.

3 ) 
```python
from program.p001_abs import abs_sign

def check():
    if abs_sign(-1) == 1:
        return True
```
'program' 패키지의 'p001_abs' 모듈을 불러와 abs_sign 함수를 사용할 것임을 암시.

+)
```python
# Relative path (상대경로를 이용할 경)
from .. # parent DIR
from .  # current DIR
```

## Test Result
pytest 실행하면, 결과는 아래와 같다.
```bash
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-4.x.y, py-1.x.y, pluggy-0.x.y
cachedir: $PYTHON_PREFIX/.pytest_cache
rootdir: $REGENDOC_TMPDIR, inifile:
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:5: AssertionError
========================= 1 failed in 0.12 seconds =========================

```
pytest 실행시 현 디렉토리부터 하위 디렉토리까지 test_*.py나 *_test.py를 실행시킴
