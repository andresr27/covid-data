#!/bin/bash

# Taer el último minuto de log procesado

#scp tvfe-logs:/opt/api_ips/reportes/$(ssh tvfe-logs "ls -t /opt/api_ips/reportes | head -n1;") /opt/mapadecalor/archivos/
#echo "Esperano a que termine de procesar el úlitmo reporte de api"
#sleep 40


# Convert custom log to .csv

#cat log_elk | cut -d '"' -f2,4,6,8,10 | sed -e 's/"/,/g' | sed -e 's/,/:00,/' | sed -e 's/\//-/g' | sort > log_elk.csv

# Sent logs backup to export to other ELK

#cat log_elk.csv >> /var/log/elk/log_elk_bkup.csv

# vaciar logs para  no enviarlos de nuevo

#cat /dev/null > log_elk

#Post CSV to ELK json API pipeline NAME into index_pattern NAME
#09-11-2018 16:55:00,09-11-2018 16:55,Canelones,Atlántida,167.57.73.102

while read f1
do
   curl -XPOST '10.68.172.52:9200/heatmap5/station?pipeline=parse_logs_mdc2' -H "Content-Type: application/json" -u elastic:changeme -d "{ \"station\": \"$f1\" }"
done < log_elk.csv
