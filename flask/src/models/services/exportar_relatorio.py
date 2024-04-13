import io
import time
from datetime import *
from flask import send_file
from openpyxl import Workbook
from openpyxl import load_workbook
import os

from repository.dados_ia import informacoesRepository

class ExportarRelatorio:

    def traduzir_dia_da_semana(dia_da_semana):
        # Dicionário de mapeamento dos dias da semana de inglês para português
        dias_da_semana = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }

        # Retorna a tradução do dia da semana se estiver no dicionário, caso contrário, retorna o próprio dia
        return dias_da_semana.get(dia_da_semana, dia_da_semana)


    def export_relatorio_7_dias(template_filename):

        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'assets', template_filename))

        wb = load_workbook(template_path)
        sheet = wb.active

        data = informacoesRepository.calcula_entrada_pessoas()
        data_inicial = datetime.now().date()
        while data_inicial.strftime("%A") != "Monday":
            data_inicial -= timedelta(days=1)

        for i, entry in enumerate(data[:7], start=3):
            data_entrada_formatada = datetime.strptime(entry["data_entrada"], "%Y-%m-%d").strftime("%d/%m/%Y") if entry["data_entrada"] else ""
            sheet[f"C{i}"] = data_entrada_formatada
            sheet[f"D{i}"] = entry["numero_pessoas"]

            if entry["data_entrada"]:
                dia_da_semana = (data_inicial + timedelta(days=i-3)).strftime("%A")
                sheet[f"B{i}"] = ExportarRelatorio.traduzir_dia_da_semana(dia_da_semana)
            else:
                sheet[f"B{i}"] = ""

        if len(data) < 7:
            for i in range(len(data) + 3, 10):
                sheet[f"C{i}"] = ""
                sheet[f"D{i}"] = ""
                sheet[f"B{i}"] = ""

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

    def export_relatorio_14_dias(template_filename):

        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'assets', template_filename))

        wb = load_workbook(template_path)
        sheet = wb.active

        data = informacoesRepository.calcula_entrada_pessoas()
        data_inicial = datetime.now().date()
        while data_inicial.strftime("%A") != "Monday":
            data_inicial -= timedelta(days=1)

        for i, entry in enumerate(data[:14], start=3):
            data_entrada_formatada = datetime.strptime(entry["data_entrada"], "%Y-%m-%d").strftime("%d/%m/%Y") if entry["data_entrada"] else ""
            sheet[f"C{i}"] = data_entrada_formatada
            sheet[f"D{i}"] = entry["numero_pessoas"]

            if entry["data_entrada"]:
                dia_da_semana = (data_inicial + timedelta(days=i-3)).strftime("%A")
                sheet[f"B{i}"] = ExportarRelatorio.traduzir_dia_da_semana(dia_da_semana)
            else:
                sheet[f"B{i}"] = ""

        if len(data) < 14:
            for i in range(len(data) + 3, 17):
                sheet[f"C{i}"] = ""
                sheet[f"D{i}"] = ""
                sheet[f"B{i}"] = ""

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
