#import pandas as pd
from sentence_transformers import SentenceTransformer, util
from sentence_transformers.util import cos_sim
from app.src.schemas.TextoComparar import TextoComparar
import numpy as np
import torch
import time
import os
 
class ModeloIaComparar:
    # Configurar el dispositivo (GPU si está disponible, CPU si no)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Usando dispositivo: {device}")
    
    model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
    
    def get_text_embedding(self,text):
        embedding = self.model.encode(text,convert_to_tensor=True)
        return embedding
    
 
    def procesar_similitud_del_coseno(self, texto:TextoComparar, umbral):
        start_time = time.time()
        
        try:
            processing_start = time.time()
            emb1=self.get_text_embedding(texto.textoA)
            emb2=self.get_text_embedding(texto.textoB)

            print(f"Calculando embedding en {self.device}")

            similitud = cos_sim(emb1,emb2).item()

            iguales ="si" if similitud >= umbral else "no"
            end_time = time.time()

            total_time = end_time - start_time

            print(f"tiempo de duración{total_time}")

            return{
                "similitud":round(similitud*100),
                "iguales":iguales
            } 

        except Exception as e:
            print(f"Error al procesar: {e}")
            return None
