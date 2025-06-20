from decimal import Decimal


class NumericStringComparator:
    def __init__(self, a: str, b: str):
        self.a = a
        self.b = b

    def compare(self) -> int:
        return self._route_to_proper_compare_function(self.a, self.b)

    @staticmethod
    def _compare_numeric_strings_simple(a: str, b: str) -> int:
        a = a.lstrip('0') or '0'
        b = b.lstrip('0') or '0'

        if len(a) != len(b):
            return 1 if len(a) > len(b) else -1
        return (a > b) - (a < b)

    @staticmethod
    def _compare_numeric_strings_with_decimals(a: str, b: str) -> int:
        a_parts = a.split(".")
        b_parts = b.split(".")

        a_pre = a_parts[0].lstrip('0') or '0'
        b_pre = b_parts[0].lstrip('0') or '0'

        # Compare whole number parts
        if len(a_pre) != len(b_pre):
            return 1 if len(a_pre) > len(b_pre) else -1
        if a_pre != b_pre:
            return (a_pre > b_pre) - (a_pre < b_pre)

        # Compare decimal parts
        a_post = a_parts[1] if len(a_parts) > 1 else ''
        b_post = b_parts[1] if len(b_parts) > 1 else ''

        max_len = max(len(a_post), len(b_post))
        a_post = a_post.ljust(max_len, '0')
        b_post = b_post.ljust(max_len, '0')

        return (a_post > b_post) - (a_post < b_post)

    @classmethod
    def _route_to_proper_compare_function(cls, a: str, b: str) -> int:
        # Handle negatives
        if a.startswith('-') and b.startswith('-'):
            return -cls._route_to_proper_compare_function(a[1:], b[1:])
        elif a.startswith('-'):
            return -1
        elif b.startswith('-'):
            return 1

        # Handle decimal or whole number
        if '.' in a or '.' in b:
            return cls._compare_numeric_strings_with_decimals(a, b)
        else:
            return cls._compare_numeric_strings_simple(a, b)

number_set = NumericStringComparator("0982345", "-987425987.0")
print(number_set.compare())
