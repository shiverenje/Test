def calculate_tax(salary_list):
    empty_list = {}
    check = (int, float)
    if isinstance(salary_list, dict):
        for individual_salary in salary_list:
            each_salary = salary_list[individual_salary]
            if isinstance(each_salary, check):
                if each_salary <= 1000:
                    tax_holder = 0
                    empty_list[individual_salary] = tax_holder
                elif 1001 <= each_salary <= 10000:
                    tax1 = 0 * 1000
                    tax2 = 0.1 * (each_salary - 1000)
                    tax_holder = tax1 + tax2
                    empty_list[individual_salary] = tax_holder
                elif 10001 <= each_salary <= 20200:
                    tax1 = 0 * 1000
                    tax2 = 0.1 * 9000
                    tax3 = 0.15 * (each_salary - 10000)
                    tax_holder = tax1 + tax2 + tax3
                    empty_list[individual_salary] = tax_holder
                elif 20201 <= each_salary <= 30750:
                    tax1 = 0 * 1000
                    tax2 = 0.1 * 9000
                    tax3 = 0.15 * 10200
                    tax4 = 0.2 * (each_salary - 20200)
                    tax_holder = tax1 + tax2 + tax3 + tax4
                    empty_list[individual_salary] = tax_holder
                elif 30751 <= each_salary <= 50000:
                    tax1 = 0 * 1000
                    tax2 = 0.1 * 9000
                    tax3 = 0.15 * 10200
                    tax4 = 0.2 * 10550
                    tax5 = 0.25 * (each_salary - 30750)
                    tax_holder = tax1 + tax2 + tax3 + tax4 + tax5
                    empty_list[individual_salary] = tax_holder
                else:
                    tax1 = 0 * 1000
                    tax2 = 0.1 * 9000
                    tax3 = 0.15 * 10200
                    tax4 = 0.2 * 10550
                    tax5 = 0.25 * 19250
                    tax6 = 0.3 * (each_salary - 50000)
                    tax_holder = tax1 + tax2 + tax3 + tax4 + tax5 + tax6
                    empty_list[individual_salary] = tax_holder
            else:
                raise ValueError('Allow only numeric input')

        return empty_list
    else:
        raise ValueError('The provided input is not a dictionary')


val = {"James": 20500}
val2 = {"James": 20500, "Mary": 500, "Evan": 70000}
res = calculate_tax(val2)
print(res["James"])
print(res)
