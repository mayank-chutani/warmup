def resolve_range(current_range):
    if (1 <= len(current_range) <= 2):
        return [str(d) for d in current_range]
    else:
        return [str(current_range[0]) + '-' + str(current_range[-1])]


def solution(array):
    result = []
    current_range = []
    for i in range(len(array)):
        if len(current_range) == 0:
            current_range.append(array[i])
            continue

        if (array[i] == array[i-1] + 1):
            current_range.append(array[i])
        else:
            resolved_range = resolve_range(current_range)
            result.extend(resolved_range)
            current_range = []
            current_range.append(array[i])
    if len(current_range) > 0:
        result.extend(resolve_range(current_range))
    return ','.join(result)


if __name__ == '__main__':
    print(solution([-2, -1, 0, 1, 3, 4]))
