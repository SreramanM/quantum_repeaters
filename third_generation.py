from functools import reduce
import operator as op
import math
from itertools import count
import numpy as np
import qec


input_list = input('Choose one of the following codes 1) QPC, 2) QRSC(single qubit), 3) QRSC (multiple qubits)')
print(input_list)

if input_list == '1':
    epg = float(input('Enter gate error rate '))
    epm = float(input('Enter measurement error rate '))
    loss = float(input('Enter loss rate '))
    n = int(input('Enter values for n for (n.m) QPC '))
    m = int(input('Enter value for m for (n,m) QPC '))
    px_correct, px_incorrect, pz_correct, pz_incorrect, p_success = qec.qpc(epg,epm,loss,n,m)
    print('The success probability of error correction for loss errors is', p_success)
    print('The logical error rate for X-basis is', px_incorrect)
    print('The logical error rate for Z-basis is', pz_incorrect)

if input_list == '2':
    epg = float(input('Enter gate error rate '))
    epd = float(input('Enter depolarization error rate '))
    loss = float(input('Enter loss rate '))
    N = int(input('Enter the number of qudits for [d,1,(d+1)/2] code '))
    px_correct, px_incorrect, pz_correct, pz_incorrect, p_success = qec.qpyc(epg,epd, loss, N)
    print('The success probability of error correction for loss errors is ', p_success)
    print('The logical error rate for X-basis is ', px_incorrect)
    print('The logical error rate for Z-basis is ', pz_incorrect)

if input_list == '3':
    epg = float(input('Enter gate error rate '))
    epd = float(input('Enter depolarization error rate '))
    loss = float(input('Enter loss rate '))
    N = int(input('Enter the number of qudits d for [[d,2k-d,d-k+1]]_d code '))
    k = int(input('Enter the number of parameter k for [[d,2k-d,d-k+1]]_d code '))
    px_correct, px_incorrect, pz_correct, pz_incorrect, p_success = qec.qpyc(epg,epd, loss, N)
    print('The success probability of error correction for loss errors is ', p_success)
    print('The logical error rate for X-basis is ', px_incorrect)
    print('The logical error rate for Z-basis is ', pz_incorrect)
