import unittest
from classes.person import Person


class PersonClassTest(unittest.TestCase):
    pass
    # def test_add_person_successfully(self):
    #     my_class_instance = Person()
    #     initial_person_count = len(my_class_instance.all_persons)
    #     staff_neil = my_class_instance.add_person("Neil Armstrong", "staff", "Y")
    #     self.assertTrue(staff_neil)
    #     new_person_count = len(my_class_instance.all_persons)
    #     self.assertEqual(new_person_count - initial_person_count, 1)
    #
    # def test_inputs_are_strings(self):
    #     with self.assertRaises(ValueError, msg='Only strings are allowed as input'):
    #         my_class_instance = Person()
    #         my_class_instance.add_person("Fellow", "Peter", 23)
    #
    # def test_wants_accommodation_default_is_N(self):
    #     my_class_instance = Person()
    #     my_class_instance.add_person("Fellow", "Peter", "Musonye")
    #     result = my_class_instance.all_persons
    #     self.assertEqual(result[0]['fellow']['peter musonye'], 'N', msg="The value of wants_accommodation should be N if it is not provided")
