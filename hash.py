import matplotlib.pyplot as plt

file_path = "hw2_data.txt"
with open(file_path, "r") as file:
    words = file.read().splitlines()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

unique_word_counts = 0
for word in word_counts:
    unique_word_counts += 1

print("不重複的英文字數量:", unique_word_counts)
print("每個英文字的出現次數:")
print(dict(word_counts))

sorted_items = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
sorted_words = [item[0] for item in sorted_items]
sorted_counts = [item[1] for item in sorted_items]
plt.figure(figsize=(10, 6))
plt.bar(sorted_words, sorted_counts)
plt.show()  