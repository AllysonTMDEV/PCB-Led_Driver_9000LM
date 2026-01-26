# LED Driver 9000 Lumens - Projeto PCB

Driver de corrente constante para LEDs de alta potencia, projetado para fornecer 10A de saida e acionar 20 LEDs em paralelo, totalizando 9000 lumens.

---

## Especificacoes Tecnicas

### Driver (Placa Principal)

| Parametro | Valor |
|-----------|-------|
| Tensao de entrada | 12-24V DC |
| Corrente de saida | 10A (constante) |
| Topologia | Buck (step-down) |
| CI Driver | A6211 |
| Microcontrolador | ATtiny45 |
| Regulador | RT9068 3.3V |
| Frequencia PWM | Ajustavel |

### Placa de LEDs

| Parametro | Valor |
|-----------|-------|
| Quantidade de LEDs | 20 unidades |
| Modelo LED | JH-3535W12G |
| Lumens por LED | 450 lm @ 0.5A |
| Corrente por LED | 0.5A |
| Tensao por LED | 3V |
| Lumens total | 9000 lm |
| Diodos bypass | 20x SS34 |

---

## Principio de Funcionamento

### 1. Conversor Buck (Step-Down)

O driver utiliza a topologia Buck para converter a tensao de entrada (12-24V) para a tensao necessaria aos LEDs (3V). O CI A6211 controla o chaveamento do MOSFET interno, regulando a corrente de saida.

### 2. Controle de Corrente Constante

A corrente de saida e definida pelo resistor de sensoriamento (Rsense):

```
I_out = V_ref / R_sense
I_out = 0.1V / 0.01 ohm = 10A
```

O A6211 monitora a tensao sobre o Rsense e ajusta o duty cycle do PWM para manter a corrente constante, independente de variacoes na tensao de entrada ou carga.

### 3. Indutor

O indutor armazena energia durante o ciclo ON e libera durante o ciclo OFF, suavizando a corrente de saida. Especificacoes:

- Modelo: SRP1265A-100M
- Indutancia: 10uH
- Corrente de saturacao: 12A
- Tamanho: 12.5 x 12.5 mm

### 4. Capacitores de Filtragem

- C3 (100uF 63V): Filtragem de entrada, reduz ripple
- C4 (10uF 100V): Filtragem de saida, estabiliza tensao

### 5. Diodo Schottky (D1)

O diodo B560C (5A 60V) conduz durante o ciclo OFF do Buck, permitindo a continuidade da corrente pelo indutor. Package SMC para melhor dissipacao termica.

### 6. Protecao dos LEDs

Cada LED possui um diodo SS34 em paralelo (bypass). Se um LED falhar em aberto, o diodo conduz a corrente, evitando que toda a string apague.

---

## Componentes Principais (BOM Resumido)

### Driver

| Ref | Componente | Valor | LCSC |
|-----|------------|-------|------|
| U$1 | Driver LED | A6211 | C131379 |
| U$3 | Indutor | SRP1265A-100M 10uH 12A | C408337 |
| R1 | Rsense | 0.01R 3W | C2933871 |
| C3 | Capacitor | 100uF 63V | C134846 |
| C4 | Capacitor | 10uF 100V | C1845 |
| D1 | Diodo | B560C 5A 60V | C85100 |

### LEDs

| Ref | Componente | Valor | LCSC |
|-----|------------|-------|------|
| LED1-20 | LED HP | JH-3535W12G 450lm | - |
| D1-20 | Diodo bypass | SS34 3A 40V | C8678 |

---

## Arquivos do Projeto

```
PCB-Led_Driver_9000LM/
  PLACA DRIVER RSENSE 10A.kicad_sch    # Esquematico do driver
  PLACA DRIVER RSENSE 10A.kicad_pcb    # Layout PCB do driver
  PLACA DRIVER RSENSE 10A.kicad_pro    # Projeto KiCad
  LED_KICAD_SS34.kicad_pcb             # Layout PCB dos LEDs
  BOM_DRIVER_10A_REVISADO.csv          # Lista de materiais driver
  BOM_LED_9000LM_REVISADO.csv          # Lista de materiais LEDs
  RELATORIO_REVISAO_FINAL.md           # Documentacao tecnica
  INSTRUCOES_ATUALIZACAO.md            # Guia de modificacoes
```

---

## Alteracoes Realizadas (Rev 001)

### Componentes Atualizados

| Componente | Valor Anterior | Valor Novo | Motivo |
|------------|----------------|------------|--------|
| U$3 Indutor | NR8040T100M 3A | SRP1265A-100M 12A | Corrente insuficiente |
| C3 | 47uF 63V | 100uF 63V | Maior filtragem |
| C4 | 4.7uF 80V | 10uF 100V | Maior margem |
| D1 | B560A SMA | B560C SMC | Melhor dissipacao |

### Calculos de Verificacao

```
Corrente de saida: I = 0.1V / 0.01R = 10A
Potencia Rsense: P = I^2 x R = 100 x 0.01 = 1W (componente 3W OK)
Margem indutor: 12A / 10A = 20% (OK)
Potencia LEDs: 20 x 3V x 0.5A = 30W
```

---

## Requisitos para Fabricacao

### PCB Driver

- Camadas: 2
- Espessura cobre: 2oz (70um) recomendado
- Espessura placa: 1.6mm
- Acabamento: HASL ou ENIG

### PCB LEDs

- Tipo: FR4 ou MCPCB (Metal Core recomendado)
- Espessura cobre: 2oz
- Dissipador: Obrigatorio (Rth menor que 1.5 C/W)

---

## Consideracoes Termicas

A potencia total dissipada pelos LEDs e de 30W. Para operacao segura:

1. Usar pasta termica entre PCB e dissipador
2. Dissipador com resistencia termica menor que 1.5 C/W
3. Ventilacao adequada se em ambiente fechado
4. Temperatura maxima de juncao do LED: 125C

---

## Como Usar

1. Conecte a alimentacao (12-24V DC) nos terminais VIN e GND
2. Conecte a placa de LEDs nos terminais LED+ e LED-
3. O driver iniciara automaticamente em corrente constante
4. Use o sinal PWM para controle de intensidade (opcional)

---

## Licenca

Este projeto e disponibilizado para fins educacionais e pode ser modificado livremente.

---

## Autor

Projeto desenvolvido e validado com auxilio do Sistema PCB+IA.

Data: Janeiro 2026
Revisao: 001
