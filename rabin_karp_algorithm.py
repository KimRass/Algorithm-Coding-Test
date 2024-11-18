# If `d` is too small, hash collision easily occurs. So `d` should be at least larger than the number of characters in both `s` and `p`. 또한 `a`가 `p`의 원시근이 아닐 경우에도 Hash collision이 쉽게 일어납니다.
d = 302
# Choose a prime number for `q` in such a way that we can perform all the calculations with single-precision arithmetic.
q = 1000000007
h = 1
for i in range(len(p) - 1):
    h = (h*d)%q

hash_s = 0
hash_p = 0
for i in range(len(p)):
    hash_s = (d*hash_s + ord(s[i]))%q
    hash_p = (d*hash_p + ord(p[i]))%q

j = 0
match = list()
while j < len(s) - len(p):
    if hash_s == hash_p:
        # Check character by character.
        for k in range(len(p)):
            if s[k + j] != p[k]:
                break
        else:
            match.append(j)
    hash_s = ((hash_s - ord(s[j])*h)*d + ord(s[j + len(p)]))%q
    j += 1
