class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # A complete valid combination
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add an opening bracket if we still have some left
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add a closing bracket only if it won't make the
            # parentheses invalid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result