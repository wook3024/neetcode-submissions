class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        filtered_str = ""

        def is_char(char):
            return ('a' <= lower_char <= 'z') or ('0' <= lower_char <= '9')

        for char in s:
            lower_char = char.lower()
            if not is_char(lower_char):
                continue
            filtered_str += lower_char

        print(filtered_str)

        str_len = len(filtered_str)
        mid = str_len // 2
        
        second_idx = str_len - 1
        for idx in range(mid):
            first = filtered_str[idx]
            second = filtered_str[str_len - idx - 1]
            print(first, second, mid, second_idx, filtered_str[mid])
            
            if first != second:
                print(f"first: {first}, second: {second} {second_idx}")
                return False

            second_idx -= 1
        
        return True

        