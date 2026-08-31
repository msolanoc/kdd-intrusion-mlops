"""
=============================================================================
Título: Estrategia de Reentrenamiento Inteligente y Trazabilidad en MLflow
Proyecto: MLOps Pipeline - KDD Cup 1999
Descripción: Implementa la lógica de decisión para el reentrenamiento basada en 
             la combinación de Data Drift (PSI > 0.25) Y Degradación de Rendimiento 
             (Performance < Threshold). Incluye la justificación teórica de por qué 
             Data Drift no equivale a Model Degradation.
=============================================================================
"""

import mlflow
import numpy as np

def evaluate_retraining_strategy():
    """
    Evalúa la necesidad de reentrenamiento combinando métricas de drift y rendimiento.
    
    JUSTIFICACIÓN TÉCNICA (Data Drift != Model Degradation):
    Un cambio en la distribución de las entradas P(X) (covariate shift) altera el PSI, 
    pero no necesariamente degrada el rendimiento del modelo f(X). Si la relación 
    condicional P(Y|X) —la frontera de decisión entre tráfico normal y ataques— 
    permanece intacta, el modelo seguirá clasificando correctamente. 
    Reentrenar a ciegas solo por cambios en P(X) desperdicia recursos y arriesga overfitting.
    Por ello, el pipeline exige una doble condición obligatoria:
    1. PSI > 0.25 (Deriva severa en datos)
    2. Performance < Threshold (Degradación real comprobada en métricas de negocio/f1)
    """
    
    mlflow.set_experiment("KDD-Retraining-Strategy")
    
    with mlflow.start_run(run_name="Retraining_Decision_Engine"):
        print("=================================================================")
        print("EVALUANDO ESTRATEGIA DE REENTRENAMIENTO (Punto R)")
        print("=================================================================")
        
        # Parámetros y umbrales de negocio justificados
        psi_value = 0.32          # Simula un PSI crítico detectado en producción (> 0.25)
        current_performance = 0.82 # F1-Score actual en producción
        performance_threshold = 0.88 # Umbral mínimo aceptable de negocio
        
        # Registrar parámetros y umbrales en MLflow
        mlflow.log_param("psi_observed", psi_value)
        mlflow.log_param("psi_threshold_alert", 0.25)
        mlflow.log_metric("current_performance", current_performance)
        mlflow.log_param("performance_threshold", performance_threshold)
        
        # Lógica de decisión combinada exigida por la rúbrica
        drift_condition = psi_value > 0.25
        degradation_condition = current_performance < performance_threshold
        
        trigger_retraining = drift_condition and degradation_condition
        
        # Registrar la decisión como métrica/parámetro en MLflow
        mlflow.log_metric("trigger_retraining_pipeline", 1 if trigger_retraining else 0)
        
        print(f"[*] Análisis de Deriva (PSI = {psi_value}): {'CRÍTICO (> 0.25)' if drift_condition else 'ESTABLE'}")
        print(f"[*] Análisis de Rendimiento (F1 = {current_performance}): {'DEGRADADO (< 0.88)' if degradation_condition else 'ÓPTIMO'}")
        print("-" * 65)
        
        if trigger_retraining:
            print("[ACCIÓN] --> CONDICIÓN CUMPLIDA: Se dispara el Pipeline de Reentrenamiento.")
            print("           Motivo: Existe Data Drift severo Y degradación real del modelo.")
            mlflow.set_tag("retraining_action", "TRIGGERED")
        else:
            print("[ACCIÓN] --> BLOQUEADO: No se requiere reentrenamiento.")
            print("           Motivo: El cambio en los datos no afectó la capacidad predictiva.")
            mlflow.set_tag("retraining_action", "SKIPPED")
            
        print("=================================================================")
        print("¡Estrategia y justificación registradas exitosamente en MLflow!")
        print("=================================================================")

if __name__ == "__main__":
    evaluate_retraining_strategy()