file_path = "hw2_data.txt"
with open(file_path, "r") as file:
    words = file.read().splitlines()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

unique_word_count = 0
for word in word_counts:
    unique_word_count += 1

print("不重複的英文字數量:", unique_word_count)
print("每個英文字的出現次數:")
print(dict(word_counts))