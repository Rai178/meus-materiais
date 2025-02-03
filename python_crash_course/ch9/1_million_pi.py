from mpmath import mp

# Define a precisão para 1 milhão de dígitos 
mp.dps = 1000000 + 1 # +1 para incluir o '3.' na frente

# Calcula pi
pi = mp.pi

# Remove o ponto decimal e os primeiros dois caracteres ('3.')
pi_digits = str(pi)[2:]

# Salva os dígitos em um arquivo
filename = 'python_crash_course\ch9\pi_million_digits.txt'
with open(filename, 'w') as file:
    file.write(pi_digits)

print(f"Arquivo '{filename}' com 1 milhão de dígitos de pi criado com sucesso")