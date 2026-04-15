import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('gastos_exemplo.csv')

print('gastos mensais')
print(df.head())


df['data'] = pd.to_datetime(df['data'])
total = df['valor'].sum()
print(f"\nTotal de gastos: R$ {total:.2f}")


gastos_categoria = df.groupby('categoria')['valor'].sum()
print("\nGastos por categoria:")
print(gastos_categoria)

maior_categoria = gastos_categoria.idxmax()
print(f"\nCategoria com maio gasto: {maior_categoria}")

gastos_categoria.plot(kind='bar')
plt.title('gastos por categoria')
plt.xlabel('categoria')
plt.ylabel('valor (R$)')
plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()


plt.savefig('exemplo.png')
