
import numpy as np

def generate_dataset(num_samples, num_features, anomaly_level=0.1):
    """
    Генерирует набор данных с заданным количеством параметров и уровнем аномалий.

    :param num_samples: количество сэмплов в наборе данных
    :param num_features: количество параметров (признаков)
    :param anomaly_level: уровень аномалий в данных (от 0 до 1)
    :return: набор данных и метки аномалий
    """
    # Генерация нормальных данных
    normal_data = np.random.rand(num_samples, num_features)
    
    # Генерация аномалий
    num_anomalies = int(num_samples * anomaly_level)
    anomaly_indices = np.random.choice(num_samples, num_anomalies, replace=False)
    
    anomalies = np.random.rand(num_anomalies, num_features) * 10  # просто для примера, можно задать другой способ генерации аномалий
    
    # Вставка аномалий в набор данных
    for i, idx in enumerate(anomaly_indices):
        normal_data[idx] = anomalies[i]
    
    # Создание меток аномалий (1 - аномалия, 0 - нормальный сэмпл)
    anomaly_labels = np.zeros(num_samples)
    anomaly_labels[anomaly_indices] = 1
    
    return normal_data, anomaly_labels

