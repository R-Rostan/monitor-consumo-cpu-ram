import multiprocessing
import time
import psutil
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

def geracao_dataframe(n):
    df = pd.DataFrame(
        {
            'A':[x for x in range(n)],
            'B':[x*3 for x in range(n)],
            'C':[x*11 for x in range(n)]
        }
    )
    for _ in range(n):
        df = pd.concat([df, df], ignore_index=True)
    return

p = multiprocessing.Process(target=geracao_dataframe, args=[25])
hr_inicio = time.perf_counter()
p.start()
print(f'Process PID: {p.pid}')

eixo_x = []
uso_memoria = []

while p.is_alive():
    monitor = psutil.Process(p.pid)
    data_hora_atual = dt.datetime.now()
    consumo_atual_mem = round(monitor.memory_percent(), 1)
    eixo_x.append(data_hora_atual)
    uso_memoria.append(consumo_atual_mem)

hr_fim = time.perf_counter()

fig, ax = plt.subplots() 
ax.plot(eixo_x, uso_memoria)
ax.set_title('Consumo de memória RAM')
ax.set_xlabel(f'Tempo de processamento: {round(hr_fim - hr_inicio, 1)} segundo(s)')
ax.set_ylabel('% Uso')
fig.savefig('consumo_ram.png')