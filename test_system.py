"""
Script de teste para verificar se todos os componentes estão funcionando
"""

import sys
import os

def test_imports():
    """Testa se todos os módulos podem ser importados"""
    print("🔍 Testando imports...")

    try:
        import gradio as gr
        print("  ✓ Gradio")
    except ImportError as e:
        print(f"  ✗ Gradio: {e}")
        return False

    try:
        import PyPDF2
        print("  ✓ PyPDF2")
    except ImportError as e:
        print(f"  ✗ PyPDF2: {e}")
        return False

    try:
        import google.generativeai as genai
        print("  ✓ Google Generative AI")
    except ImportError as e:
        print(f"  ✗ Google Generative AI: {e}")
        return False

    try:
        from sentence_transformers import SentenceTransformer
        print("  ✓ Sentence Transformers")
    except ImportError as e:
        print(f"  ✗ Sentence Transformers: {e}")
        return False

    try:
        from utils import RAGSystem, extract_text_from_pdf, build_full_prompt
        print("  ✓ Utils customizados")
    except ImportError as e:
        print(f"  ✗ Utils: {e}")
        return False

    return True


def test_rag_system():
    """Testa o sistema RAG"""
    print("\n🔍 Testando sistema RAG...")

    try:
        from utils import RAGSystem

        rag = RAGSystem()

        # Adicionar documento de teste
        rag.add_document(
            filename="test.md",
            content="Decisão de recebimento de denúncia por tráfico de drogas",
            tags=["recebimento", "denúncia", "tráfico de drogas"],
            description="Teste de documento"
        )

        # Buscar
        results = rag.search_relevant_minutas("recebimento denúncia drogas", top_k=1)

        if results and len(results) > 0:
            print(f"  ✓ RAG funcionando - {len(results)} resultado(s) encontrado(s)")
            return True
        else:
            print("  ✗ RAG não retornou resultados")
            return False

    except Exception as e:
        print(f"  ✗ Erro no RAG: {e}")
        return False


def test_metadata_loading():
    """Testa carregamento de metadados"""
    print("\n🔍 Testando carregamento de metadados...")

    try:
        import json

        with open("minutas_metadata.json", "r", encoding="utf-8") as f:
            metadata = json.load(f)

        print(f"  ✓ {len(metadata)} minutas carregadas")

        # Verificar se os arquivos existem
        missing_files = []
        for item in metadata[:5]:  # Testar apenas os 5 primeiros
            if not os.path.exists(item["filename"]):
                missing_files.append(item["filename"])

        if missing_files:
            print(f"  ⚠️  Arquivos não encontrados: {missing_files}")
        else:
            print("  ✓ Todos os arquivos verificados estão presentes")

        return True

    except Exception as e:
        print(f"  ✗ Erro ao carregar metadados: {e}")
        return False


def test_prompt_builder():
    """Testa construção de prompts"""
    print("\n🔍 Testando construção de prompts...")

    try:
        from utils import build_full_prompt

        prompt = build_full_prompt(
            autos_text="Teste de autos processuais",
            task="Elaborar decisão",
            context="Contexto de teste",
            relevant_minutas=[{
                'filename': 'test.md',
                'content': 'Conteúdo de teste',
                'tags': ['teste'],
                'description': 'Descrição de teste',
                'similarity_score': 0.95
            }]
        )

        if len(prompt) > 100 and "RELATÓRIO PRÉVIO" in prompt:
            print("  ✓ Prompt construído com sucesso")
            print(f"  ℹ️  Tamanho do prompt: {len(prompt)} caracteres")
            return True
        else:
            print("  ✗ Prompt incompleto")
            return False

    except Exception as e:
        print(f"  ✗ Erro na construção do prompt: {e}")
        return False


def test_rate_limiter():
    """Testa o rate limiter"""
    print("\n🔍 Testando Rate Limiter...")

    try:
        from utils import RateLimiter

        # Criar rate limiter de teste
        limiter = RateLimiter(tokens_per_minute=1000)

        # Testar estimativa de tokens
        text = "Este é um texto de teste para estimar tokens."
        tokens = limiter.estimate_tokens(text)

        if tokens > 0:
            print(f"  ✓ Estimativa de tokens funcionando: {tokens} tokens")
        else:
            print("  ✗ Estimativa de tokens retornou 0")
            return False

        # Testar status
        status = limiter.get_status()
        if 'tokens_remaining' in status and 'tpm_limit' in status:
            print(f"  ✓ Status: {status['tokens_remaining']}/{status['tpm_limit']} tokens disponíveis")
            return True
        else:
            print("  ✗ Status incompleto")
            return False

    except Exception as e:
        print(f"  ✗ Erro no rate limiter: {e}")
        return False


def test_api_key():
    """Verifica se a API key está configurada"""
    print("\n🔍 Verificando API Key do Gemini...")

    api_key = os.getenv("GEMINI_API_KEY", "")

    if api_key:
        print("  ✓ GEMINI_API_KEY configurada")
        print(f"  ℹ️  Tamanho: {len(api_key)} caracteres")
        return True
    else:
        print("  ⚠️  GEMINI_API_KEY não configurada")
        print("     Configure a variável de ambiente antes de usar o sistema")
        return False


def main():
    """Executa todos os testes"""
    print("="*60)
    print("TESTE DO SISTEMA - Assessor Jurídico Criminal")
    print("="*60)

    results = {
        "Imports": test_imports(),
        "Sistema RAG": test_rag_system(),
        "Metadados": test_metadata_loading(),
        "Prompt Builder": test_prompt_builder(),
        "Rate Limiter": test_rate_limiter(),
        "API Key": test_api_key()
    }

    print("\n" + "="*60)
    print("RESUMO DOS TESTES")
    print("="*60)

    for test_name, result in results.items():
        status = "✓ PASSOU" if result else "✗ FALHOU"
        print(f"{test_name:.<40} {status}")

    all_passed = all(results.values())

    print("\n" + "="*60)
    if all_passed:
        print("✅ TODOS OS TESTES PASSARAM!")
        print("\nSistema pronto para uso!")
    else:
        print("⚠️  ALGUNS TESTES FALHARAM")
        print("\nVerifique os erros acima antes de prosseguir.")

    print("="*60)

    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
