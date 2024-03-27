# Пример использования
num_samples = 1000  # количество сэмплов
num_features = 5  # количество параметров (признаков)
anomaly_level = 0.1  # уровень аномалий

data, labels = generate_dataset(num_samples, num_features, anomaly_level)

# Вывод первых 10 сэмплов и их меток
print("Примеры данных:")
print(data)
print("Метки аномалий:")
print(labels)

