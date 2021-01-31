class Employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, incr=5000):
        self.salary = self.salary + incr
        return self.salary
        

if __name__ == '__main__':
    employee_aaa = Employee('AAA','BBB',10000)
    employee_aaa.give_raise(7000)
    print(f"New salary of employee {employee_aaa.first.title()} is {employee_aaa.salary}.")

    employee_ccc = Employee('CCC','DDD',4000)
    employee_ccc.give_raise()
    print(f"New salary of employee {employee_ccc.first.title()} is {employee_ccc.salary}.")


