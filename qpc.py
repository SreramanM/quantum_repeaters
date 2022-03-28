import math
import numpy as np
import qec
import matplotlib.pyplot as plt

def qber(px_correct, px_incorrect, pz_correct, pz_incorrect, num):
    value_a_x = px_correct+px_incorrect
    value_b_x = px_correct-px_incorrect
    value_a_z = pz_correct+pz_incorrect
    value_b_z = pz_correct-pz_incorrect
    error_x = 0.5-0.5*((value_b_x/value_a_x)**num)
    error_z = 0.5-0.5*((value_b_z/value_a_z)**num)
    qber = (error_x + error_z)*0.5
    return qber


def key_rate(qber, p_success, num):
    if qber==0:
        key_rate = p_success**num
        return key_rate
    elif qber!=0:
        key_rate = (p_success**num)*(max(1-2*((-qber)*math.log(qber, 2) - (1-qber)*math.log(1-qber, 2)), 0))
        return key_rate


def cost_function(n, m, key_rate, l_rep):
    if key_rate < 10**(-5):
        key_rate = 10**(-5)
    cost = 2*m*n/(key_rate*l_rep)
    return cost


epg = float(input('Enter gate error rate '))
epm = float(input('Enter measurement error rate '))
max_m = 11
max_n = 11
max_l_rep = 10

cost = [0 for i in range(10)]
axes = [0 for i in range(10)]
print('Calculating the cost coefficient for the one-way quantum repeater scheme with QPC')
for k in range(10):
    var_2 = [1e5 for i in range(max_l_rep)]
    L = k * 100
    for l_rep in range(1,max_l_rep):
        loss = 1 - math.exp (-l_rep / 20)
        num = math.floor (L / l_rep)
        var_1 = [[1e5 for i in range (max_n)] for j in range (max_m)]
        for i in range(2,max_n):
            for j in range(2,max_m):
                px_correct,px_incorrect,pz_correct,pz_incorrect,p_success = qec.qpc (epg,epm,loss,i,j)
                qber_val = qber (px_correct,px_incorrect,pz_correct,pz_incorrect,num)
                key_rate_val = key_rate (qber_val,p_success,num)
                var_1[i][j] = cost_function (i,j,key_rate_val,l_rep)
        var_2[l_rep] = np.amin(var_1)
    cost[k] = np.amin(var_2)
    axes[k] = L
plt.plot(axes, cost)
plt.xlabel('Distance(km)')
plt.ylabel('Cost coefficient (qubits/sbit/s)')
plt.show()

