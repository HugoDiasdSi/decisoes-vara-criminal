"""
Rate Limiter para API do Gemini (tier free: 125 TPM)
"""

import time
from threading import Lock
from typing import Optional
import tiktoken


class RateLimiter:
    """
    Rate limiter para controlar chamadas à API do Gemini
    Tier Free: 125 tokens por minuto (TPM)
    """

    def __init__(self, tokens_per_minute: int = 125):
        """
        Inicializa o rate limiter

        Args:
            tokens_per_minute: Limite de tokens por minuto
        """
        self.tpm_limit = tokens_per_minute
        self.tokens_used = 0
        self.window_start = time.time()
        self.lock = Lock()

        # Usar tokenizer aproximado (tiktoken para GPT, mas serve como estimativa)
        try:
            self.encoding = tiktoken.get_encoding("cl100k_base")
        except:
            self.encoding = None

    def estimate_tokens(self, text: str) -> int:
        """
        Estima o número de tokens em um texto

        Args:
            text: Texto a estimar

        Returns:
            Número estimado de tokens
        """
        if self.encoding:
            try:
                return len(self.encoding.encode(text))
            except:
                pass

        # Fallback: aproximação grosseira
        # Em média, 1 token ≈ 4 caracteres em inglês
        # Para português, podemos usar 1 token ≈ 3.5 caracteres
        return len(text) // 3.5

    def wait_if_needed(self, estimated_tokens: int) -> float:
        """
        Aguarda se necessário para respeitar o rate limit

        Args:
            estimated_tokens: Número estimado de tokens a serem usados

        Returns:
            Tempo de espera em segundos
        """
        with self.lock:
            current_time = time.time()
            elapsed = current_time - self.window_start

            # Reset da janela após 60 segundos
            if elapsed >= 60:
                self.tokens_used = 0
                self.window_start = current_time
                elapsed = 0

            # Verificar se adicionar os tokens excederia o limite
            if self.tokens_used + estimated_tokens > self.tpm_limit:
                # Calcular tempo de espera necessário
                wait_time = 60 - elapsed

                if wait_time > 0:
                    print(f"⏳ Rate limit: aguardando {wait_time:.1f}s...")
                    time.sleep(wait_time)

                    # Reset após espera
                    self.tokens_used = 0
                    self.window_start = time.time()

            # Registrar uso de tokens
            self.tokens_used += estimated_tokens

            return 0

    def get_status(self) -> dict:
        """
        Retorna status atual do rate limiter

        Returns:
            Dicionário com status
        """
        with self.lock:
            current_time = time.time()
            elapsed = current_time - self.window_start

            if elapsed >= 60:
                tokens_remaining = self.tpm_limit
                time_until_reset = 0
            else:
                tokens_remaining = max(0, self.tpm_limit - self.tokens_used)
                time_until_reset = 60 - elapsed

            return {
                'tokens_used': self.tokens_used,
                'tokens_remaining': tokens_remaining,
                'time_until_reset': time_until_reset,
                'tpm_limit': self.tpm_limit
            }


def retry_with_exponential_backoff(
    func,
    max_retries: int = 3,
    initial_delay: float = 1,
    max_delay: float = 60
):
    """
    Decorator para retry com backoff exponencial

    Args:
        func: Função a decorar
        max_retries: Número máximo de tentativas
        initial_delay: Delay inicial em segundos
        max_delay: Delay máximo em segundos
    """
    def wrapper(*args, **kwargs):
        delay = initial_delay

        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    # Última tentativa, propagar erro
                    raise e

                # Verificar se é erro de rate limit
                error_msg = str(e).lower()
                if 'quota' in error_msg or 'rate limit' in error_msg or '429' in error_msg:
                    wait_time = min(delay * (2 ** attempt), max_delay)
                    print(f"⚠️ Rate limit atingido. Tentativa {attempt + 1}/{max_retries}. Aguardando {wait_time:.1f}s...")
                    time.sleep(wait_time)
                else:
                    # Erro diferente, propagar imediatamente
                    raise e

        return None

    return wrapper
