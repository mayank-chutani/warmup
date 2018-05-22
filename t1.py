import re

def dedup(input_str: str, chunk_size: int) -> str:
    print(input_str)
    # Write your code here
    chunk = input_str[:chunk_size]
    deduplicated_string = chunk + re.sub(r'{}+'.format(chunk), '|', input_str)

    redup = deduplicated_string[chunk_size:].replace('|', deduplicated_string[:chunk_size])
    assert(len(deduplicated_string) < len(input_str))
    assert(input_str == redup)


if __name__ == '__main__':
    dedup('aaaaaaaaaabbbbbbbbbbaaaaaaaaaabbbbbbbbbbaaaaaaaaaabbbbbbbbbbaaaaaaaaaabbbbbbbbbbaaaaaaaaaabbbbbbbbbbaaaaaaaaaabbbbbbbbbbcccccccccc', 10)
