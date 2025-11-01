"""
Sistema RAG (Retrieval-Augmented Generation) para busca de minutas relevantes
"""

import json
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class RAGSystem:
    """Sistema de busca e recuperação de minutas jurídicas"""

    def __init__(self, model_name: str = "neuralmind/bert-base-portuguese-cased"):
        """
        Inicializa o sistema RAG

        Args:
            model_name: Nome do modelo de embedding a ser usado
        """
        self.documents = []
        self.embeddings = []

        # Usar modelo BERT em português
        try:
            self.model = SentenceTransformer(model_name)
        except:
            # Fallback para modelo multilíngue se o português não estiver disponível
            self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

    def add_document(self, filename: str, content: str, tags: List[str], description: str):
        """
        Adiciona um documento ao sistema RAG

        Args:
            filename: Nome do arquivo
            content: Conteúdo completo do documento
            tags: Tags/categorias do documento
            description: Descrição do documento
        """
        # Criar texto combinado para embedding
        combined_text = f"{description} {' '.join(tags)}"

        # Gerar embedding
        embedding = self.model.encode(combined_text)

        # Armazenar documento e embedding
        self.documents.append({
            'filename': filename,
            'content': content,
            'tags': tags,
            'description': description,
            'combined_text': combined_text
        })
        self.embeddings.append(embedding)

    def search_relevant_minutas(self, query: str, top_k: int = 3) -> List[Dict]:
        """
        Busca as minutas mais relevantes para uma consulta

        Args:
            query: Consulta/descrição do caso
            top_k: Número de minutas a retornar

        Returns:
            Lista com as minutas mais relevantes
        """
        if not self.documents:
            return []

        # Gerar embedding da consulta
        query_embedding = self.model.encode(query)

        # Calcular similaridade com todos os documentos
        similarities = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]

        # Obter índices dos top_k documentos mais similares
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        # Retornar documentos mais relevantes
        results = []
        for idx in top_indices:
            doc = self.documents[idx]
            results.append({
                'filename': doc['filename'],
                'content': doc['content'],
                'tags': doc['tags'],
                'description': doc['description'],
                'similarity_score': float(similarities[idx])
            })

        return results

    def search_by_tags(self, tags: List[str], top_k: int = 5) -> List[Dict]:
        """
        Busca documentos por tags específicas

        Args:
            tags: Lista de tags a buscar
            top_k: Número de resultados

        Returns:
            Lista de documentos que contêm as tags
        """
        results = []

        for doc in self.documents:
            # Verificar quantas tags coincidem
            matching_tags = set(tags).intersection(set(doc['tags']))

            if matching_tags:
                results.append({
                    'filename': doc['filename'],
                    'content': doc['content'],
                    'tags': doc['tags'],
                    'description': doc['description'],
                    'matching_tags': list(matching_tags),
                    'match_score': len(matching_tags) / len(tags)
                })

        # Ordenar por score de match
        results.sort(key=lambda x: x['match_score'], reverse=True)

        return results[:top_k]

    def search_by_keywords(self, keywords: List[str], top_k: int = 5) -> List[Dict]:
        """
        Busca documentos por palavras-chave

        Args:
            keywords: Lista de palavras-chave
            top_k: Número de resultados

        Returns:
            Lista de documentos que contêm as palavras-chave
        """
        results = []

        for doc in self.documents:
            # Verificar presença de keywords no texto combinado
            text_lower = doc['combined_text'].lower()
            matching_keywords = [kw for kw in keywords if kw.lower() in text_lower]

            if matching_keywords:
                results.append({
                    'filename': doc['filename'],
                    'content': doc['content'],
                    'tags': doc['tags'],
                    'description': doc['description'],
                    'matching_keywords': matching_keywords,
                    'match_score': len(matching_keywords) / len(keywords)
                })

        # Ordenar por score
        results.sort(key=lambda x: x['match_score'], reverse=True)

        return results[:top_k]

    def hybrid_search(self, query: str, tags: List[str] = None, keywords: List[str] = None, top_k: int = 3) -> List[Dict]:
        """
        Busca híbrida combinando similaridade semântica, tags e keywords

        Args:
            query: Consulta textual
            tags: Tags opcionais
            keywords: Palavras-chave opcionais
            top_k: Número de resultados

        Returns:
            Lista de documentos mais relevantes
        """
        # Buscar por similaridade semântica
        semantic_results = self.search_relevant_minutas(query, top_k=top_k * 2)

        # Se houver tags, filtrar/priorizar por tags
        if tags:
            tag_results = self.search_by_tags(tags, top_k=top_k * 2)
            # Combinar resultados
            filenames_semantic = {r['filename']: r for r in semantic_results}
            filenames_tags = {r['filename']: r for r in tag_results}

            # Priorizar documentos que aparecem em ambas as buscas
            combined = []
            for filename in filenames_semantic:
                if filename in filenames_tags:
                    # Documento aparece em ambas - alta prioridade
                    doc = filenames_semantic[filename]
                    doc['combined_score'] = doc['similarity_score'] + filenames_tags[filename]['match_score']
                    combined.append(doc)

            # Adicionar resultados únicos de cada busca
            for r in semantic_results:
                if r['filename'] not in [c['filename'] for c in combined]:
                    r['combined_score'] = r['similarity_score']
                    combined.append(r)

            for r in tag_results:
                if r['filename'] not in [c['filename'] for c in combined]:
                    r['combined_score'] = r['match_score']
                    combined.append(r)

            # Ordenar por score combinado
            combined.sort(key=lambda x: x['combined_score'], reverse=True)
            semantic_results = combined[:top_k]

        # Se houver keywords, aplicar boost adicional
        if keywords:
            for result in semantic_results:
                text_lower = result['description'].lower() + ' '.join(result['tags']).lower()
                keyword_matches = sum(1 for kw in keywords if kw.lower() in text_lower)
                result['keyword_boost'] = keyword_matches / len(keywords) if keywords else 0

            semantic_results.sort(
                key=lambda x: x.get('combined_score', x['similarity_score']) + x.get('keyword_boost', 0),
                reverse=True
            )

        return semantic_results[:top_k]

    def get_document_by_filename(self, filename: str) -> Dict:
        """
        Recupera um documento específico pelo nome do arquivo

        Args:
            filename: Nome do arquivo

        Returns:
            Documento ou None se não encontrado
        """
        for doc in self.documents:
            if doc['filename'] == filename:
                return doc
        return None

    def get_all_tags(self) -> List[str]:
        """
        Retorna todas as tags únicas do sistema

        Returns:
            Lista de tags únicas
        """
        all_tags = set()
        for doc in self.documents:
            all_tags.update(doc['tags'])
        return sorted(list(all_tags))

    def get_statistics(self) -> Dict:
        """
        Retorna estatísticas do sistema RAG

        Returns:
            Dicionário com estatísticas
        """
        return {
            'total_documents': len(self.documents),
            'total_tags': len(self.get_all_tags()),
            'all_tags': self.get_all_tags(),
            'avg_tags_per_doc': np.mean([len(doc['tags']) for doc in self.documents]) if self.documents else 0
        }
