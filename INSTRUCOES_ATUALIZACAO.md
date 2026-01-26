# Instrucoes de Atualizacao - LED Driver 9000 Lumens

## Alteracoes Necessarias no KiCad

### 1. INDUTOR (CRITICO)

**Abra o arquivo:** `PLACA DRIVER RSENSE 10A.kicad_sch`

**Localize:** U$3 (Indutor)

**Altere:**
- Value: `NR8040T100M` → `SRP1265A-100M`
- Footprint: `8x8mm` → `12.5x12.5mm`

**No KiCad:**
1. Clique duplo no indutor U$3
2. Altere o campo "Value" para: `SRP1265A-100M 10uH 12A`
3. Clique em "Edit Footprint"
4. Selecione um footprint 12.5x12.5mm ou crie um novo

### 2. CAPACITOR C3

**Localize:** C3 (Capacitor eletrolitico)

**Altere:**
- Value: `47uF 63V` → `100uF 63V`
- Footprint: Manter ou ajustar para 8x10mm

### 3. CAPACITOR C4

**Localize:** C4 (Capacitor ceramico)

**Altere:**
- Value: `4.7uF 80V` → `10uF 100V`
- Footprint: Manter 1210

### 4. DIODO D1

**Localize:** D1 (Schottky principal)

**Altere:**
- Value: `B560A-13-F` → `B560C-13-F`
- Footprint: `SMA` → `SMC`

---

## Atualizacao do PCB

### Passo 1: Atualizar PCB do Schematic
1. Abra `PLACA DRIVER RSENSE 10A.kicad_pcb`
2. Menu: Tools → Update PCB from Schematic (F8)
3. Clique "Update PCB"

### Passo 2: Reposicionar Indutor
O novo indutor e maior (12.5mm vs 8mm):
1. Selecione o footprint do indutor
2. Mova para uma posicao com espaco
3. Re-roteie as trilhas conectadas

### Passo 3: Verificar Trilhas de Potencia
Certifique-se que:
- VIN, GND, LED+, LED- usam zonas de cobre (nao trilhas finas)
- Track width minimo para sinais: 0.25mm
- Track width para potencia: usar zonas/fills

### Passo 4: Rodar DRC
1. Menu: Inspect → Design Rules Checker
2. Corrigir todos os erros
3. Warnings podem ser ignorados se justificados

---

## Geracao de Gerbers

### Configuracao JLCPCB
1. Menu: File → Plot
2. Selecione layers:
   - F.Cu, B.Cu (cobre)
   - F.SilkS, B.SilkS (silkscreen)
   - F.Mask, B.Mask (solder mask)
   - Edge.Cuts (contorno)
3. Clique "Plot"
4. Clique "Generate Drill Files"

### Arquivos Gerados
```
projeto-F_Cu.gbr      (cobre frente)
projeto-B_Cu.gbr      (cobre verso)
projeto-F_SilkS.gbr   (silk frente)
projeto-B_SilkS.gbr   (silk verso)
projeto-F_Mask.gbr    (mask frente)
projeto-B_Mask.gbr    (mask verso)
projeto-Edge_Cuts.gbr (contorno)
projeto.drl           (furos)
projeto-NPTH.drl      (furos nao-metalizados)
```

### Upload JLCPCB
1. Acesse: https://cart.jlcpcb.com/quote
2. Arraste o ZIP com os Gerbers
3. Selecione opcoes:
   - Layers: 4 (ou 2 se simplificar)
   - PCB Thickness: 1.6mm
   - Copper Weight: 2oz (para 10A)
   - Surface Finish: HASL

---

## Footprint do Indutor 12.5mm

Se nao tiver o footprint, crie um novo:

```
Pad 1: SMD Rect 4.0 x 3.5mm @ (-5.0, 0)
Pad 2: SMD Rect 4.0 x 3.5mm @ (+5.0, 0)
Courtyard: 14 x 14mm
Silkscreen: Retangulo 12.5 x 12.5mm
```

Ou use um footprint existente similar:
- `Inductor_SMD:L_Bourns_SRP1265A`
- `Inductor_SMD:L_12x12mm`

---

## Checklist Final

- [ ] Indutor atualizado para 12A
- [ ] C3 atualizado para 100uF
- [ ] C4 atualizado para 10uF 100V
- [ ] D1 footprint SMC
- [ ] PCB atualizado do schematic
- [ ] Indutor reposicionado
- [ ] Trilhas re-roteadas
- [ ] DRC passou
- [ ] Gerbers gerados
- [ ] ZIP criado para JLCPCB

---

## Codigos LCSC para Pedido

| LCSC | Qtd | Componente |
|------|-----|------------|
| C131379 | 1 | A6211 Driver |
| C408337 | 1 | SRP1265A-100M Indutor 12A |
| C2933871 | 1 | Rsense 0.01R 3W |
| C134846 | 1 | Cap 100uF 63V |
| C1845 | 1 | Cap 10uF 100V |
| C85100 | 1 | B560C Schottky SMC |
| C14259 | 1 | ATtiny45 |
| C47779 | 1 | RT9068 LDO |
| C2290043 | 20 | LED 3535 450lm |
| C8678 | 20 | SS34 Schottky |
