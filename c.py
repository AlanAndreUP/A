import tkinter as tk

class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)
        self.head = 0          
        self.state = 'q0'      
    
    def step(self):
        symbol = self.tape[self.head]
        
        if self.state == 'q0':
            if symbol == '1':
                self.head += 1  
            elif symbol == '0':
                self.tape[self.head] = 'B'  
                self.state = 'q1'
                self.head += 1
            elif symbol == 'B':
                self.state = 'qf'  
        
        elif self.state == 'q1':
            if symbol == '1':
                self.tape[self.head] = 'B'  
                self.state = 'q2'
                self.head -= 1
            elif symbol == '0':
                self.head += 1
            elif symbol == 'B':
                self.state = 'qf'
        
        elif self.state == 'q2':
            if symbol == '1' or symbol == 'B':
                self.head += 1
                self.tape.insert(self.head, '1') 
                self.state = 'q0'
                self.head += 1

    def run(self):
        while self.state != 'qf':
            self.step()
    
    def get_tape(self):
        return ''.join(self.tape).strip('B')  


class TuringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Máquina de Turing para Suma en Unario")

   
        tk.Label(root, text="Ingrese números en unario (separados por 0):").pack(pady=10)
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)


        tk.Button(root, text="Calcular Suma", command=self.calculate_sum).pack(pady=10)


        self.result_label = tk.Label(root, text="Resultado en unario: ")
        self.result_label.pack(pady=5)

    def calculate_sum(self):
        tape_input = 'B' + self.entry.get() + 'B' 
        
     
        tm = TuringMachine(tape_input)
        tm.run()
     
        result_unary = tm.get_tape()
        result_decimal = len(result_unary) 
        self.result_label.config(text=f"Resultado en unario: {result_unary} (Decimal: {result_decimal})")

root = tk.Tk()
app = TuringApp(root)
root.mainloop()
