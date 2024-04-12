import io
import time
from datetime import *
from flask import send_file
from openpyxl import Workbook

from repository.dados_ia import informacoesRepository

class ExportarRelatorio:

    def export_relatorio_7_dias():

        wb = Workbook()

        sheet = wb.active
        sheet.title = "Relatorio"

        data = informacoesRepository.calcula_entrada_pessoas()

        for i, entry in enumerate(data[:7], start=3):
            sheet[f"C{i}"] = entry["data_entrada"]
            sheet[f"D{i}"] = entry["numero_pessoas"]

        if len(data) < 7:
            for i in range(len(data) + 3, 10):
                sheet[f"C{i}"] = ""
                sheet[f"D{i}"] = ""

        output = io.BytesIO()
        wb.save(output)
        output.seek(0)

        file_name = f"Relatorio_7_dias.xlsx"
        response = send_file(
            output,
            as_attachment=True,
            download_name=file_name,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response.headers['Content-Disposition'] = f'attachment; filename={file_name}'
        return response
    

    def export_relatorio_14_dias():

        wb = Workbook()

        sheet = wb.active
        sheet.title = "Relatorio"

        data = informacoesRepository.calcula_entrada_pessoas()

        for i, entry in enumerate(data[:14], start=3):
            sheet[f"C{i}"] = entry["data_entrada"]
            sheet[f"D{i}"] = entry["numero_pessoas"]

        if len(data) < 14:
            for i in range(len(data) + 3, 10):
                sheet[f"C{i}"] = ""
                sheet[f"D{i}"] = ""

        output = io.BytesIO()
        wb.save(output)
        output.seek(0)

        file_name = f"Relatorio_14_dias.xlsx"
        response = send_file(
            output,
            as_attachment=True,
            download_name=file_name,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response.headers['Content-Disposition'] = f'attachment; filename={file_name}'
        return response
