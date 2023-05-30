init_code = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car' class?")

Car = USER_GLOBAL['Car']

if not "my_car" in USER_GLOBAL:
    raise NotImplementedError("Dude, where is 'my_car'?")

my_car = USER_GLOBAL['my_car']

if not isinstance(my_car, Car):
    raise TypeError("'my_car' should be an instance of 'Car' class")


if not hasattr(Car, "wheels"):
    raise AttributeError("Where is 'wheels' attribute of 'Car' class?")

if not hasattr(Car, "doors"):
    raise AttributeError("Where is 'doors' attribute of 'Car' class?")

if Car.wheels != "four":
    raise ValueError("'wheels' attribute should be equal 'four'")
    
if Car.doors != 4:
    raise ValueError("'doors' attribute should be equal 4")
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "Basics": [
        prepare_test(middle_code='''''',
                     test="",
                     answer="")]
    }
