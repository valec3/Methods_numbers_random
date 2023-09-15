class Config:
    def __init__(self):
        self.size = "1000x800"
        self.title = "Generador de Numeros Pseudoaleatorios"
        self.fields = ["n","x0","x00","x0*x00","largo","centro","ri"]
        self.data = [
                (0,0,0,0,0,0,0)
            ]
        
# singleton
config = Config()
