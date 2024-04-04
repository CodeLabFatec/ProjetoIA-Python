import io
import time
from flask import send_file
from openpyxl import Workbook

from repository.dados_ia import informacoesRepository


class ExportarRelatorio:

    def export_relatorio(data_inicial : str, data_final : str):

        relatorio = informacoesRepository.get_informacoes_for_export(data_inicial, data_final)
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