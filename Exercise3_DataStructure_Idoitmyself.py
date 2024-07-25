sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
start = 0
end = 3
for i in range(1, 4):
    chunk = sample_list[start:end]
    print("Chunk", i, chunk)
    chunk.reverse()
    print("After reversing it", chunk)
    start = end
    end += 3




























