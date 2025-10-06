from collections import Counter,deque
from functools import  lru_cache
import json


class BPETokenizerSimple:
    def __init__(self):
        self.vocab = {}
        self.inverse_vocab = {}
        self.bpe_merges = {}
        self.bpe_ranks = {}

    @staticmethod
    def find_freq_pair(token_ids, mode="most"):
        pairs = Counter(zip(token_ids, token_ids[1:]))

        if not pairs:
            return None

        if mode == "most":
            return max(pairs.items(), key=lambda x: x[1])[0]
        elif mode == "least":
            return min(pairs.items(), key=lambda x: x[1])[0]
        else:
            raise ValueError("Invalid mode. Choose 'most' or 'least'.")

    @staticmethod
    def replace_pair(token_ids, pair_id, new_id):
        dq = deque(token_ids)
        replaced = []

        while dq:
            current = dq.popleft()
            if dq and (current, dq[0]) == pair_id:
                replaced.append(new_id)
                # Remove the 2nd token of the pair, 1st was already removed
                dq.popleft()
            else:
                replaced.append(current)
        return replaced

    def train(self, text, vocab_size, allowed_special={"<|endoftext|>"}):
        processed_text1 = []
        for i, char in enumerate(text):
            #print("char is:",char)
            if char == " " and i != 0:
                processed_text1.append("Ġ")
            if char != " ":
                processed_text1.append(char)
                #print(processed_text1)
            processed_text = "".join(processed_text1)
            #print("processed Text is :",processed_text)

        unique_chars = [chr(i) for i in range(256)]
        unique_chars.extend(
            char for char in sorted(set(processed_text))
            if char not in unique_chars
        )
        if "Ġ" not in unique_chars:
            unique_chars.append("Ġ")
        #print(unique_chars)

        self.vocab = {i: char for i, char in enumerate(unique_chars)}
        self.inverse_vocab = {char: i for i, char in self.vocab.items()}

        if allowed_special:
            for token in allowed_special:
                if token not in self.inverse_vocab:
                    new_id = len(self.vocab)
                    self.inverse_vocab[token] = new_id
                    self.vocab[new_id] = token

        print(self.vocab)
        token_ids = [self.inverse_vocab[char] for char in processed_text]
        # absprint(token_ids)
        #print(len(self.vocab))
        for new_id in range(len(self.vocab), vocab_size):
            pair_id = self.find_freq_pair(token_ids, mode="most")
            if pair_id is None:
                break
            token_ids = self.replace_pair(token_ids, pair_id, new_id)
            self.bpe_merges[pair_id] = new_id


if __name__ == "__main__":
    bpetoknizer = BPETokenizerSimple()
    bpetoknizer.train(text="The fox is out in the wild", vocab_size=1000, allowed_special={"<|endoftext|>"})
