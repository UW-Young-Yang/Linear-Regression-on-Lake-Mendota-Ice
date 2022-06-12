from symtable import Symbol
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sympy import beta

if __name__ == '__main__':
    csv_file = sys.argv[1]

    # Q2
    df = pd.read_csv(csv_file)
    plt.plot(df['year'], df['days'])
    plt.xlabel('Year')
    plt.ylabel('Number of frozen days')
    plt.savefig("plot.jpg")

    # Q3
    X = np.insert(np.array(df['year']).reshape(-1, 1), 0, 1, axis=1)
    #X = np.stack([np.ones(len(df['year'])), df['year']], axis=1)
    print("Q3a:")
    print(X)
    Y = np.array(df['days'])
    print("Q3b:")
    print(Y)
    Z = X.T @ X
    print("Q3c:")
    print(Z)
    I = np.linalg.inv(Z)
    print("Q3d:")
    print(I)
    PI = I @ X.T
    print("Q3e:")
    print(PI)
    hat_beta = PI @ Y.reshape(-1, 1)
    print("Q3f:")
    print(hat_beta)

    # Q4
    B0 = hat_beta[0, 0]
    B1 = hat_beta[1, 0]
    y_test = B0 + B1 * 2021
    print("Q4: " + str(y_test))

    # Q5
    if B1 < 0:
        symbol = '<'
    elif B1 == 0:
        symbol = '='
    else:
        symbol ='>'
    print("Q5a: " + symbol)
    short_answer = 'The symbol stands for the change trend of frozen days \
with the increase of years, so this sign shows that the number of the frozen \
days of Lake Mendota is decreasing as the the number of years increases'
    print("Q5b: " + short_answer)

    #Q6
    x_star = -B0 / B1
    print("Q6a: " + str(x_star))
    answer = 'It is a compelling prediction, because according to the sign \
calculated above, we can know that the freezing days are decreasing, so Mendota \
lake will no longer freeze in the future'
    print("Q6b: " + answer)
