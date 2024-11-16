# s = "ABABABABABACABABACABAD"
# p = "ABABACABA"
# 를 가지고 이해하면 쉽습니다.
failure_func = {0:0}
i = 0
j = 1
while j < len(p):
	if p[i] == p[j]:
		failure_func[j] = i + 1
		j += 1
		i += 1
	else:
		if i == 0:
			failure_func[j] = 0
			j += 1
		else:
			# `p[i - 1] == p[j - 1]`, `p[i - 2] == p[j - 2]`, ..., `p[0] == p[j - i - 2]`가 성립할 것이고 `p[i] != p[j]`이므로 `failure_func[j]`는 `i + 1`이 될 수 없습니다. 따라서 `i`를 더 작게 만들어서 failure_func[j]`의 값을 찾아야 합니다. 이 때, `p[:i]`은 길이 `failure_func[i - 1]`만큼의 Prefix와 Suffix가 같습니다. 이 말은 즉, `p[failure_func[i - 1]] != p[i - 1]`임을 의미합니다. 그런데 앞서 살펴봤듯이 `p[i - 1] == p[j - 1]`이므로 `p[failure_func[i - 1]] != p[j - 1]`입니다. 따라서 `failure_func[j]`는 `failure_func[i - 1] + 2`가 될 수 없고 가능한 최댓값은 `failure_func[i - 1] + 1`입니다. 그러므로 `failure_func[j]`가 `failure_func[i - 1] + 1`과 같을 수 있는지 알아내기 위해 `i = failure_func[i - 1]`을 대입하고 다음 스텝에서 `p[i] == p[j]`를 만족하는지 확인하는 것입니다.
			i = failure_func[i - 1]
			
i = 0
j = 0
match = list()
while i < len(s):
	if s[i] == p[j]:
		if j == len(p) - 1:
			match.append(i - len(p) + 1)
			i += 1
			j = failure_func[len(p) - 1]
		else:
			i += 1
			j += 1
	else:
		if j == 0:
			i += 1
		else:
			j = failure_func[j - 1]
