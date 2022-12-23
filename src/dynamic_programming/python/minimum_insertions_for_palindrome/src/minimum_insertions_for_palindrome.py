def minimum_insertions_for_palindrome_basic(s):
    n = len(s)
    if n == 0:
        return 0

    def min_insertions_helper(s, l, h):
        if l > h:
            return float("inf")

        if l == h:
            return 0

        if l == h - 1:
            return 0 if s[l] == s[h] else 1

        if s[l] == s[h]:
            return min_insertions_helper(s, l + 1, h - 1)
        else:
            return 1 + min(
                min_insertions_helper(s, l, h - 1), min_insertions_helper(s, l + 1, h)
            )

    return min_insertions_helper(s, 0, n - 1)


def minimum_insertions_for_palindrome_memo(s):
    n = len(s)
    if n == 0:
        return 0

    def min_insertions_helper(s, l, h, memo):
        if l > h:
            return float("inf")

        if l == h:
            return 0

        if l == h - 1:
            return 0 if s[l] == s[h] else 1

        key = f"{l},{h}"
        if key in memo:
            return memo[key]

        if s[l] == s[h]:
            memo[key] = min_insertions_helper(s, l + 1, h - 1, memo)
        else:
            memo[key] = 1 + min(
                min_insertions_helper(s, l, h - 1, memo),
                min_insertions_helper(s, l + 1, h, memo),
            )
        return memo[key]

    return min_insertions_helper(s, 0, n - 1, dict())


def minimum_insertions_for_palindrome_tab(s):
    n = len(s)

    table = [[0 for x in range(n)] for y in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                table[i][j] = table[i + 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i + 1][j], table[i][j - 1])

    return table[0][-1]
