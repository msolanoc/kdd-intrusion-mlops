"""
=============================================================================
Título: Script de Simulación de Producción, Data Drift y Tracking en MLflow
Proyecto: MLOps Pipeline - KDD Cup 1999
Descripción: Divide los datos en un conjunto de referencia y tres lotes de
             producción (Batch 1, 2 y 3), calcula el Population Stability Index (PSI)
             y registra formalmente los resultados y umbrales en MLflow.
=============================================================================
"""

import mlflow
import numpy as np
import pandas as pd

def calculate_psi(reference, production, bins=10):
    """Calcula el Population Stability Index (PSI) entre dos distribuciones."""
    reference = np.array(reference)
    production = np.array(production)
    
    percentiles = np.linspace(0, 100, bins + 1)
    bin_edges = np.percentile(reference, percentiles)
    bin_edges[0] = -np.inf
    bin_edges[-1] = np.inf
    
    ref_counts, _ = np.histogram(reference, bins=bin_edges)
    prod_counts, _ = np.histogram(production, bins=bin_edges)
    
    ref_props = np.where(ref_counts == 0, 0.0001, ref_counts) / len(reference)
    prod_props = np.where(prod_counts == 0, 0.0001, prod_counts) / len(production)
    
    psi_value = np.sum((prod_props - ref_props) * np.log(prod_props / ref_props))
    return psi_value

def evaluate_drift_with_mlflow():
    """Ejecuta la simulación y realiza el tracking completo en MLflow."""
    mlflow.set_experiment("KDD-Production-Data-Drift")
    
    with mlflow.start_run(run_name="Drift_Simulation_Batches"):
        print("=================================================================")
        print("INICIANDO SIMULACIÓN DE DRIFT Y TRACKING EN MLFLOW")
        print("=================================================================")
        
        np.random.seed(42)
        reference_data = np.random.normal(loc=0.0, scale=1.0, size=1000)
        
        batches = {
            "PRODUCTION BATCH 1": np.random.normal(loc=0.02, scale=1.01, size=1000),
            "PRODUCTION BATCH 2": np.random.normal(loc=0.25, scale=1.2, size=1000),
            "PRODUCTION BATCH 3": np.random.normal(loc=0.80, scale=1.6, size=1000)
        }
        
        # Registrar umbrales de referencia en MLflow como parámetros
        mlflow.log_param("psi_threshold_warning", 0.10)
        mlflow.log_param("psi_threshold_alert", 0.25)
        
        for batch_name, data in batches.items():
            psi = calculate_psi(reference_data, data)
            
            # Registrar métrica en MLflow con una clave limpia para la UI
            metric_key = batch_name.lower().replace(" ", "_") + "_psi"
            mlflow.log_metric(metric_key, psi)
            
            if psi < 0.10:
                status = "OK (Estable)"
            elif 0.10 <= psi < 0.25:
                status = "WARNING (Deriva moderada)"
            else:
                status = "ALERT (Deriva crítica - Requiere Reentrenamiento)"
                
            print(f"[{batch_name}] -> PSI = {psi:.4f} -> Estado: {status}")
            
        print("=================================================================")
        print("¡Métricas de drift registradas exitosamente en MLflow!")
        print("=================================================================")

if __name__ == "__main__":
    evaluate_drift_with_mlflow()