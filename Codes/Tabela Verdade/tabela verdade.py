import itertools
import tkinter as tk

# definir operadores lógicos
def E(*args):
    return all(args)

def OU(*args):
    return any(args)

def NAO(a):
    return not a

def OU_EXCLUSIVO(a, b):
    return (a and not b) or (not a and b)

# definir função de tabela verdade
def tabela_verdade(operacao, n):
    table = tk.Toplevel(root)
    table.title(operacao.__name__)
    for i in range(n):
        tk.Label(table, text=f"{'A' if i == 0 else chr(65+i)}").grid(row=0, column=i)
    tk.Label(table, text="Resultado").grid(row=0, column=n)
    tk.Label(table, text="-" * 20).grid(row=1, column=0, columnspan=n+1)
    for values in itertools.product((True, False), repeat=n):
        resultado = operacao(*values)
        row = len(table.grid_slaves()) // (n+1) + 2
        for i, value in enumerate(values):
            tk.Label(table, text=str(value)).grid(row=row, column=i)
        tk.Label(table, text=str(resultado)).grid(row=row, column=n)

# criar interface gráfica
root = tk.Tk()
root.title("Tabelas Verdade")
tk.Label(root, text="Número de Variáveis:").grid(row=0, column=0)
var_entry = tk.Entry(root)
var_entry.grid(row=0, column=1)
tk.Button(root, text="E", command=lambda: tabela_verdade(E, int(var_entry.get()))).grid(row=1, column=0)
tk.Button(root, text="OU", command=lambda: tabela_verdade(OU, int(var_entry.get()))).grid(row=1, column=1)
tk.Button(root, text="NÃO", command=lambda: tabela_verdade(NAO, 1)).grid(row=2, column=0)
tk.Button(root, text="OU_EXCLUSIVO", command=lambda: tabela_verdade(OU_EXCLUSIVO, int(var_entry.get()))).grid(row=2, column=1)

# iniciar loop de eventos
root.mainloop()
