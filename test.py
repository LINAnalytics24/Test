import pandas as pd
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os

# Creazione di più DataFrame di esempio
data1 = {
    "C": ["S"],
    "S": ["CN"],
    "C": ["BO"],
    "D": ["B"],
    "C": ["B"],
    "A": [""]
}

data2 = {
    "C": ["S"],
    "S": ["CN"],
    "C": ["BO"],
    "D": ["B"],
    "C": ["B"],
    "A": [""]
}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Lista di DataFrame e relativi titoli
tables = [(df1, "2024"), (df2, "Servizi")]

# Variabili per le immagini
logo_image_1 = ""
logo_image_2 = ""

# Titolo e sottotitolo
Title = 'ALLEGATO'
Subtitle = 'Questo template è stato generato tramite uno script che compila un template HTML'
# Creazione dell'ambiente Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.from_string('''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Template Allegato</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .header, .footer { width: 100%; }
        .header { height: 50px; background-color: #ff0000; }
        .footer { height: 30px; background-color: #ff0000; margin-top: 20px; }
        .logo { display: block; margin: 20px auto; }
        .content { text-align: center; }
        .table-container { margin: 20px 100px; } /* Margini di 100px intorno alle tabelle */
        .table-title { margin: 40px 0 20px; font-size: 1.5em; font-weight: bold; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: center; }

        /* Queste regole CSS si applicano solo quando si visualizza il documento su schermo */
        @media screen {
            th { background-color: #ff0000; color: #fff; }
        }

        /* Queste regole CSS si applicano solo quando si stampa il documento */
        @media print {
            .header, .footer {display:none;}
            table { 
                page-break-inside:auto; 
                table-layout: fixed; /* Imposta la larghezza delle colonne in base al contenuto */
                width: 100%; /* Assicura che la tabella non si estenda oltre i limiti del foglio */

            }
            tr { 
                page-break-inside:avoid; 
                page-break-after:auto; 
            }
            thead { display:table-header-group; }
            tfoot { display:table-footer-group; }
            @page {
                margin: 20mm 10mm; /* Riduci i margini su tutti i lati */
            }
            th, td { font-size: 10px; } /* Riduci la dimensione del carattere nei dati delle tabelle */
            .header, .footer { margin-left: -10mm; margin-right: -10mm; } /* Compensa i margini per la striscia rossa */
        }
    </style>
</head>
<body>
    <div class="header"></div>
    <img src="{{ logo_image_1 }}" alt="Logo" width="400" height="200" class="logo">
    <div class="content">
        <h1>{{ Title }}</h1>
        <p>{{ Subtitle }}</p>
        {% for df, title in tables %}
        <div class="table-container">
            <div class="table-title">{{ title }}</div>
            <table>
                <thead>
                    <tr>
                        {% for col in df.columns %}
                        <th>{{ col }}</th>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody>
                    {% for index, row in df.iterrows() %}
                    <tr>
                        {% for col in df.columns %}
                        <td>{{ row[col] }}</td>
                        {% endfor %}
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% endfor %}
    <p>ALLEGATO</p>
     <img src="{{ logo_image_2 }}" alt="Logo" width="300" height="80" class="Logo">
    </div>
    <div class="footer"></div>
</body>
</html>
''')
# Rendering del template con i dati e le immagini
html_output = template.render(Title=Title, Subtitle=Subtitle, tables=tables, logo_image_1=logo_image_1,
                              logo_image_2=logo_image_2)
