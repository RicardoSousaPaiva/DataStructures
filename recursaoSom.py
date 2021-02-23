# FATEC - ESTRUTURAS DE DADOS - PROF. MASANORI
#Recursão somatória
#sd(1234) = 1+2+3+4    
def sd(n): 
    if n <= 9: return n
    return n%10 + sd(n//10)