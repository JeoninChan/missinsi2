height = Element("height").value
weight = Element("weight").value
want_grade = Element("start-1")
result = Element("result")
height = float(height)
weight = float(weight)
bmi = ((weight/height)/height)/10000
grade = 1
def 의무군인(*args):
    if height <= 140:
        grade = 6
        result.element.innerText="당신은 6등급입니다.!"



