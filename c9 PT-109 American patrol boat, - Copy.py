# sub_breaker_skeleton.py
import random, re
from collections import Counter

# tiny english word list for scoring
WORDS = {"THE","AND","TO","OF","A","IN","IS","IT","YOU","THAT","HE","WAS","FOR","ON","ARE","AS","WITH","HIS","I"}

def score_text(text):
    text = text.upper()
    words = re.findall(r"[A-Z]+", text)
    score = 0
    for w in words:
        if w in WORDS: score += len(w)
    # penalize non-words length
    return score

def apply_mapping(ct, mapping):
    out=[]
    for ch in ct:
        if ch.isalpha():
            out.append(mapping.get(ch,'?'))
        else:
            out.append(ch)
    return ''.join(out)

def random_mapping():
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    perm = letters[:]
    random.shuffle(perm)
    return {letters[i]:perm[i] for i in range(26)}

def improve_mapping(ct, mapping, max_iters=500):
    best_map = mapping.copy()
    best_score = score_text(apply_mapping(ct,best_map))
    letters=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for _ in range(max_iters):
        a,b = random.sample(letters,2)
        # swap images
        new_map = best_map.copy()
        new_map = new_map.copy()
        # find keys with values a_val and b_val? easier: swap outputs for two plaintext letters
        # Instead swap mapping for two ciphertext letters:
        new_map[a], new_map[b] = new_map[b], new_map[a]
        sc = score_text(apply_mapping(ct,new_map))
        if sc > best_score:
            best_score = sc
            best_map = new_map
    return best_map, best_score

if __name__=="__main__":
    # Example: assumed ciphertext (short)
    ct = "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"
    mapping = random_mapping()
    print("Initial guess:", apply_mapping(ct,mapping))
    m, s = improve_mapping(ct, mapping, max_iters=2000)
    print("Improved:", apply_mapping(ct,m))
    print("Score:", s)
