import uno
from datetime import datetime
from com.sun.star.awt import MessageBoxButtons as MSG_BUTTONS


# -----------------------------
# TAXA DE CONVERSÃO
# -----------------------------
def get_rp_conversion_rate():
    soma = 30.42 + 32.83 + 33.37 + 33.86 + 34.22 + 35.53
    return soma / 6


# -----------------------------
# MESSAGE BOX
# -----------------------------
def show_message(mensagem, titulo="Conversão RP ↔ R$"):
    context = uno.getComponentContext()
    toolkit = context.ServiceManager.createInstanceWithContext(
        "com.sun.star.awt.Toolkit", context)

    msgbox = toolkit.createMessageBox(
        None,
        "infobox",
        MSG_BUTTONS.BUTTONS_OK,
        titulo,
        mensagem
    )
    msgbox.execute()


# -----------------------------
# RELATÓRIO AUTOMÁTICO
# -----------------------------
def gerar_relatorio(model, total_rp, total_reais, qtd, taxa):
    sheets = model.Sheets

    if sheets.hasByName("Relatório RP"):
        sheet = sheets.getByName("Relatório RP")
        sheet.clearContents(1023)
    else:
        sheets.insertNewByName("Relatório RP", sheets.getCount())
        sheet = sheets.getByName("Relatório RP")

    dados = [
        ("Data da conversão", datetime.now().strftime("%d/%m/%Y %H:%M")),
        ("Taxa usada (RP por R$)", round(taxa, 2)),
        ("Total de RP", total_rp),
        ("Total em R$", round(total_reais, 2)),
        ("Quantidade de células", qtd),
        ("Status", "Conversão realizada com sucesso")
    ]

    for i, (titulo, valor) in enumerate(dados):
        sheet.getCellByPosition(0, i).String = titulo
        if isinstance(valor, (int, float)):
            sheet.getCellByPosition(1, i).Value = valor
        else:
            sheet.getCellByPosition(1, i).String = valor


# -----------------------------
# RP → REAIS
# -----------------------------
def converter_para_reais():
    context = uno.getComponentContext()
    desktop = context.ServiceManager.createInstanceWithContext(
        "com.sun.star.frame.Desktop", context)
    model = desktop.getCurrentComponent()
    sheet = model.CurrentController.ActiveSheet

    taxa = get_rp_conversion_rate()

    linha = 1
    total_rp = 0
    total_reais = 0
    contador = 0

    while True:
        rp = sheet.getCellByPosition(0, linha).Value  # coluna A
        if rp <= 0:
            break

        reais = round(rp / taxa, 2)
        sheet.getCellByPosition(1, linha).Value = reais  # coluna B

        total_rp += rp
        total_reais += reais
        contador += 1
        linha += 1

    if contador == 0:
        show_message(
            "Nenhum valor válido encontrado na coluna A (RP).",
            "Erro de Conversão"
        )
        return

    gerar_relatorio(model, total_rp, total_reais, contador, taxa)
    show_message("Conversão de RP para R$ realizada com sucesso.")


# -----------------------------
# REAIS → RP
# -----------------------------
def converter_para_rp():
    context = uno.getComponentContext()
    desktop = context.ServiceManager.createInstanceWithContext(
        "com.sun.star.frame.Desktop", context)
    model = desktop.getCurrentComponent()
    sheet = model.CurrentController.ActiveSheet

    taxa = get_rp_conversion_rate()
    linha = 1
    contador = 0

    while True:
        reais = sheet.getCellByPosition(1, linha).Value  # coluna B
        if reais <= 0:
            break

        rp = round(reais * taxa)
        sheet.getCellByPosition(2, linha).Value = rp  # coluna C
        contador += 1
        linha += 1

    if contador == 0:
        show_message(
            "Nenhum valor válido encontrado na coluna B (R$).",
            "Erro de Conversão"
        )
        return

    show_message("Conversão de R$ para RP realizada com sucesso.")
