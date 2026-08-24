"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """
        funçaõ de verificação com condicional de criticidade
    """
    
    if temperature < 800 and neutrons_emitted > 500  and temperature * neutrons_emitted < 500000:
        return True
    else:
        return False
  







def reactor_efficiency(voltage, current, theoretical_max_power):
    """
            função que traz  a faixa de potencia do reator em status de cores.
    """   
    generated_power = voltage * current
    eficiencia = generated_power / theoretical_max_power * 100
  
    
    if eficiencia >= 80:
        return 'green'
    elif eficiencia < 80 and eficiencia >= 60:
        return 'orange'
    elif eficiencia < 60 and eficiencia >= 30:
        return 'red'
    else:
        return 'black'

    
    

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """
            função que traz o mecanismo de segurança.
    """
    status_percent1 = temperature * neutrons_produced_per_second
    status = status_percent1 / threshold * 100



    if status < 90:
        return 'LOW'
    elif status  >= 90 and status <= 110:
        return 'NORMAL'
    else:
        return 'DANGER'

    
 
