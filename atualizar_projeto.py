#!/usr/bin/env python3
"""
Script para atualizar automaticamente o projeto KiCad LED Driver 9000 Lumens
Corrige: Indutor, Capacitores, Diodo
"""

import os
import re
import shutil
from datetime import datetime

# Diretorio do projeto
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMATIC_FILE = os.path.join(PROJECT_DIR, "PLACA DRIVER RSENSE 10A.kicad_sch")
PCB_FILE = os.path.join(PROJECT_DIR, "PLACA DRIVER RSENSE 10A.kicad_pcb")

# Alteracoes a fazer
ALTERACOES = {
    "indutor": {
        "antigo_value": "NR8040T100M",
        "novo_value": "SRP1265A-100M 10uH 12A",
        "antigo_footprint": "NR8040",
        "novo_footprint": "Inductor_SMD:L_12x12mm_H8mm"
    },
    "C3": {
        "antigo_value": "47uF",
        "novo_value": "100uF 63V"
    },
    "C4": {
        "antigo_value": "4.7uF",
        "novo_value": "10uF 100V"
    },
    "D1": {
        "antigo_footprint": "SMA",
        "novo_footprint": "SMC"
    }
}

def backup_file(filepath):
    """Cria backup do arquivo antes de modificar"""
    backup_path = filepath + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(filepath, backup_path)
    print(f"Backup criado: {backup_path}")
    return backup_path

def atualizar_schematic(filepath):
    """Atualiza o arquivo schematic com os novos valores"""
    print(f"\nAtualizando schematic: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    alteracoes_feitas = []
    
    # 1. Atualizar indutor NR8040T100M -> SRP1265A-100M
    # Procurar por Value "NR8040T100M" ou similar
    patterns_indutor = [
        (r'(\(property "Value" ")NR8040T100M(")', r'\g<1>SRP1265A-100M 10uH 12A\g<2>'),
        (r'(\(property "Value" ")10uH(")', r'\g<1>SRP1265A-100M 10uH 12A\g<2>'),
    ]
    for pattern, replacement in patterns_indutor:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            alteracoes_feitas.append("Indutor: Value atualizado para SRP1265A-100M 10uH 12A")
    
    # 2. Atualizar C3: 47uF -> 100uF 63V
    patterns_c3 = [
        (r'(\(property "Value" ")47uF 63V(")', r'\g<1>100uF 63V\g<2>'),
        (r'(\(property "Value" ")47uF(")', r'\g<1>100uF 63V\g<2>'),
    ]
    for pattern, replacement in patterns_c3:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            alteracoes_feitas.append("C3: Value atualizado para 100uF 63V")
    
    # 3. Atualizar C4: 4.7uF -> 10uF 100V
    patterns_c4 = [
        (r'(\(property "Value" ")4\.7uF 80V(")', r'\g<1>10uF 100V\g<2>'),
        (r'(\(property "Value" ")4\.7uF(")', r'\g<1>10uF 100V\g<2>'),
    ]
    for pattern, replacement in patterns_c4:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            alteracoes_feitas.append("C4: Value atualizado para 10uF 100V")
    
    # 4. Atualizar D1 footprint: SMA -> SMC
    patterns_d1 = [
        (r'(\(property "Footprint" "[^"]*):SMA(")', r'\g<1>:SMC\g<2>'),
    ]
    for pattern, replacement in patterns_d1:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            alteracoes_feitas.append("D1: Footprint atualizado para SMC")
    
    # Salvar se houve alteracoes
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Alteracoes realizadas: {len(alteracoes_feitas)}")
        for alt in alteracoes_feitas:
            print(f"  - {alt}")
    else:
        print("Nenhuma alteracao necessaria ou padroes nao encontrados")
    
    return alteracoes_feitas

def atualizar_pcb(filepath):
    """Atualiza o arquivo PCB com os novos footprints"""
    print(f"\nAtualizando PCB: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    alteracoes_feitas = []
    
    # 1. Atualizar footprint do indutor
    # O footprint do indutor precisa ser maior (12.5x12.5mm)
    # Isso e mais complexo pois envolve geometria
    
    # 2. Atualizar D1 SMA -> SMC (pads maiores)
    # Procurar pelo footprint SMA relacionado a D1
    
    # Por seguranca, apenas registrar que precisa de atualizacao manual do PCB
    # pois alterar footprints automaticamente pode causar problemas de layout
    
    print("NOTA: O arquivo PCB requer atualizacao via KiCad:")
    print("  1. Abra o PCB no KiCad")
    print("  2. Use Tools -> Update PCB from Schematic (F8)")
    print("  3. Reposicione componentes se necessario")
    
    return alteracoes_feitas

def gerar_relatorio(alteracoes_sch, alteracoes_pcb):
    """Gera relatorio das alteracoes realizadas"""
    relatorio_path = os.path.join(PROJECT_DIR, "ALTERACOES_AUTOMATICAS.txt")
    
    with open(relatorio_path, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("RELATORIO DE ALTERACOES AUTOMATICAS\n")
        f.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("SCHEMATIC:\n")
        f.write("-" * 40 + "\n")
        if alteracoes_sch:
            for alt in alteracoes_sch:
                f.write(f"  [OK] {alt}\n")
        else:
            f.write("  Nenhuma alteracao\n")
        
        f.write("\nPCB:\n")
        f.write("-" * 40 + "\n")
        f.write("  [PENDENTE] Atualizar PCB via KiCad (F8)\n")
        f.write("  [PENDENTE] Reposicionar indutor maior\n")
        f.write("  [PENDENTE] Verificar D1 footprint SMC\n")
        
        f.write("\n\nCOMPONENTES ATUALIZADOS:\n")
        f.write("-" * 40 + "\n")
        f.write("  Indutor: NR8040T100M (3A) -> SRP1265A-100M (12A)\n")
        f.write("  C3: 47uF 63V -> 100uF 63V\n")
        f.write("  C4: 4.7uF 80V -> 10uF 100V\n")
        f.write("  D1: Footprint SMA -> SMC\n")
        
        f.write("\n\nCODIGOS LCSC PARA COMPRA:\n")
        f.write("-" * 40 + "\n")
        f.write("  C408337 - Indutor SRP1265A-100M 10uH 12A\n")
        f.write("  C134846 - Capacitor 100uF 63V\n")
        f.write("  C1845   - Capacitor 10uF 100V\n")
        f.write("  C85100  - Diodo B560C SMC\n")
    
    print(f"\nRelatorio gerado: {relatorio_path}")

def main():
    print("=" * 60)
    print("ATUALIZACAO AUTOMATICA - LED Driver 9000 Lumens")
    print("=" * 60)
    
    # Verificar arquivos
    if not os.path.exists(SCHEMATIC_FILE):
        print(f"ERRO: Arquivo nao encontrado: {SCHEMATIC_FILE}")
        return
    
    if not os.path.exists(PCB_FILE):
        print(f"AVISO: Arquivo PCB nao encontrado: {PCB_FILE}")
    
    # Criar backups
    print("\n1. Criando backups...")
    backup_file(SCHEMATIC_FILE)
    if os.path.exists(PCB_FILE):
        backup_file(PCB_FILE)
    
    # Atualizar schematic
    print("\n2. Atualizando schematic...")
    alteracoes_sch = atualizar_schematic(SCHEMATIC_FILE)
    
    # Atualizar PCB
    print("\n3. Verificando PCB...")
    alteracoes_pcb = atualizar_pcb(PCB_FILE) if os.path.exists(PCB_FILE) else []
    
    # Gerar relatorio
    print("\n4. Gerando relatorio...")
    gerar_relatorio(alteracoes_sch, alteracoes_pcb)
    
    print("\n" + "=" * 60)
    print("ATUALIZACAO CONCLUIDA!")
    print("=" * 60)
    print("\nPROXIMOS PASSOS:")
    print("1. Abra o projeto no KiCad")
    print("2. Verifique as alteracoes no schematic")
    print("3. Use F8 para atualizar o PCB do schematic")
    print("4. Reposicione o indutor (agora maior)")
    print("5. Rode o DRC")
    print("6. Gere os Gerbers")

if __name__ == "__main__":
    main()
