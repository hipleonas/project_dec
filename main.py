def token_ttl(ttl, queries):
    token_map = {}  # token_id -> expire_time
    result = []

    for query in queries:
        parts = query.split()
        op = parts[0]

        if op == "generate":
            token_id = parts[1]
            current_time = int(parts[2])
            token_map[token_id] = current_time + ttl

        elif op == "renew":
            token_id = parts[1]
            current_time = int(parts[2])

            # chỉ gia hạn nếu token còn hạn
            if token_id in token_map and token_map[token_id] > current_time:
                token_map[token_id] = current_time + ttl

        elif op == "count":
            current_time = int(parts[1])

            count = 0
            for expire_time in token_map.values():
                if expire_time > current_time:
                    count += 1

            result.append(count)

    return result


# ================= TEST =================
if __name__ == "__main__":
    ttl = 5
    queries = [
        "generate aaa 1",
        "generate bbb 2",
        "renew aaa 3",
        "count 4",
        "renew bbb 8",
        "renew aaa 10",
        "count 10",
        "count 15"
    ]

    print(token_ttl(ttl, queries))  # Output: [2, 0, 0]