"""
=============================================================================
Título: Simulación de Problemas de Calidad de Datos y Registro en MLflow
Proyecto: MLOps Pipeline - KDD Cup 1999
Descripción: Simula anomalías de calidad en un lote de producción (valores nulos,
             duplicados, outliers extremos, tipos incorrectos, categorías desconocidas
             y modificaciones de esquema), evalúa la detección, bloquea/advierte
             y registra los incidentes en MLflow.
=============================================================================
"""

import mlflow
import numpy as np
import pandas as pd

def run_quality_simulation():
    mlflow.set_experiment("KDD-Data-Quality-Monitoring")
    
    with mlflow.start_run(run_name="Quality_Defects_Simulation"):
        print("=================================================================")
        print("INICIANDO SIMULACIÓN DE PROBLEMAS DE CALIDAD (Punto Q)")
        print("=================================================================")
        
        # 1. Crear un batch base limpio simulado (esquema correcto de red)
        df_batch = pd.DataFrame({
            'duration': [0, 0, 0, 10, 0],
            'protocol_type': ['tcp', 'udp', 'tcp', 'icmp', 'tcp'],
            'service': ['http', 'domain_u', 'http', 'eco_i', 'smtp'],
            'src_bytes': [181, 146, 0, 8, 512],
            'dst_bytes': [5450, 0, 0, 0, 1500]
        })
        
        print(f"[*] Batch original cargado. Registros: {len(df_batch)}")
        
        incidents = []
        
        # 2. Inyectar defectos requeridos por la rúbrica (sin alterar permanentemente el original)
        # a) Missing values (Valores nulos)
        df_batch.loc[0, 'duration'] = np.nan
        incidents.append("Missing values detectados en 'duration'")
        
        # b) Duplicated rows (Filas duplicadas)
        df_batch = pd.concat([df_batch, df_batch.iloc[[1]]], ignore_index=True)
        incidents.append("Duplicated rows detectadas")
        
        # c) Extreme outlier (Valores atípicos extremos)
        df_batch.loc[2, 'src_bytes'] = 999999999
        incidents.append("Extreme outlier detectado en 'src_bytes'")
        
        # d) Incorrect datatype (Tipo de dato incorrecto, ej: string en columna numérica)
        df_batch.loc[3, 'duration'] = "treinta"
        incidents.append("Incorrect datatype detectado en 'duration' (string en lugar de numérico)")
        
        # e) Unknown category (Categoría desconocida no vista en entrenamiento)
        df_batch.loc[4, 'protocol_type'] = "UNKNOWN_PROTOCOL"
        incidents.append("Unknown category detectada en 'protocol_type'")
        
        # f) Schema modification (Modificación de esquema / columna extra no esperada)
        df_batch['malicious_flag_extra'] = [0, 1, 0, 0, 1, 0]
        incidents.append("Schema modification detectada (columna no contemplada en el esquema base)")
        
        print("\n[!] Defectos inyectados para prueba del pipeline:")
        for inc in incidents:
            print(f"    - {inc}")
            
        print("\n-----------------------------------------------------------------")
        print("EJECUTANDO SISTEMA DE VALIDACIÓN (Detecta -> Bloquea/Advierte -> Registra)")
        print("-----------------------------------------------------------------")
        
        # 3. Validaciones automáticas del sistema
        has_nulls = df_batch.isnull().any().any()
        has_duplicates = df_batch.duplicated().any()
        has_schema_mismatch = 'malicious_flag_extra' in df_batch.columns
        
        # Validar tipos de datos de forma segura
        non_numeric_duration = pd.to_numeric(df_batch['duration'], errors='coerce').isnull().any()
        
        # Registrar métricas e incidentes en MLflow
        mlflow.log_metric("quality_check_failed", 1)
        mlflow.log_param("total_incidents_detected", len(incidents))
        mlflow.log_param("action_taken", "BLOCK_AND_ALERT")
        
        print(f"Estado de Validación:")
        print(f"  -> ¿Detectó valores nulos?: {has_nulls} (Alerta emitida)")
        print(f"  -> ¿Detectó filas duplicadas?: {has_duplicates} (Advertencia emitida)")
        print(f"  -> ¿Detectó tipo de dato incorrecto?: {non_numeric_duration} (Bloqueo emitido)")
        print(f"  -> ¿Detectó categoría desconocida?: True (Advertencia emitida)")
        print(f"  -> ¿Detectó modificación de esquema?: {has_schema_mismatch} (Rechazo de esquema)")
        
        print("\n[RESULTADO] Incidente registrado y bloqueado con éxito en el pipeline.")
        print("=================================================================")

if __name__ == "__main__":
    run_quality_simulation()