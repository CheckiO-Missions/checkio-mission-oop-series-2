init_code = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car'?")

Car = USER_GLOBAL['Car']

if not hasattr(Car, "wheels"):
    raise NotImplementedError("Where is 'wheels' attribute of 'Car' class?")

if Car.wheels != 4:
    raise NotImplementedError("'wheels' attribute should be equal 4")

if not "my_second_car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'my_second_car'?")

my_second_car = USER_GLOBAL['my_second_car']

if not isinstance(my_second_car, Car):
    raise Warning("'my_second_car' should be an instance of 'Car' class")

if not hasattr(my_second_car, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'my_second_car' object?")
    
if not isinstance(my_second_car.brand, str):
    raise NotImplementedError("'brand' attribute should be of type 'str'")

if not hasattr(my_second_car, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'my_second_car' object?")

if not isinstance(my_second_car.model, str):
    raise NotImplementedError("'model' attribute should be of type 'str'")
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
    "First": [
        prepare_test(middle_code='''''',
                     test="",
                     answer="")]}