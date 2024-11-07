class motor:
    def status(self):
        return "O motor v8 está funcionando"
    
class pneu:
    def status(self):
        return "Os pneus estão em perfeitas condições"
    
class veiculo(motor, pneu):
    def status(self):
        motor_status = motor.status(self)
        pneu_status = pneu.status(self)
        return f"Status do veiculo:\n{motor_status}\n{pneu_status}"
    
veiculo = veiculo()
print(veiculo.status())