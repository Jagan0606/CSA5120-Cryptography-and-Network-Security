# q29_sha3_lanes_sim.py
# Simulate Keccak lane marking (simplified, ignoring permutation)
RATE = 1024
CAPACITY = 576
LANE_SIZE = 64  # Keccak-f[1600]
# number of lanes = 25; total bits = 25*64 = 1600
lanes = [0]*25  # 0=zero lane, 1=nonzero lane
# suppose first message block has every lane nonzero (as given)
message_lanes_nonzero = [1]*25

# absorption (XOR): capacity lanes will be set to nonzero if message lane nonzero
for i in range(25):
    if message_lanes_nonzero[i]:
        lanes[i] = 1

print("After one absorption, number of nonzero lanes:", sum(lanes))
print("All capacity lanes nonzero? ->", sum(lanes) == 25)
