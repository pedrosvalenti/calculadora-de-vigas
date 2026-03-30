import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        L = float(entry_L.get())
        q = float(entry_q.get())
        sigma = float(entry_sigma.get())

        # Cálculos
        M = (q * L**2) / 8
        M_kgf_cm = M * 100 * 100
        W = M_kgf_cm / sigma
        f_max = (L * 100) / 200

        # Sugestão de perfil
        if W <= 500:
            perfil = "I 200"
        elif W <= 1000:
            perfil = "I 300"
        elif W <= 2000:
            perfil = "I 400"
        else:
            perfil = "Acima de I 400"

        # Criar modal
        modal = tk.Toplevel(app)
        modal.title("Resultado do Cálculo")
        modal.geometry("380x420")
        modal.resizable(False, False)
        modal.configure(bg=cor_fundo)
        modal.transient(app)
        modal.grab_set()

        # Centralizar modal na tela
        modal.update_idletasks()
        x = app.winfo_x() + (app.winfo_width() // 2) - (modal.winfo_width() // 2)
        y = app.winfo_y() + (app.winfo_height() // 2) - (modal.winfo_height() // 2)
        modal.geometry(f"+{x}+{y}")

        # Cabeçalho do modal
        header = tk.Frame(modal, bg=cor_titulo, height=60)
        header.pack(fill=tk.X, padx=0, pady=0)

        tk.Label(
            header,
            text="Resultado do Cálculo",
            font=("Segoe UI", 14, "bold"),
            bg=cor_titulo,
            fg="white"
        ).pack(pady=12)

        # Conteúdo do resultado
        content = tk.Frame(modal, bg=cor_fundo)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        resultado_texto = (
            f"Momento: {M:.2f} kN.m\n\n"
            f"W necessário: {W:.2f} cm³\n\n"
            f"Flecha máxima: {f_max:.2f} cm\n\n"
            f"Perfil sugerido: {perfil}"
        )

        tk.Label(
            content,
            text=resultado_texto,
            font=("Segoe UI", 11),
            bg=cor_fundo,
            fg=cor_label,
            justify="left",
            wraplength=340
        ).pack(fill=tk.BOTH, expand=True)

        # Botão de fechar
        tk.Button(
            modal,
            text="Fechar",
            command=modal.destroy,
            bg="#cccccc",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            activebackground="#aaaaaa",
            activeforeground="black"
        ).pack(fill=tk.X, padx=20, pady=15, ipady=8)

    except:
        messagebox.showerror("Erro", "Preencha os valores corretamente!")

# Professional Color Scheme
cor_fundo = "#ffffff"
cor_titulo = "#007acc"
cor_label = "#333333"
cor_entrada = "#ffffff"
cor_botao = "#007acc"
cor_resultado = "#f5f5f5"

# Janela
app = tk.Tk()
app.title("Calculadora de Vigas")
app.geometry("400x480")
app.resizable(False, False)
app.configure(bg=cor_fundo)

# Título
titulo_frame = tk.Frame(app, bg=cor_titulo, height=80)
titulo_frame.pack(fill=tk.X, padx=0, pady=0)

tk.Label(
    titulo_frame, 
    text="Calculadora de Vigas", 
    font=("Segoe UI", 18, "bold"),
    bg=cor_titulo,
    fg="white"
).pack(pady=15)

tk.Label(
    titulo_frame,
    text="Dimensionamento de Vigas de Aço",
    font=("Segoe UI", 10),
    bg=cor_titulo,
    fg="#e0e0e0"
).pack()

# Frame de entradas
entrada_frame = tk.Frame(app, bg=cor_fundo)
entrada_frame.pack(pady=20, padx=20, fill=tk.X)
tk.Label(entrada_frame, text="Comprimento (m):", font=("Segoe UI", 11, "bold"), bg=cor_fundo, fg=cor_label).pack(anchor="w", pady=(0, 5))
entry_L = tk.Entry(entrada_frame, font=("Segoe UI", 11), bg=cor_entrada, relief="flat", bd=0)
entry_L.pack(fill=tk.X, pady=(0, 15), ipady=8)

# Carga
tk.Label(entrada_frame, text="Carga (kN/m):", font=("Segoe UI", 11, "bold"), bg=cor_fundo, fg=cor_label).pack(anchor="w", pady=(0, 5))
entry_q = tk.Entry(entrada_frame, font=("Segoe UI", 11), bg=cor_entrada, relief="flat", bd=0)
entry_q.pack(fill=tk.X, pady=(0, 15), ipady=8)

# Tensão
tk.Label(entrada_frame, text="Tensão (kgf/cm²):", font=("Segoe UI", 11, "bold"), bg=cor_fundo, fg=cor_label).pack(anchor="w", pady=(0, 5))
entry_sigma = tk.Entry(entrada_frame, font=("Segoe UI", 11), bg=cor_entrada, relief="flat", bd=0)
entry_sigma.pack(fill=tk.X, pady=(0, 20), ipady=8)

# Botão
tk.Button(
    entrada_frame, 
    text="CALCULAR", 
    command=calcular, 
    bg=cor_botao, 
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    cursor="hand2",
    activebackground="#005a9e",
    activeforeground="white",
    height=2
).pack(fill=tk.X, pady=(0, 20))

# Rodar
app.mainloop()