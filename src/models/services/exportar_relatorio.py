import io
import time
from date import datetime
from flask import send_file
from openpyxl import Workbook

from repository.dados_ia import informacoesRepository


class ExportarRelatorio:

    def calcular_data_sete_dias_antes(data: str) -> str:

        data_formatada = datetime.strptime(datetime.now(), '%Y-%m-%d')
        data_anterior = data_formatada - timedelta(days=7)

        return data_anterior.strftime('%Y-%m-%d')

    def export_relatorio():

        data_inicial_anterior = ExportarRelatorio.calcular_data_sete_dias_antes(data_entrada)

        relatorio = informacoesRepository.get_informacoes_for_export(data_inicial_anterior)
        wb = Workbook()

        for sheet_name, data in relatorio.items():
            if data:
                sheet = wb.create_sheet(title=sheet_name)
                headers = list(data[0].keys())
                sheet.append(headers)
                for row in data:
                    sheet.append([row[header] for header in headers])

        output = io.BytesIO()
        wb.remove(wb["Sheet"])
        wb.save(output)
        output.seek(0)
        time.sleep(2)
        file_name = f"Relatorio-{data_inicial}-{data_final}.xlsx"
        response = send_file(
            output,
            as_attachment=True,
            download_name=file_name,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response.headers['Content-Disposition'] = f'attachment; filename={file_name}'
        return response