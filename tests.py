import unittest

from utils import (
    find_matched_string,
    calculate_money_changes,
    validate_string_parentheses,
    is_allowed_to_cuty
)


class TestMatchedString(unittest.TestCase):
    
    def test_matched_case_1(self):
        arr1 = ["4", "abcd", "acbd", "aaab", "acbd"]
        self.assertEqual(find_matched_string(arr1), "2 4")

    def test_matched_case_2(self):
        arr2 = [
            "5", "pisang", "goreng", "enak", 
            "sekali", "rasanya"
        ]
        self.assertFalse(find_matched_string(arr2))

    def test_matched_case_3(self):
        arr3 = [
            "11", "Satu", "Sate", "Tujuh", "Tusuk",
            "Tujuh", "Sate", "Bonus", "Tiga",
            "Puluh", "Tujuh", "Tusuk"
        ]
        self.assertEqual(find_matched_string(arr3), "3 5 10")


class TestMoneyChanges(unittest.TestCase):

    def test_calculate_case_1(self):
        expected = (
            99300, 
            [
                "1 lembar 50000", "2 lembar 20000", 
                "1 lembar 5000", "2 lembar 2000", 
                "1 koin 200", "1 koin 100"
            ]
        )
        self.assertEqual(
            calculate_money_changes(700649, 800000),
            expected
        )

    def test_calculate_case_2(self):
        self.assertEqual(
            calculate_money_changes(657650, 600000),
            (False, "kurang bayar")
        )

    def test_calculate_case_3(self):
        expected = (4300, [
            "2 lembar 2000",
            "1 koin 200",
            "1 koin 100"  
        ])
        self.assertEqual(
            calculate_money_changes(575650, 580000),
            expected
        )


class TestValidateParentheses(unittest.TestCase):

    def test_validate_case_1(self):
        parentheses_items = [
            "{{[<>[{{}}]]}}",
            "{<{[[{{[]<{{[{[]<>}]}}<>>}}]]}>}",
            "{{[{<[[{<{<<<[{{{[]{<{[<[[<{{[[[[[<{[{<[<<[[<<{[[{[<<<<<<<[{[{[{{<{[[<{<<<{<{[<>]}>}>>[]>}>]]}>}}]}]}]>>>>>>>]}]]}>>]]>>]>}]}>]]]]]}}>]]>]}>}}}}]>>>}>}]]>}]}}",
            "[<{<{[{[{}[[<[<{{[<[<[[[<{{[<<<[[[<[<{{[<<{{<{<{<[<{[{{[{{{{[<<{{{<{[{[[[{<<<[{[<{<<<>>>}>]}]>>>}]]]}]}>}}}>>]}}}}]}}]}>]>}>}>}}>>]}}>]>]]]>>>]}}>]]]>]>]}}>]>]]]}]}>}>]",
            "[[{[[<{{{{[[[<[{[[<{{{{[{[{[[[<<{<{[{<<<[[<[{[<{{[{[<[[<<[{<<[[[{<[{[[{{<<>[<<{{<<{[[[<{}{[{{{[[{{[[<[{}]>]]}}]]}}}]}>]]]}>>}}>>]>}}]]}]>}]]]>>}]>>]]>]}]}}>]}]>]]>>>}]}>}>>]]]}]}]}}}}>]]}]>]]]}}}}>]]}]]",
            "[{}<>]"
        ]
        for parentheses in parentheses_items:
            self.assertTrue(validate_string_parentheses(parentheses))

    def test_validate_case_2(self):
        parentheses_items = [
            "]",
            "][",
            "[>]",
            "[>",
            "{{[<>[{{}}]]}}]",
            "{<{[[{{[]<{[{[]<>}]}}<>>}}]]}>}",
            "{{[{<[[{<{<<<[{{{[]{<{[<[[<{{[[[[<{[{<[<<[[<<{[[{[<<<<<<<[{[{[{{<{[[<{<<<{<{[<>]}>}>>[]>}>]]}",
            ">}}]}]}]>>>>>>]}]]}>>]]>>]>}]}>]]]]]}}>]]>]}>}}}}]>>>}>}]]>}]}}",
            "[<{<{[{[{}[[<[<{{[<[<[[[<{{[<<<[[[<[<{{[<<{{<{<{<[<{[{{[{{{{[<<{{{<{[{[[[{<<<[{[<{<<>>[]}]>>>}]]]}]}>}}}>>]}}}}]}}]}>]>}>}>}}>>]}}>]>]]]>>>]}}>]]]>]>]}}>]>]]]}]}>}>]",
            "[{}<[>]"
        ]
        for parentheses in parentheses_items:
            self.assertFalse(validate_string_parentheses(parentheses))


class TestAllowedToCuti(unittest.TestCase):

    def test_allowed_case_1(self):
        self.assertEqual(
            is_allowed_to_cuty(7, "2021-05-01", "2021-07-05", 1),
            (False, "Karena  belum 180 hari sejak tanggal join karyawan")
        )

    def test_allowed_case_2(self):
        self.assertEqual(
            is_allowed_to_cuty(7, "2021-05-01", "2021-11-05", 3),
            (False, "Karena hanya boleh mengambil 1 hari cuti")
        )

    def test_allowed_case_3(self):
        self.assertTrue(is_allowed_to_cuty(7, "2021-01-05", "2021-12-18", 1))

    def test_allowed_case_4(self):
        self.assertTrue(is_allowed_to_cuty(7, "2021-01-05", "2021-12-18", 3))


if __name__ == "__main__":
    unittest.main()
