import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np
import torch
import time
import os
 
##############################
# UZIAS SAMIR GOMEZ MALDONADO
##############################
class modeloIA:
    # Configurar el dispositivo (GPU si está disponible, CPU si no)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Usando dispositivo: {device}")
    
    model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
    
    def get_text_embedding(text):
        embedding = model.encode(text)
        return embedding
    
    def calculate_cosine_similarity(embedding_1, embedding_2):
        a = np.array(embedding_1)
        b = np.array(embedding_2)
 
        dot_product = np.dot(a, b)
 
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)

        similarity = dot_product / (norm_a * norm_b)

        return similarity
 
    def procesar_similitud_del_coseno(self,textoA,textoB, umbral):
        start_time = time.time()
        
        try:
            #df = pd.read_excel(ruta_archivo)
            
            #if "DESCRIPCION_INCOMMING" not in df.columns or "DESCRIPCION_BANCO" not in df.columns:
            #   print("Error: Columnas no encontradas.")
             #   return df
            
            # Limpieza rápida: asegurar que todo sea string y manejar nulos
            #textos_incommin = df["DESCRIPCION_INCOMMING"].fillna("").astype(str).tolist()
            #textos_banco = df["DESCRIPCION_BANCO"].fillna("").astype(str).tolist()

            #print(f"Calculando embeddings en {device} para {len(df)} registros...")
            textos_incommin=textoA
            textos_banco=textoB

            emb1 = self.model.encode(
                  textoA,
                  convert_to_tensor=True)
            
            emb2 = self.model.encode(
                textoB,
                convert_to_tensor=True)
            
            print(f"Calculando embedding en {device} para {len(textoA)} y para {(len(textoB))}")
            # 2. PROCESAMIENTO EN BLOQUE (EL GOLPE A LA GPU)
            # convert_to_tensor=True mantiene los datos en la GPU para el siguiente paso
            processing_start = time.time()
            
            #emb_incommin = model.encode(textos_incommin, convert_to_tensor=True, show_progress_bar=True)
            #emb_banco = model.encode(textos_banco, convert_to_tensor=True, show_progress_bar=True)
            
            # 3. CÁLCULO DE SIMILITUD VECTORIZADO
            # util.cos_sim calcula todas las similitudes de un solo golpe en la GPU
            # .diagonal() extrae la similitud entre el par fila a fila
            #cos_sim_matrix = util.cos_sim(emb_incommin, emb_banco)
            #similarities = cos_sim_matrix.diagonal().cpu().tolist()
            similitud = util.cos_sim(emb1, emb2).item()
            processing_end = time.time()
            processing_time = processing_end - processing_start
            print(f"Tiempo de procesamiento de embeddings: {processing_time:.2f} segundos")
    
            # Crear DataFrame con resultados
            #df_resultados = df.copy()
            #df_resultados["SIMILITUD_COSENO"] = similarities
           # texto_resultados["SIMILITUF_COSENO"]=similarities
            
            # Clasificar
            def clasificar_valor(sim):
                if pd.isna(sim): return ""
                return "P" if sim >= umbral else "N"
            
            #df_resultados["VALOR_OBTENIDO"] = df_resultados["SIMILITUD_COSENO"].apply(clasificar_valor)
            
            # Resultado de comparación entre valor esperado y valor obtenido
            def evaluar_resultado(row):
                esperado = str(row.get("VALOR_ESPERADO", "")).strip().upper()
                obtenido = str(row.get("VALOR_OBTENIDO", "")).strip().upper()
                if (esperado == "T" and obtenido == "P") or (esperado == "F" and obtenido == "N"):
                    return "correcta"
                return "fallida"
            
            #df_resultados["RESULTADO"] = df_resultados.apply(evaluar_resultado, axis=1)
            
            # Guardar archivo
            #output_path = os.path.join(os.path.dirname(ruta_archivo), "Salida", "resultados_similitud.xlsx")
            #os.makedirs(os.path.dirname(output_path), exist_ok=True)
            #df_resultados.to_excel(output_path, index=False)
            
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Procesamiento completado. Archivo guardado en: {output_path}")
            print(f"Tiempo total de ejecución: {total_time:.2f} segundos")
            
            #return df_resultados
            

        except Exception as e:
            print(f"Error al procesar: {e}")
            return None