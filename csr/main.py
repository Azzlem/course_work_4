from vacancies import Vacancies, Vacancies_hh

a = Vacancies("bla bla vla", "HH")
b = Vacancies_hh("a", "HH", 10000)

# Test1
assert a.url == "bla bla vla"
assert a.platform == "HH"
# a.platform = "99"
assert b.url == "a"
assert b.platform == "HH"
# b.platform = 2
assert b.pay == 10000
print(repr(a))
print(repr(b))
