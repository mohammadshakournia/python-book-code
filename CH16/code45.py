# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH16 / code45.py  |  الگوریتم‌های یادگیری ماشین نظارت شده
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=42
)

tree = DecisionTreeClassifier(max_depth=4, random_state=0)
tree.fit(X_train, y_train)

print("Feature importances:\n{}".format(tree.feature_importances_))

def plot_feature_importances_cancer(model):
    n_features = cancer.data.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align="center")
    plt.yticks(np.arange(n_features), cancer.feature_names)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")

plot_feature_importances_cancer(tree)
plt.show()
