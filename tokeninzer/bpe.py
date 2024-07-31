from collections import Counter

word_freqs = {
    "たのしい": 6,
    "たのしさ": 2,
    "うつくしい": 4,
    "うつくしさ": 1
}

vocab = sorted(set([char for word in word_freqs for char in word]))

#print(vocab)

splits = {word: [char for char in word] for word in word_freqs}

print(splits)

def compute_most_frequent_pair(
  splits: dict[str, list[str]],
) -> tuple[str, str]:
    """
    最も頻度の高い隣接するサブワードの組を計算する
    """
    pair_freqs = Counter()
    for word, freq in word_freqs.items():
        split = splits[word]
        #print(word,split)
        # すべての隣接したサブワードの組を処理
        for i in range(len(split) - 1):
            pair = (split[i], split[i + 1])
            # サブワードの組の頻度に単語の頻度を加算
            pair_freqs[pair] += freq
    pair, _ = pair_freqs.most_common(1)[0]
    #print(pair_freqs.most_common(1))
    return pair

def merge_pair(
  target_pair: tuple[str, str],
  splits: dict[str, list[str]]
) -> dict[str, list[str]]:
    """
    サブワードの組を結合する
    """
    l_str, r_str = target_pair
    print(l_str, r_str)
    for word in word_freqs:
        split = splits[word]
        i = 0
        while i < len(split) -1:
            # サブワードの組が結合対象と一致したら結合
            if split[i] == l_str and split[i + 1 ] == r_str:
                split = split[:i] + [l_str + r_str ] + split[i + 2 :]
            i += 1
        splits[word] = split
    return splits

for step in range(9):
    # もっとも頻度の高い隣接するサブワードの組を計算
    target_pair = compute_most_frequent_pair(splits)
    #print(target_pair)
    # サブワードの組を結合
    splits = merge_pair(target_pair, splits)
    #vocab.append(target_pair)

#print(splits)
#print(m_splits)
