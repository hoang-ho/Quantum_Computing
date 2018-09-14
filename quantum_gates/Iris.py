from sklearn import datasets
import numpy as np
import random
from sklearn.preprocessing import StandardScaler, normalize


def load_random(n_trainning, attr, class_choice):
    assert n_trainning % 2 == 0, "Please use even number of trainning examples"

    data, target = datasets.load_iris(True)
    data = data[:, attr]
    std_scale = StandardScaler().fit(data)
    data = std_scale.transform(data)
    data = normalize(data)

    list1 = (target == class_choice[0]).nonzero()[0]  # a list of indices of the data where target equals class_choice[0]
    list2 = (target == class_choice[1]).nonzero()[0]  # a list of indices of the data where target equals class_choice[1]
    try:
        idx_test1 = random.choice(list1)
        idx_test2 = random.choice(list2)
        temp1 = list1.tolist()
        temp1.remove(idx_test1)
        list_1 = random.choices(temp1, k=int(n_trainning / 2))
        temp2 = list2.tolist()
        temp2.remove(idx_test2)
        list_2 = random.choices(temp2, k=int(n_trainning / 2))
        sample_train = []

        for idx in list_1:
            data_idx = data[idx, :]
            target_idx = target[idx]
            sample_train.append(np.hstack((data_idx, target_idx)))
        for idx in list_2:
            data_idx = data[idx, :]
            target_idx = target[idx]
            sample_train.append(np.hstack((data_idx, target_idx)))

        sample_train = np.array(sample_train)

        sample_test_1 = data[idx_test1, :]
        sample_test_1 = np.hstack((sample_test_1, target[idx_test1]))

        sample_test_2 = data[idx_test2, :]
        sample_test_2 = np.hstack((sample_test_2, target[idx_test2]))

        sample_test = np.vstack((sample_test_1, sample_test_2))

        return sample_train, sample_test

    except IndexError:
        print("Use smaller training size!")
        return None
