import unittest
from models_oop import Calculator, Contacts, Grade

class TestCalculator(unittest.TestCase):

    def test_calculator(self):
        cal = Calculator()
        cal.num1 = 5
        cal.num2 = 8
        self.assertEqual(cal.divice(), 1.0)
        self.assertEqual(cal.add(), 10)
        self.assertEqual(cal.mulitple(), 25)
        self.assertEqual(cal.subtract(), 0)

class TextContacts(unittest.TestCase):
    def test_set_contact(self):
        ls = []
        ls.append(Contacts.set_contact('장인성', '010-4007-3771', 'roomate1245@gamail.com', 'Paris'))
        ls.append(Contacts.set_contact('홍길동', '010-5856-7849', 'lionx3@naver.com', 'Seoul'))
        ls.append(Contacts.set_contact('이순신', '010-8485-6669', 'wkd1598@nate.com', 'chine'))
        ls = Contacts.get_contact(ls)
        self.assertEqual(ls[0].name, '장인성')

    def test_del_contact(self):
        ls = []
        ls.append(Contacts.set_contact('Tom', '010-1234', 'tom@test.com', 'Seoul'))
        ls.append(Contacts.set_contact('Jane', '010-3334', 'jane@test.com', 'Incheon'))
        ls.append(Contacts.set_contact('Kim', '010-7734', 'kim@test.com', 'Busan'))
        ls = Contacts.del_contact(ls, 'Tom')
        print([x.to_string() for x in ls])
        self.assertEqual(len(ls), 2)

class TextGrade(unittest.TestCase):
    def test_avg(self):
        grade = Grade('Han',60,80,70)
        # print(grade.return_grade())
        self.assertEqual(grade.name, 'Han')
        self.assertEqual(grade.return_grade(), 'C')

if __name__ == '__main__':
    unittest.main()

